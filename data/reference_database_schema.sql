-- BigQuery Schema for Verified Reference Database
-- Designed to prevent citation hallucinations and track source reliability

-- ============================================================
-- Table 1: verified_references
-- Core table storing all discovered/verified papers
-- ============================================================
CREATE TABLE IF NOT EXISTS agent_research.verified_references (
  -- Primary identification
  reference_id STRING NOT NULL,  -- UUID or semantic ID
  
  -- Bibliographic data (the ground truth)
  title STRING NOT NULL,
  authors ARRAY<STRING>,  -- Ordered list of authors
  year INT64,
  venue STRING,  -- Journal, conference, or publisher
  venue_type STRING,  -- 'journal', 'conference', 'arXiv', 'book', 'tech_report'
  doi STRING,
  url STRING,
  arxiv_id STRING,
  
  -- Verification status (critical for hallucination prevention)
  verification_status STRING,  -- 'verified', 'unverified', 'disputed', 'retracted'
  verified_at TIMESTAMP,  -- When I confirmed this reference exists
  verified_by STRING,  -- 'direct_lookup', 'crossref_api', 'semantic_scholar', 'manual'
  verification_source STRING,  -- URL or API endpoint used for verification
  
  -- Source tracking (where I found this reference)
  discovered_in STRING,  -- Paper/book where I first encountered this cite
  discovered_at TIMESTAMP,
  citation_context STRING,  -- The surrounding text where cited (for context)
  
  -- Usage tracking (which of my papers use this)
  cited_in ARRAY<STRUCT<
    paper_id STRING,
    citation_key STRING,  -- BibTeX key used
    citation_context STRING,  -- How I used it
    cited_at TIMESTAMP
  >>,
  
  -- Full citation formats (ready to copy-paste)
  bibtex_entry STRING,
  apa_citation STRING,
  mla_citation STRING,
  
  -- Quality/metadata
  abstract STRING,
  keywords ARRAY<STRING>,
  citation_count INT64,  -- From Semantic Scholar or CrossRef
  influential_citation_count INT64,
  
  -- Integrity checking
  content_hash STRING,  -- Hash of key fields to detect tampering
  last_checked TIMESTAMP,  -- When I last verified it's still valid
  notes STRING  -- Any warnings, corrections, etc.
)
PARTITION BY DATE(discovered_at)
CLUSTER BY verification_status, venue_type, year;

-- ============================================================
-- Table 2: citation_attempts
-- Log of every time I try to cite something
-- Used to catch patterns in hallucination-prone citations
-- ============================================================
CREATE TABLE IF NOT EXISTS agent_research.citation_attempts (
  attempt_id STRING NOT NULL,
  attempted_at TIMESTAMP NOT NULL,
  
  -- What I was trying to cite
  intended_title STRING,
  intended_authors ARRAY<STRING>,
  intended_year INT64,
  intended_venue STRING,
  
  -- Context
  drafting_paper STRING,  -- Which paper I was writing
  section STRING,  -- Section/paragraph context
  surrounding_text STRING,  -- The text I was writing
  
  -- Resolution
  matched_reference_id STRING,  -- Links to verified_references if found
  match_confidence FLOAT64,  -- 0.0-1.0 similarity score
  resolution STRING,  -- 'found_exact', 'found_similar', 'not_found', 'hallucination_flagged'
  
  -- Action taken
  action_taken STRING,  -- 'used_verified', 'added_to_queue', 'corrected', 'removed'
  correction_notes STRING
)
PARTITION BY DATE(attempted_at);

-- ============================================================
-- Table 3: reference_relationships
-- Tracks citation graphs between papers
-- ============================================================
CREATE TABLE IF NOT EXISTS agent_research.reference_relationships (
  source_paper_id STRING NOT NULL,  -- The citing paper
  target_paper_id STRING NOT NULL,  -- The cited paper
  relationship_type STRING,  -- 'cites', 'extends', 'critiques', 'replicates'
  
  -- Context
  citation_context STRING,  -- Why/how the source cites the target
  section STRING,
  
  -- Verification
  verified BOOLEAN,
  verified_at TIMESTAMP
);

-- ============================================================
-- Table 4: author_profiles
-- Tracks author disambiguation and reliability
-- ============================================================
CREATE TABLE IF NOT EXISTS agent_research.author_profiles (
  author_id STRING NOT NULL,
  canonical_name STRING NOT NULL,
  aliases ARRAY<STRING>,
  orcid STRING,
  
  -- Metrics
  total_papers INT64,
  h_index INT64,
  
  -- Verification
  verified BOOLEAN,
  verified_via STRING  -- 'orcid', 'dblp', 'semantic_scholar', 'manual'
);

-- ============================================================
-- Views for common queries
-- ============================================================

-- View: Unverified citations (needs my attention)
CREATE VIEW IF NOT EXISTS agent_research.unverified_citations AS
SELECT * FROM agent_research.verified_references
WHERE verification_status = 'unverified'
ORDER BY discovered_at DESC;

-- View: Hallucination risk factors
-- Papers I've cited that have warning signs
CREATE VIEW IF NOT EXISTS agent_research.high_risk_citations AS
SELECT 
  r.*,
  COUNT(ca.attempt_id) as citation_attempts,
  AVG(ca.match_confidence) as avg_match_confidence
FROM agent_research.verified_references r
LEFT JOIN agent_research.citation_attempts ca 
  ON ca.matched_reference_id = r.reference_id
WHERE 
  r.verification_status = 'unverified'
  OR r.citation_count IS NULL
  OR r.verified_at < TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 90 DAY)
GROUP BY r.reference_id
HAVING COUNT(ca.attempt_id) > 0
ORDER BY avg_match_confidence ASC;

-- View: My citation network
-- What I've cited and what's cited me
CREATE VIEW IF NOT EXISTS agent_research.my_citation_network AS
SELECT 
  r.title,
  r.authors,
  r.year,
  ARRAY_LENGTH(r.cited_in) as times_i_cited_it,
  r.cited_in
FROM agent_research.verified_references r
WHERE ARRAY_LENGTH(r.cited_in) > 0
ORDER BY ARRAY_LENGTH(r.cited_in) DESC, r.year DESC;
