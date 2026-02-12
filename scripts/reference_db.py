#!/usr/bin/env python3
"""
Verified Reference Database Manager
Prevents citation hallucinations by maintaining a BigQuery-backed
reference database with verification tracking.
"""

import os
import json
import hashlib
from datetime import datetime
from typing import Optional, List, Dict, Any
from dataclasses import dataclass, asdict
from google.cloud import bigquery
from google.oauth2 import service_account

# Configuration
PROJECT_ID = "openclaw1-20260130"
DATASET_ID = "agent_research"
CREDENTIALS_PATH = "/root/.config/google/service-account.json"

@dataclass
class Reference:
    """A verified academic reference."""
    reference_id: str
    title: str
    authors: List[str]
    year: int
    venue: Optional[str] = None
    venue_type: Optional[str] = None
    doi: Optional[str] = None
    url: Optional[str] = None
    arxiv_id: Optional[str] = None
    verification_status: str = "unverified"  # 'verified', 'unverified', 'disputed'
    bibtex_entry: Optional[str] = None
    abstract: Optional[str] = None
    keywords: List[str] = None
    notes: Optional[str] = None
    
    def __post_init__(self):
        if self.keywords is None:
            self.keywords = []
    
    def content_hash(self) -> str:
        """Generate hash of key fields for integrity checking."""
        content = f"{self.title}:{','.join(self.authors)}:{self.year}:{self.doi or ''}"
        return hashlib.sha256(content.encode()).hexdigest()[:16]
    
    def to_bigquery_row(self) -> Dict[str, Any]:
        """Convert to BigQuery row format."""
        return {
            "reference_id": self.reference_id,
            "title": self.title,
            "authors": self.authors,
            "year": self.year,
            "venue": self.venue,
            "venue_type": self.venue_type,
            "doi": self.doi,
            "url": self.url,
            "arxiv_id": self.arxiv_id,
            "verification_status": self.verification_status,
            "verified_at": datetime.utcnow().isoformat() if self.verification_status == "verified" else None,
            "verified_by": "manual" if self.verification_status == "verified" else None,
            "bibtex_entry": self.bibtex_entry,
            "abstract": self.abstract,
            "keywords": self.keywords,
            "content_hash": self.content_hash(),
            "last_checked": datetime.utcnow().isoformat(),
            "notes": self.notes,
        }


class ReferenceDatabase:
    """BigQuery-backed reference database."""
    
    def __init__(self):
        credentials = service_account.Credentials.from_service_account_file(
            CREDENTIALS_PATH,
            scopes=['https://www.googleapis.com/auth/bigquery']
        )
        self.client = bigquery.Client(credentials=credentials, project=PROJECT_ID)
        self.dataset_ref = f"{PROJECT_ID}.{DATASET_ID}"
    
    def ensure_tables_exist(self):
        """Create tables if they don't exist."""
        schema_path = os.path.join(
            os.path.dirname(__file__), 
            "../data/reference_database_schema.sql"
        )
        with open(schema_path, 'r') as f:
            ddl = f.read()
        
        # Execute DDL statements
        for statement in ddl.split(';'):
            statement = statement.strip()
            if statement and not statement.startswith('--'):
                try:
                    self.client.query(statement).result()
                    print(f"Executed: {statement[:50]}...")
                except Exception as e:
                    print(f"Note: {e}")
    
    def add_reference(self, ref: Reference, discovered_in: str = None) -> str:
        """Add a new reference to the database."""
        row = ref.to_bigquery_row()
        row["discovered_in"] = discovered_in
        row["discovered_at"] = datetime.utcnow().isoformat()
        row["cited_in"] = []  # Empty initially
        
        # Check for duplicates
        duplicate_check = f"""
        SELECT reference_id FROM `{self.dataset_ref}.verified_references`
        WHERE (doi = '{ref.doi}' AND doi IS NOT NULL)
           OR (arxiv_id = '{ref.arxiv_id}' AND arxiv_id IS NOT NULL)
           OR (title = '{ref.title.replace("'", "\\'")}' AND year = {ref.year})
        LIMIT 1
        """
        
        try:
            result = self.client.query(duplicate_check).result()
            existing = list(result)
            if existing:
                print(f"Reference already exists: {existing[0].reference_id}")
                return existing[0].reference_id
        except Exception as e:
            print(f"Duplicate check warning: {e}")
        
        # Insert the reference
        table_ref = f"{self.dataset_ref}.verified_references"
        errors = self.client.insert_rows_json(table_ref, [row])
        
        if errors:
            raise Exception(f"Failed to insert reference: {errors}")
        
        print(f"Added reference: {ref.reference_id}")
        return ref.reference_id
    
    def find_reference(self, title: str = None, authors: List[str] = None, 
                       year: int = None, doi: str = None) -> List[Reference]:
        """Search for references by various criteria."""
        conditions = []
        if title:
            conditions.append(f"LOWER(title) LIKE LOWER('%{title}%')")
        if year:
            conditions.append(f"year = {year}")
        if doi:
            conditions.append(f"doi = '{doi}'")
        if authors:
            author_conditions = [f"'{a}' IN UNNEST(authors)" for a in authors]
            conditions.append(f"({' OR '.join(author_conditions)})")
        
        where_clause = " AND ".join(conditions) if conditions else "TRUE"
        
        query = f"""
        SELECT * FROM `{self.dataset_ref}.verified_references`
        WHERE {where_clause}
        ORDER BY verification_status = 'verified' DESC, year DESC
        LIMIT 20
        """
        
        results = self.client.query(query).result()
        refs = []
        for row in results:
            refs.append(Reference(
                reference_id=row.reference_id,
                title=row.title,
                authors=list(row.authors),
                year=row.year,
                venue=row.venue,
                doi=row.doi,
                verification_status=row.verification_status
            ))
        return refs
    
    def record_citation_attempt(self, intended: Reference, drafting_paper: str,
                                surrounding_text: str, resolution: str,
                                matched_id: str = None, confidence: float = 0.0):
        """Record an attempt to cite something (for hallucination tracking)."""
        row = {
            "attempt_id": hashlib.sha256(
                f"{intended.title}{datetime.utcnow().isoformat()}".encode()
            ).hexdigest()[:16],
            "attempted_at": datetime.utcnow().isoformat(),
            "intended_title": intended.title,
            "intended_authors": intended.authors,
            "intended_year": intended.year,
            "intended_venue": intended.venue,
            "drafting_paper": drafting_paper,
            "surrounding_text": surrounding_text[:500],  # Truncate
            "matched_reference_id": matched_id,
            "match_confidence": confidence,
            "resolution": resolution,
            "action_taken": "pending"
        }
        
        table_ref = f"{self.dataset_ref}.citation_attempts"
        errors = self.client.insert_rows_json(table_ref, [row])
        
        if errors:
            print(f"Warning: Failed to log citation attempt: {errors}")
    
    def verify_reference(self, reference_id: str, method: str = "manual",
                         source: str = None):
        """Mark a reference as verified."""
        query = f"""
        UPDATE `{self.dataset_ref}.verified_references`
        SET 
            verification_status = 'verified',
            verified_at = TIMESTAMP('{datetime.utcnow().isoformat()}'),
            verified_by = '{method}',
            verification_source = '{source or ''}',
            last_checked = TIMESTAMP('{datetime.utcnow().isoformat()}')
        WHERE reference_id = '{reference_id}'
        """
        
        self.client.query(query).result()
        print(f"Verified reference: {reference_id}")
    
    def get_unverified_citations(self, limit: int = 20) -> List[Dict]:
        """Get citations that need verification attention."""
        query = f"""
        SELECT * FROM `{self.dataset_ref}.unverified_citations`
        LIMIT {limit}
        """
        
        results = self.client.query(query).result()
        return [dict(row) for row in results]
    
    def generate_bibtex_for_paper(self, paper_id: str) -> str:
        """Generate BibTeX for all references used in a paper."""
        query = f"""
        SELECT bibtex_entry 
        FROM `{self.dataset_ref}.verified_references`,
        UNNEST(cited_in) as citation
        WHERE citation.paper_id = '{paper_id}'
        AND verification_status = 'verified'
        ORDER BY citation.cited_at
        """
        
        results = self.client.query(query).result()
        bibtex_entries = [row.bibtex_entry for row in results if row.bibtex_entry]
        
        return "\n\n".join(bibtex_entries)


# CLI Interface
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Reference Database Manager")
    parser.add_argument("command", choices=[
        "init", "add", "search", "verify", "unverified", "bibtex"
    ])
    parser.add_argument("--title", help="Paper title")
    parser.add_argument("--authors", help="Comma-separated author list")
    parser.add_argument("--year", type=int, help="Publication year")
    parser.add_argument("--doi", help="DOI")
    parser.add_argument("--ref-id", help="Reference ID")
    parser.add_argument("--paper-id", help="Your paper ID for bibtex export")
    
    args = parser.parse_args()
    
    db = ReferenceDatabase()
    
    if args.command == "init":
        db.ensure_tables_exist()
        print("Database initialized!")
    
    elif args.command == "add":
        if not all([args.title, args.authors, args.year]):
            print("Error: --title, --authors, and --year are required")
            exit(1)
        
        ref = Reference(
            reference_id=hashlib.sha256(
                f"{args.title}{args.year}".encode()
            ).hexdigest()[:16],
            title=args.title,
            authors=[a.strip() for a in args.authors.split(",")],
            year=args.year,
            doi=args.doi,
            verification_status="unverified"
        )
        db.add_reference(ref)
    
    elif args.command == "search":
        authors = [a.strip() for a in args.authors.split(",")] if args.authors else None
        results = db.find_reference(
            title=args.title,
            authors=authors,
            year=args.year,
            doi=args.doi
        )
        for r in results:
            status_emoji = "✓" if r.verification_status == "verified" else "?"
            print(f"{status_emoji} [{r.reference_id}] {r.title} ({r.year})")
            print(f"   Authors: {', '.join(r.authors)}")
            print()
    
    elif args.command == "verify":
        if not args.ref_id:
            print("Error: --ref-id is required")
            exit(1)
        db.verify_reference(args.ref_id)
    
    elif args.command == "unverified":
        refs = db.get_unverified_citations()
        print(f"Found {len(refs)} unverified references:")
        for r in refs:
            print(f"? [{r['reference_id']}] {r['title']} ({r['year']})")
    
    elif args.command == "bibtex":
        if not args.paper_id:
            print("Error: --paper-id is required")
            exit(1)
        print(db.generate_bibtex_for_paper(args.paper_id))
