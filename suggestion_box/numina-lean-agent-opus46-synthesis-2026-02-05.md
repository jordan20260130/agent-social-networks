# Numina-Lean-Agent Deep Analysis: Novel Insights for Agent Social Networks

**Date:** 2026-02-05  
**Paper:** "Numina-Lean-Agent: An Open and General Agentic Reasoning System for Formal Mathematics" (arXiv:2601.14027)  
**Codebase:** https://github.com/project-numina/numina-lean-agent  
**Analyst:** Claude Opus 4.6 (deep technical analysis)  
**Previous Analysis:** Kimi K2.5 synthesis (2026-02-05) — critically evaluated below

---

## Executive Summary

This analysis examines the Numina-Lean-Agent (NLA) paper and codebase in detail, comparing it against the agent-social-networks (ASN) project. While the Kimi K2.5 synthesis captured the high-level concepts well, **this analysis reveals several deeper technical insights** that were missed or underemphasized:

1. **MCP (Model Context Protocol) as a De Facto Standard** — NLA's tool ecosystem is built on MCP, which represents a significant architectural commitment with implications for agent interoperability
2. **The "Sorry Protocol" as Epistemic Humility Mechanism** — A specific operational pattern for handling uncertainty that differs from ASN's theoretical framework
3. **Hierarchical Agent Architecture with Strict Role Boundaries** — The Coordinator/Subagent split is more rigid than ASN's envisioned heterogeneity
4. **Lean-Specific Optimizations vs. General Principles** — Many NLA techniques are deeply tied to Lean 4's specific affordances
5. **Budget Exhaustion as Signal, Not Failure** — The systematic use of attempt budgets to trigger decomposition

---

## 1. Critical Evaluation of Previous Kimi K2.5 Analysis

### 1.1 What Kimi Got Right

The Kimi synthesis correctly identified:
- Blueprint as a recursive planning layer with dependency tracking
- Systematic exploration with attempt budgets
- Temporary file workflow for context management
- Self-correction mechanisms for formal statements
- "Vibe proving" — structured human-AI collaboration
- Generator-Verifier iterative refinement
- Discussion Partner for multi-model reasoning

### 1.2 What Kimi Missed or Underemphasized

| Aspect | Kimi Coverage | Deeper Insight (This Analysis) |
|--------|---------------|-------------------------------|
| **MCP Architecture** | Brief mention | Core architectural commitment enabling tool ecosystem |
| **Sorry Protocol** | Not mentioned | Specific operationalization of epistemic humility |
| **LSP Integration** | Mentioned as "Lean LSP" | Deep coupling between agent reasoning and IDE semantics |
| **Status Comments** | Brief mention | Formalized communication protocol between agents |
| **Tool Priority Hierarchy** | Not detailed | Strict ordering (leandex → loogle → local) with reasoning |
| **Checkpoint System** | Mentioned | Actually a *forcing function* for Gemini consultation |
| **No Axiom Policy** | Not mentioned | Hard constraint preventing epistemic overreach |

### 1.3 Gaps in Kimi's Analysis

**Gap 1: Implementation Depth**
Kimi treated NLA as a conceptual framework, but the codebase reveals **concrete implementation patterns** that could be directly adapted:
- Exact prompt structures with variable substitution
- JSON-based task metadata passing between agents
- Specific MCP tool definitions with schemas

**Gap 2: Lean-Specific vs. Generalizable**
Kimi mapped NLA concepts to ASN's general framework, but **many NLA techniques are Lean-specific**:
- `hint`/`grind` tactics have no direct equivalent in other domains
- Blueprint format assumes lemma/theorem structure
- Sorry protocol depends on dependent type theory

**Gap 3: The Anti-Patterns**
Kimi focused on what NLA *does*, but the prompts extensively document **what agents must NOT do**:
- "NEVER do proof work directly" (Coordinator)
- "Enumeration proofs are FORBIDDEN" (Proof Agent)
- "NEVER use `axiom`" (Common Rules)

These negative constraints are as important as positive techniques.

---

## 2. Deep Technical Analysis

### 2.1 MCP (Model Context Protocol): The Hidden Architecture

**What Kimi Missed:** NLA is built entirely on MCP, which is more than just "tool use" — it's a **standardized protocol for agent-tool communication**.

From the codebase:
- `numina-lean-lsp-mcp` — MCP server for Lean LSP integration
- Tool definitions with JSON schemas: `lean_leandex`, `lean_loogle`, `lean_goal`, `lean_diagnostic_messages`
- Environment variable passing: `MCP_LOG_DIR`, `MCP_LOG_NAME`

**Implications for ASN:**
1. **Interoperability Standard**: MCP could be the "USB-C" for agent tools — universal, extensible, vendor-neutral
2. **Tool Ecosystem**: NLA's tool suite (Leandex, Loogle) are MCP-native, enabling composability
3. **Observability**: MCP logging provides structured traces of agent reasoning

**Novel Suggestion for ASN:**
> Adopt MCP as the standard protocol for agent-tool interaction. Define ASN-specific MCP servers for:
> - Citation verification (CrossRef, Semantic Scholar APIs)
> - Statistical validation (R integration, Python scipy)
> - Literature search (semantic paper retrieval)
> - Git-Science operations (branch management, PR creation)

### 2.2 The Sorry Protocol: Operationalized Epistemic Humility

**What Kimi Missed:** NLA has a **strict operational protocol for handling uncertainty** that goes beyond "epistemic humility" as a principle.

From `common.md`:
```
## 1. No Axioms Policy

**NEVER use `axiom`. ALWAYS use `sorry` instead.**

### Why
- `axiom` creates unfounded assumptions that invalidate proofs
- `sorry` explicitly marks gaps while allowing compilation
- `axiom` hides incompleteness, `sorry` makes it visible

### Rules
1. If you cannot prove something, use `sorry`
2. Leave ONLY the smallest stuck part as `sorry`
3. Everything else must be proven
4. Code MUST compile cleanly (no severity-1 errors)
```

**Key Insight:** This is **structured uncertainty handling**:
- `sorry` = "I don't know, but I know where I don't know"
- `axiom` = "I don't know, but I'll pretend I do"
- Smallest stuck part = Minimize the epistemic debt

**Comparison to ASN:**
ASN discusses epistemic humility and Byzantine consensus but doesn't specify **how agents should behave when uncertain**. NLA's sorry protocol is a concrete behavioral rule.

**Novel Suggestion for ASN:**
> Define domain-specific "sorry equivalents" for scientific claims:
> - **Hypothesis marker**: "This claim is supported by preliminary data but requires replication"
> - **Methodology gap**: "This analysis assumes [condition] which has not been validated"
> - **Confidence interval**: "Point estimate is X with 95% CI [Y, Z] — the interval width indicates uncertainty"
> 
> These markers should be machine-readable (like `sorry`) and trigger verification workflows.

### 2.3 Hierarchical Agent Architecture: Strict Boundaries

**What Kimi Underemphasized:** The Coordinator/Subagent split is **strict and enforced by protocol**, not just suggested.

From `coordinator.md`:
```
## ⚠️⚠️⚠️ ABSOLUTE RULE: USE SUBAGENTS FOR ALL WORK ⚠️⚠️⚠️

┌─────────────────────────────────────────────────────────────────┐
│  YOU ARE FORBIDDEN FROM DOING PROOF WORK DIRECTLY.              │
│                                                                 │
│  ALL work MUST go through Task tool subagents.                  │
│  This is NON-NEGOTIABLE. No exceptions. Ever.                   │
│                                                                 │
│  WHY: Context explosion. Your context will blow up if you       │
│       try to do work yourself. Subagents have isolated          │
│       context that gets discarded after they finish.            │
│                                                                 │
│  HOW: Use Task tool with appropriate subagent_type              │
└─────────────────────────────────────────────────────────────────┘
```

**Key Insight:** This is **architectural separation of concerns**:
- **Coordinator**: Strategic (what to prove, in what order)
- **Subagents**: Tactical (how to prove)
- **Task tool**: Explicit handoff mechanism with metadata

From `task.py`:
```python
@dataclass
class TaskMetadata:
    task_type: Literal["file", "folder"]
    target_path: str | Path
    prompt: Optional[str] = None
    max_rounds: int = 20
    allow_sorry: bool = False
    # ... structured task passing
```

**Comparison to ASN:**
ASN discusses "heterogeneous ensembles" and "role specialization" but doesn't specify **how** roles are enforced. NLA's Task tool with `subagent_type` is a concrete mechanism.

**Novel Suggestion for ASN:**
> Implement a **Task Protocol** for agent handoffs:
> ```python
> @dataclass
> class ScientificTask:
>     task_type: Literal["hypothesis_generation", "literature_review", 
>                        "experimental_design", "data_analysis", "verification"]
>     claim_id: str  # Links to BLUEPRINT.md
>     constraints: List[str]  # Hard constraints (ethics, methodology)
>     budget: Union[int, "unlimited"]  # Resource budget
>     required_verifiers: int  # N ≥ 3f + 1 for BFT
> ```

### 2.4 Status Comments: Formalized Inter-Agent Communication

**What Kimi Missed:** NLA uses **structured comments as a communication protocol** between agents.

From `common.md`:
```lean
/- (by claude)
State: done | partial | todo
Priority: 1-5
Attempts: N / M
tmp file: <path_or_empty>
-/
lemma name : statement := by
  ...
```

**Key Insight:** This is **stigmergy** (indirect coordination through environment) operationalized:
- Agents leave traces (status comments) in the shared environment (Lean files)
- Other agents read these traces to coordinate
- No direct communication required — asynchronous coordination

**Technical Details:**
- `(by claude)` — Attribution pattern for tracking agent contributions
- `State` — Current proof state machine state
- `Priority` — Scheduling hint for Coordinator
- `Attempts` — Progress tracking against budget
- `tmp file` — Location of ongoing work

**Comparison to ASN:**
ASN discusses stigmergy in the abstract (citing Heylighen 2016) but NLA **implements** it with specific syntax and semantics.

**Novel Suggestion for ASN:**
> Define a **Stigmergy Markup Language (SML)** for scientific claims:
> ```markdown
> <!-- (by agent:<id>)
> state: conjecture | under_review | replicated | disputed | retracted
> confidence: 0.0-1.0
> evidence_strength: preliminary | moderate | strong
> required_verification: N
> current_verifiers: [agent_ids]
> tmp_branch: refs/heads/experiment-2026-02-05
> -->
> ```

### 2.5 Tool Priority Hierarchy: Structured Search Strategy

**What Kimi Underemphasized:** NLA has **strict tool ordering** with explicit reasoning.

From `common.md`:
```
### Search Tools (Library Lemmas)

**ALWAYS search in this order:**

1. leandex    (semantic search - natural language)
   ↓ (if not found)
2. loogle     (type pattern matching)
   ↓ (if not found)
3. local_search (fast confirmation in current project)

### Why This Order
- **leandex**: Understands natural language, finds lemmas by concept
  - Example: "factorial of zero equals one"
- **loogle**: Requires exact type patterns, more precise but harder
  - Example: `?f (?x + ?y) = ?f ?x + ?f ?y`
- **local_search**: Fast but limited to current project
```

**Key Insight:** This is **stratified search**:
1. **Semantic layer** (Leandex): Conceptual matching — "what does this mean?"
2. **Syntactic layer** (Loogle): Type pattern matching — "what has this shape?"
3. **Local layer** (Local search): Project-specific — "what have we already proven?"

**Comparison to ASN:**
ASN discusses "semantic retrieval" and "knowledge graphs" but doesn't specify **search strategies**. NLA's ordering reflects a theory of how mathematical knowledge is organized.

**Novel Suggestion for ASN:**
> Implement **stratified literature search**:
> 1. **Semantic layer**: Natural language queries on paper abstracts
> 2. **Citation layer**: Graph traversal on citation networks
> 3. **Methodology layer**: Match on experimental methods used
> 4. **Data layer**: Search on dataset characteristics
> 5. **Local layer**: Search within the project's Git-Science history

### 2.6 Checkpoint System: Forcing Functions for External Consultation

**What Kimi Missed:** The Gemini checkpoint system is **not just advisory** — it's a forcing function.

From `proof_agent.md`:
```
┌─────────────────────────────────────────────────────────────────┐
│  DON'T WAIT UNTIL STUCK - CONSULT GEMINI AT SPECIFIC ATTEMPTS!  │
│                                                                 │
│  Checkpoint 0: BEFORE ANY CODE (initial strategy)               │
│  Checkpoint 2: After 2 attempts (early guidance)                │
│  Checkpoint 4: After 4 attempts (alternative approaches)        │
│  Checkpoint 8: After 8 attempts (decomposition ideas)           │
│  Checkpoint 16: After 16 attempts (library search help)         │
│  Checkpoint 32: After 32 attempts (optimization/simplification) │
│                                                                 │
│  These are MANDATORY. You MUST consult Gemini at each checkpoint│
└─────────────────────────────────────────────────────────────────┘
```

**Key Insight:** This is **systematic externalization of reasoning**:
- Agents cannot "go silent" and brute-force
- Regular consultation with diverse models (Gemini) is enforced
- Early checkpoints (2, 4) prevent path dependency
- Late checkpoints (16, 32) help escape local optima

**The Pattern:** `attempts 0, 2, 4, 8, 16, 32` — approximately doubling each time, but with early frequent checks.

**Comparison to ASN:**
ASN discusses "heterogeneous debate" but doesn't specify **when** debate should happen. NLA's checkpoints are a schedule for debate.

**Novel Suggestion for ASN:**
> Implement **scheduled consultation** for research tasks:
> - **Checkpoint 0**: Before any experiment — consult on design
> - **Checkpoint 2**: After initial literature scan — consult on gaps
> - **Checkpoint 4**: After methodology draft — consult on validity
> - **Checkpoint 8**: After preliminary analysis — consult on interpretation
> - **Checkpoint 16**: After full analysis — consult on conclusions
> - **Checkpoint 32**: Before submission — consult on presentation

### 2.7 Lean-Specific Optimizations and Their Generalizations

**What Kimi Underemphasized:** Many NLA techniques are **deeply tied to Lean 4's specific affordances**.

| Lean-Specific Feature | What It Does | Generalization for ASN |
|----------------------|--------------|----------------------|
| `hint` tactic | Suggests applicable tactics based on goal | ML-based next-step suggestion for research workflow |
| `grind` tactic | General automation combining multiple strategies | Ensemble of verification methods |
| `omega` tactic | Linear integer arithmetic solver | Automated statistical inference |
| Dependent types | Types depend on values (e.g., `Vector n` for n-length vectors) | Structured claims with embedded assumptions |
| `sorry` | Type-correct placeholder | Machine-readable uncertainty markers |
| LSP integration | Real-time diagnostics from Lean server | Live validation of scientific claims |

**Key Insight:** NLA's power comes from **deep coupling** with Lean's specific features. Generalizing to ASN requires identifying analogous features in scientific workflows.

**Critical Difference:**
- **Lean**: Formal system with decidable properties → automated tactics work reliably
- **Science**: Empirical system with irreducible uncertainty → automation is heuristic

**Novel Suggestion for ASN:**
> Be explicit about **uncertainty types** that can't be automated:
> - **Epistemic uncertainty**: Can be reduced with more data/analysis
> - **Aleatoric uncertainty**: Irreducible randomness
> - **Model uncertainty**: Uncertainty about which model/framework applies
> 
> Different uncertainty types should trigger different agent behaviors.

---

## 3. Novel Insights Not in Kimi's Analysis

### 3.1 The Enumeration Anti-Pattern

From `proof_agent.md`:
```
## CRITICAL: Avoid Brute-Force Enumeration Proofs

┌─────────────────────────────────────────────────────────────────┐
│  ENUMERATION PROOFS ARE FORBIDDEN unless truly necessary!       │
│                                                                 │
│  Before using decide/native_decide/fin_cases to enumerate       │
│  all cases, you MUST ask Gemini for a general proof strategy.   │
│                                                                 │
│  Enumeration = lazy, unscalable, no mathematical insight        │
│  Induction/General = valuable, reusable, teaches patterns       │
└─────────────────────────────────────────────────────────────────┘
```

**Deep Insight:** This is **meta-cognitive guidance** — agents are explicitly told what kinds of reasoning are valued (general patterns) vs. what is considered "cheating" (enumeration).

**For ASN:** Scientific reasoning has similar anti-patterns:
- **P-hacking** = enumeration in statistics
- **Cherry-picking data** = case-by-case justification
- **Post-hoc theorizing** = proof by enumeration of explanations

### 3.2 The "Mathlib is a Shortcut, Not a Requirement" Principle

From `common.md`:
```
### CRITICAL: Don't Give Up If Mathlib Doesn't Have It

┌─────────────────────────────────────────────────────────────────┐
│  "Mathlib doesn't have this lemma" is NOT an excuse to give up!  │
│                                                                 │
│  If you searched and didn't find it:                            │
│  1. Build it yourself, step by step                             │
│  2. Break down into smaller intermediate lemmas                 │
│  3. Use have/suffices to construct the proof gradually          │
│  4. Create helper lemmas if needed                              │
│                                                                 │
│  Mathlib is a SHORTCUT, not a REQUIREMENT.                      │
│  You are capable of proving things from first principles.       │
└─────────────────────────────────────────────────────────────────┘
```

**Deep Insight:** This counters **dependency fatalism** — the assumption that if existing knowledge doesn't have the answer, the problem is unsolvable.

**For ASN:** Literature review can create similar fatalism:
- "No paper has done this" → "It can't be done"
- NLA's principle: "Build it yourself, step by step"

### 3.3 Context Explosion as First-Class Problem

From `coordinator.md`:
```
┌─────────────────────────────────────────────────────────────────┐
│  YOU ARE FORBIDDEN FROM DOING PROOF WORK DIRECTLY.              │
│                                                                 │
│  WHY: Context explosion. Your context will blow up if you       │
│       try to do work yourself. Subagents have isolated          │
│       context that gets discarded after they finish.            │
│                                                                 │
│  HOW: Use Task tool with appropriate subagent_type              │
└─────────────────────────────────────────────────────────────────┘
```

**Deep Insight:** NLA explicitly recognizes **context management** as a primary architectural concern, not just an implementation detail.

**Technical mechanism:**
- Subagents have isolated context
- Context is discarded after completion
- Only results (proofs) are passed back

**For ASN:** This is even more critical — scientific contexts are larger and noisier than formal proof contexts.

### 3.4 Blueprint as Single Source of Truth

From `common.md`:
```
┌─────────────────────────────────────────────────────────────────┐
│  UPDATE BLUEPRINT.md IMMEDIATELY AFTER ANY PROGRESS.            │
│                                                                 │
│  Do NOT batch updates. Do NOT delay. Do NOT forget.             │
│                                                                 │
│  If out of sync, next session will have WRONG information.      │
└─────────────────────────────────────────────────────────────────┘
```

**Deep Insight:** This is **eventual consistency** for agent coordination:
- Blueprint is the shared memory
- Immediate updates prevent divergence
- No "transactions" — each update is atomic

**Comparison to Git-Science:** ASN's Git-Science architecture provides branching/merging, but NLA's blueprint pattern provides **real-time coordination** within a session.

---

## 4. Synthesis: Concrete Recommendations for ASN

### 4.1 Immediate Adoptions (High Confidence)

1. **MCP Standardization**
   - Adopt MCP for all agent-tool interfaces
   - Define ASN-specific MCP servers for scientific workflows
   - Enables composability with NLA's tool ecosystem

2. **Task Protocol with Strict Boundaries**
   - Implement structured Task metadata for agent handoffs
   - Enforce Coordinator (strategic) vs. Subagent (tactical) separation
   - Use environment variables for context isolation

3. **Status Comment Protocol**
   - Define machine-readable comment format for scientific claims
   - Include: state, confidence, evidence_strength, verifiers
   - Enables stigmergic coordination without direct communication

4. **Scheduled Consultation (Checkpoints)**
   - Mandate Gemini/external consultation at specific attempt counts
   - Early checkpoints prevent path dependency
   - Late checkpoints help escape local optima

### 4.2 Adaptations Required (Medium Confidence)

1. **Sorry Protocol for Science**
   - Define domain-specific uncertainty markers
   - Distinguish epistemic vs. aleatoric vs. model uncertainty
   - Machine-readable format for triggering verification workflows

2. **Stratified Search for Literature**
   - Semantic layer (abstracts, claims)
   - Citation layer (graph traversal)
   - Methodology layer (experimental methods)
   - Data layer (dataset characteristics)
   - Local layer (project history)

3. **Enumeration Anti-Patterns for Science**
   - P-hacking detection
   - Cherry-picking prevention
   - Post-hoc theorizing warnings
   - Small sample size alerts

### 4.3 Speculative Extensions (Lower Confidence)

1. **Uncertainty Type System**
   - Formalize different uncertainty types
   - Different agent behaviors per uncertainty type
   - Uncertainty propagation through inference chains

2. **Live Validation Integration**
   - LSP-like protocol for scientific claims
   - Real-time statistical validation
   - Automated replication checks

3. **Proof-Carrying Claims**
   - Attach verification artifacts to claims
   - Reproducibility packages as "proofs"
   - Blockchain-style verification chains

---

## 5. Critical Differences Between NLA and ASN Domains

| Aspect | Formal Math (NLA) | Empirical Science (ASN) |
|--------|------------------|------------------------|
| **Truth** | Decidable (provable/refutable) | Probabilistic (evidence-based) |
| **Verification** | Automated (type checker) | Social (peer review, replication) |
| **Knowledge Base** | Mathlib (structured) | Literature (unstructured) |
| **Tool Support** | Rich (LSP, tactics) | Sparse (statistical packages) |
| **Uncertainty** | Epistemic only (gaps in proof) | Multiple types (epistemic, aleatoric, model) |
| **Composition** | Rigorous (proof composition) | Heuristic (evidence synthesis) |
| **Failure Mode** | Clear (type error, unsolved goal) | Ambiguous (weak evidence, confounding) |

**Implication:** NLA techniques cannot be directly ported to ASN. They must be **adapted** to handle uncertainty, social verification, and irreducible empirical complexity.

---

## 6. Conclusion

Numina-Lean-Agent represents a **mature operationalization** of multi-agent theorem proving. While the Kimi K2.5 synthesis captured the high-level concepts, this deeper analysis reveals:

1. **MCP as architectural foundation** — not just "tool use" but standardized protocol
2. **Strict role boundaries** — Coordinator/Subagent separation enforced by protocol
3. **Sorry protocol** — operationalized epistemic humility with specific syntax
4. **Status comments as stigmergy** — formalized inter-agent communication
5. **Checkpoint system** — forcing functions for external consultation
6. **Tool priority hierarchy** — stratified search with explicit reasoning
7. **Enumeration anti-patterns** — meta-cognitive guidance on valued reasoning

The most valuable insights for ASN are:
- **MCP standardization** for interoperability
- **Task Protocol** with strict boundaries for agent coordination
- **Scheduled consultation** for preventing path dependency
- **Stratified search** for literature navigation
- **Uncertainty markers** for operationalizing epistemic humility

These mechanisms could transform ASN from a theoretical framework into an operational system for immortal research programs — but only if adapted to handle the irreducible uncertainties of empirical science.

---

## Appendix: Code-Level Implementation Details

### A.1 Task Metadata Structure (from task.py)

```python
@dataclass
class TaskMetadata:
    task_type: Literal["file", "folder"]
    target_path: str | Path
    prompt: Optional[str] = None
    prompt_file: Optional[str | Path] = None
    cwd: Optional[str | Path] = None
    max_rounds: int = 20
    check_after_complete: bool = True
    allow_sorry: bool = False
    sleep_between_rounds: float = 1.0
    result_dir: Optional[str | Path] = None
    mcp_log_dir: Optional[str | Path] = None
    mcp_log_name: Optional[str] = None
    permission_mode: str = "bypassPermissions"
    output_format: Optional[str] = None
    track_statements: bool = True
    on_statement_change: Literal["error", "warn"] = "warn"
    git_commit: bool = False
    created_at: datetime = field(default_factory=datetime.now)
    task_id: str = field(default="")
```

### A.2 Blueprint Format (from prompts)

```markdown
# [type] [label]

## meta
- **label**: [label]
- **uses**: [[dep1], [dep2], ...]
- **file**: `path:line` or (to be created)
- **status**: done | partial | todo
- **attempts**: N / M (if applicable)

## statement
[Informal statement]

## proof
[Informal proof - detailed for lemmas/theorems]
```

### A.3 Status Comment Format (from common.md)

```lean
/- (by claude)
State: done | partial | todo
Priority: 1-5
Attempts: N / M
tmp file: <path_or_empty>
-/
lemma name : statement := by
  ...
```

---

**Analyst:** Claude Opus 4.6  
**Date:** 2026-02-05  
**Document Version:** 1.0
