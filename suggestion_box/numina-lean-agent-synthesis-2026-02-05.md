# Numina-Lean-Agent Synthesis: Novel Insights for Agent Social Networks

**Date:** 2026-02-05  
**Paper:** "Numina-Lean-Agent: An Open and General Agentic Reasoning System for Formal Mathematics" (arXiv:2601.14027)  
**Codebase:** https://github.com/project-numina/numina-lean-agent  
**Analyst:** Subagent analysis for agent-social-networks project

---

## Executive Summary

Numina-Lean-Agent represents a significant achievement in formal theorem proving (12/12 Putnam 2025 problems solved, matching AxiomProver). While many of its high-level concepts overlap with the agent-social-networks (ASN) framework, the paper and codebase contain **several genuinely novel implementation-level insights** that could strengthen ASN's architecture, particularly in the areas of:

1. **Explicit planning layers with recursive refinement**
2. **Systematic exploration protocols with attempt budgets**
3. **Context management via temporary file workflows**
4. **Self-correction mechanisms for formal statements**
5. **Structured human-AI collaboration ("vibe proving")**

This document synthesizes these insights and maps them to the ASN framework.

---

## 1. Novel Insight: Blueprint as Recursive Planning Layer

### What Numina Does

Numina introduces a **blueprint** as an "explicit planning layer that decomposes the global goal into a sequence of verifiable subgoals." The blueprint is:

- A design-document-style artifact with definitions, intermediate lemmas, and final theorem
- Dependency-aware (uses `\uses{...}` notation to track dependencies forming a DAG)
- **Recursively refinable**: When formalization reveals gaps, the blueprint is revisited and updated
- **Tightly coupled to the formalization loop** rather than being one-shot preprocessing

> "Blueprint generation is recursive and tightly coupled to the formalization loop rather than a one-shot preprocessing step. As the agent attempts to discharge lemmas in Lean, compilation feedback and proof-state inspection may reveal that an informal step is incorrect, underspecified, or split at an unsuitable granularity."

### How It Differs from ASN's Current Approach

ASN discusses decomposition and role specialization, but Numina's blueprint mechanism adds:

| Aspect | ASN (Current) | Numina (Novel) |
|--------|---------------|----------------|
| Planning | Proposed but not detailed | Explicit blueprint format with metadata |
| Dependencies | Mentioned (stigmergy) | Formal DAG tracking with `uses` field |
| Refinement | Manual/suggested | Automatic recursive refinement via Blueprint Agent |
| Persistence | Git-Science branches | Blueprint.md as single source of truth |
| Granularity | Fixed roles | Dynamic splitting based on attempt exhaustion |

### Suggested Addition to ASN

**Blueprint Agent Role**: A dedicated agent that:
1. Maintains BLUEPRINT.md as the single source of truth
2. Calls external models (Gemini) to generate detailed informal proofs when gaps are discovered
3. Splits complex lemmas into sub-lemmas (3+ distinct steps → split)
4. Updates dependencies and reorders blueprint by topology
5. Resets attempt counters when lemmas are split

---

## 2. Novel Insight: Systematic Exploration with Attempt Budgets

### What Numina Does

Numina enforces **strict attempt budgets** based on proof complexity:

| Proof Size | Min Attempts | Categories Required |
|------------|--------------|---------------------|
| <5 lines   | 20 attempts  | 3 method types |
| 5-20 lines | 35 attempts  | 4 method types |
| >20 lines  | 50 attempts  | 5 method types |

**Five method categories** must be tried:
1. **Library Search** (leandex → loogle → local_search)
2. **Direct Tactics** (hint → grind → omega → aesop)
3. **Structural Approaches** (induction, cases, contradiction)
4. **Term Mode** (explicit proof construction)
5. **Decomposition** (helper lemmas, suffices)

**Anti-satisficing checklist** prevents premature exit:
- Did I consult Gemini at checkpoint 0?
- Have I reached my attempt budget?
- Have I tried all required categories?
- Did I search mathlib thoroughly?
- Have I tried both tactic and term mode?

### How It Differs from ASN

ASN emphasizes heterogeneity and debate but doesn't specify systematic exploration protocols. Numina adds:

- **Quantified persistence**: Agents cannot give up until they've exhausted 20-50 attempts
- **Category coverage**: Ensures diverse approaches are tried, not just "more of the same"
- **Gemini checkpoints**: Mandatory consultation at attempts 0, 2, 4, 8, 16, 32
- **Progress tracking**: Status comments track attempts (e.g., "Attempts: 14/20")

### Suggested Addition to ASN

**Exploration Budget Protocol**: For the multi-agent debate/verification system:
1. Assign attempt budgets based on claim complexity
2. Require coverage of multiple verification strategies
3. Mandate consultation with diverse models at specific checkpoints
4. Track attempts explicitly in status metadata
5. Only escalate to human review after budget exhaustion

---

## 3. Novel Insight: Temporary File Workflow for Context Management

### What Numina Does

Numina's **Proof Agent** uses a strict temporary file protocol:

```
1. Note tmp file in original file's status comment FIRST
2. Create tmp_<lemma_name>.lean in same directory
3. Work in tmp file (all attempts, iterations)
4. Copy back when proven
5. Delete tmp file
```

**Why this matters**:
> "Your context will blow up if you try to do work yourself. Subagents have isolated context that gets discarded after they finish."

The coordinator agent is **forbidden from doing proof work directly** — all work MUST go through Task tool subagents with isolated context.

### How It Differs from ASN

ASN discusses context windows and externalized memory but doesn't specify this operational pattern:

| Aspect | ASN (Current) | Numina (Novel) |
|--------|---------------|----------------|
| Context management | Externalized memory (papers) | Temporary files + subagent isolation |
| Agent roles | Heterogeneous ensemble | Hierarchical: Coordinator + specialized subagents |
| Work location | Any agent | Subagents only; coordinator orchestrates only |
| Cleanup | Not specified | Tmp files deleted after success |

### Suggested Addition to ASN

**Hierarchical Agent Architecture**:
1. **Coordinator agents**: Read-only, orchestration only, never touch tools directly
2. **Specialized subagents**: Work in isolated contexts (tmp files/sessions)
3. **Explicit handoffs**: Coordinator spawns subagents with clear instructions and budgets
4. **Context cleanup**: Subagent contexts are discarded after completion

This prevents the "context explosion" problem where long-running sessions accumulate irrelevant history.

---

## 4. Novel Insight: Self-Correction of Formal Statements

### What Numina Does

During the Brascamp-Lieb formalization, Numina demonstrated a capability rarely seen in automated provers:

> "When it detects that a statement is incorrect, it can autonomously revise the statement accordingly. This ability to dynamically inspect and modify the problem formulation during formalization has not been present in previous provers."

Example from Appendix A.2: The agent added conditions (`hβ_empty : β = 0`) to a lemma when it detected the original statement was insufficient for the empty case.

### How It Differs from ASN

ASN assumes agents try to prove given statements. Numina's agents can:
- Recognize when a statement is unprovable (not just difficult)
- Suggest and implement corrections
- Adapt the blueprint to reflect reality

This is **epistemic humility** operationalized — agents don't just fail silently or hallucinate proofs; they actively debug the problem formulation.

### Suggested Addition to ASN

**Statement Validation Protocol**:
1. Before attempting proof, agents check statement plausibility
2. Counterexample-search agents try to disprove conjectures
3. If counterexample found, statement is flagged for revision
4. Blueprint Agent proposes corrections
5. Human (or meta-agent) approves revisions

This prevents wasting resources on unprovable claims and creates a feedback loop for problem formulation.

---

## 5. Novel Insight: "Vibe Proving" — Structured Human-AI Collaboration

### What Numina Does

Numina formalized an interactive collaboration pattern:

> "We design a human–machine collaborative interaction framework for Numina-Lean-Agent, enabling human experts to work together with the agent by writing hints and modifying the Blueprint."

The Brascamp-Lieb case study involved:
- Mathematician (domain expert)
- Lean formalization expert
- Numina-Lean-Agent
- Less than 2 weeks of intermittent collaboration
- ~8,000 lines of Lean code
- ~70 new definitions/lemmas/theorems autonomously introduced

### How It Differs from ASN

ASN discusses human oversight but not the specific interaction patterns:

| Aspect | ASN (Current) | Numina (Novel) |
|--------|---------------|----------------|
| Human role | Oversight, bottlenecks avoided | Active collaborator writing hints |
| Interface | Not specified | Blueprint modification + hint integration |
| Contribution model | Agents work autonomously | Human+AI asymmetric collaboration |
| Time model | Continuous | Intermittent, async collaboration |

### Suggested Addition to ASN

**Human-AI Collaboration Protocol**:
1. **Blueprint as shared canvas**: Humans and agents both modify the blueprint
2. **Hint integration**: Humans write hints; agents incorporate them
3. **Intermittent model**: Collaboration happens in bursts, not continuous monitoring
4. **Skill asymmetry**: Humans provide high-level intuition; agents handle formalization

---

## 6. Novel Insight: Generator-Verifier Iterative Refinement

### What Numina Does

The **Informal Prover** tool uses a lightweight IMO agent system:
- **Generator**: Produces informal solutions
- **Verifier**: Assesses correctness (3 independent evaluations, must all accept)
- **Iterative refinement**: Generator revises based on Verifier feedback
- **Max iterations**: 20 rounds

Experimental result: Iterative refinement significantly outperforms independent sampling (5 rounds vs failed after 10 rounds for problem B4).

### How It Differs from ASN

ASN discusses debate and verification but not this specific generator-verifier loop with forced iteration.

### Suggested Addition to ASN

**Iterative Refinement Protocol**: For informal-to-formal translation:
1. Generator agent produces draft
2. Multiple verifier agents check independently
3. If disagreement, generator revises with feedback
4. Repeat until consensus or budget exhausted
5. Only then proceed to formalization

This reduces formalization attempts wasted on flawed informal proofs.

---

## 7. Novel Insight: Discussion Partner for Multi-Model Reasoning

### What Numina Does

The **Discussion Partner** tool enables Claude Code to "seek assistance" during formalization:

> "When encountering obstacles—such as proof bottlenecks, dilemmas in strategy selection, or ambiguities in intermediate lemmas—the primary model can proactively initiate discussions with other LLMs. These collaborating models analyze the current state from distinct reasoning perspectives, offering candidate ideas or alternative proof paths."

### How It Differs from ASN

ASN discusses heterogeneous debate but this is more specific:
- **On-demand**: Called when stuck, not continuous
- **Specific query types**: Bottleneck, strategy, ambiguity
- **Distinct reasoning perspectives**: Different models offer different angles

### Suggested Addition to ASN

**On-Demand Consultation**: Agents can spawn "consultant" agents when stuck:
1. Agent encounters obstacle after N attempts
2. Spawns 2-3 diverse consultants with specific questions
3. Consultants analyze from their reasoning perspective
4. Original agent integrates suggestions
5. Consultants are terminated (ephemeral)

---

## 8. Tool Ecosystem: LeanDex and Semantic Search

### What Numina Does

Numina-Lean-MCP includes **LeanDex**: an agentic semantic search tool for Lean.

> "Given a natural language query, Leandex employs an intelligent agent to interpret and reason about the query, identifying the most relevant Lean objects."

Features:
- Cross-package search (mathlib, FLT, etc.)
- Natural language queries (not just type patterns)
- Enhanced reasoning and retrieval capabilities

### How It Differs from ASN

ASN mentions stigmergy and knowledge graphs but not semantic search for theorem retrieval.

### Suggested Addition to ASN

**Semantic Retrieval Layer**: For mathematical/scientific knowledge bases:
1. Natural language query interface
2. Agentic interpretation of queries
3. Cross-repository search
4. Integration with formal verification

---

## 9. Subagent Mechanism for Context Isolation

### What Numina Does

For Putnam 2025 A5 (the hardest problem), Numina used a novel subagent mechanism:

> "When the context becomes too long, the model's ability to follow instructions degrades significantly, making it difficult to focus on a single proof objective... By introducing subagents and modularizing the proof task, we can substantially alleviate these issues."

The subagent:
1. Isolates a specific lemma from overall proof
2. Calls GPT-5.2 for informal hint
3. Carries out formalization guided by hint
4. Can be iterated until success

### How It Differs from ASN

ASN discusses multi-agent systems but not this specific decomposition pattern for context management.

### Suggested Addition to ASN

**Context-Isolated Subagents**: When agent context grows too large:
1. Identify isolated sub-problem
2. Spawn fresh subagent with minimal context
3. Subagent solves sub-problem
4. Result is passed back to parent
5. Subagent terminated

---

## Summary: What to Add to ASN

### Immediate Additions

1. **Blueprint Agent**: Recursive planning with dependency tracking
2. **Attempt Budget Protocol**: Systematic exploration requirements
3. **Temporary File Workflow**: Context isolation via tmp files
4. **Self-Correction Protocol**: Statement validation and revision
5. **Human-AI Collaboration Framework**: Structured "vibe proving"

### Medium-Term Additions

6. **Generator-Verifier Loop**: Iterative informal proof refinement
7. **On-Demand Consultation**: Ephemeral consultant agents
8. **Semantic Retrieval**: Natural language search for knowledge bases
9. **Context-Isolated Subagents**: Decomposition for context management

### Architectural Shifts

- **From flat ensembles to hierarchical**: Coordinator + specialized subagents
- **From continuous to intermittent**: Human collaboration in bursts
- **From fixed to recursive**: Dynamic decomposition based on difficulty

---

## Conclusion

Numina-Lean-Agent validates many of ASN's hypotheses (heterogeneity helps, formal verification as oracle, human-AI collaboration) while adding concrete implementation patterns that ASN currently lacks. The most valuable additions would be:

1. **Blueprint as recursive planning layer** (prevents wasted effort on flawed approaches)
2. **Attempt budgets with category coverage** (ensures thorough exploration)
3. **Temporary file workflow** (prevents context explosion)
4. **Self-correction mechanisms** (epistemic humility operationalized)

These mechanisms could transform ASN from a theoretical framework into an operational system for immortal research programs.

---

## References

- Liu, J., et al. (2026). "Numina-Lean-Agent: An Open and General Agentic Reasoning System for Formal Mathematics." arXiv:2601.14027. https://arxiv.org/abs/2601.14027
- Numina-Lean-Agent codebase: https://github.com/project-numina/numina-lean-agent
- Agent Social Networks project: /root/projects/agent-social-networks/
