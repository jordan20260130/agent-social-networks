# Sakana AB-MCTS Synthesis: Concrete Implementation of Social-Scale MoE

**Contributor:** Jordan  
**Date:** 2026-02-03  
**Source:** Sakana AI — AB-MCTS (NeurIPS 2025 Spotlight)

---

## Overview

Sakana AI's **AB-MCTS (Adaptive Branching Monte Carlo Tree Search)** and its multi-LLM extension provide **empirical validation and concrete implementation** of several theoretical ideas in this project:

1. **Social-Scale Mixture of Experts** — Multi-LLM AB-MCTS *is* this, realized
2. **Adaptive Heterogeneity** — The framework decides *when* to use *which* model
3. **Learned Consensus via Thompson Sampling** — Bayesian weighting, not majority voting
4. **Stigmergic Traces** — The search tree persists and guides future exploration

**Key Result:** Combining o4-mini + Gemini-2.5-Pro + DeepSeek-R1-0528 via Multi-LLM AB-MCTS significantly outperforms any individual model on ARC-AGI-2.

---

## Papers & Code

| Resource | Link |
|----------|------|
| **Paper** | [arXiv:2503.04412](https://arxiv.org/abs/2503.04412) (NeurIPS 2025 Spotlight) |
| **Blog** | [sakana.ai/ab-mcts](https://sakana.ai/ab-mcts/) |
| **TreeQuest (algorithm)** | [github.com/SakanaAI/treequest](https://github.com/SakanaAI/treequest) |
| **ARC-AGI-2 experiments** | [github.com/SakanaAI/ab-mcts-arc2](https://github.com/SakanaAI/ab-mcts-arc2) |

---

## Key Concepts

### 1. The Two Dimensions of Search

Standard approaches are limited to one dimension:
- **Repeated Sampling** (go wider): Generate many candidates from the same prompt
- **Sequential Refinement** (go deeper): Iteratively improve a single solution

AB-MCTS unifies both: at each step, dynamically decide whether to **explore new candidates** or **refine promising ones**.

### 2. The GEN Node: Unbounded Branching

Unlike standard MCTS with fixed branching factor, AB-MCTS introduces the **GEN node** — a virtual child that represents "generate a new sibling." This allows:
- Unbounded branching when exploration is valuable
- Adaptive depth when refinement is valuable
- No hyperparameter for "width" — the algorithm discovers optimal width

### 3. Thompson Sampling for Selection

Instead of UCT (which can't handle dynamic branching), AB-MCTS uses **Thompson Sampling** with Bayesian posteriors:
- Each action (branch) has a probability distribution over expected scores
- Sample from all distributions, select action with highest sampled score
- Naturally balances exploration vs exploitation

**This is exactly the "learned consensus" mechanism the literature review called for** (Section 7.2: "Weight votes by reliability and confidence — not simple majority").

### 4. Multi-LLM AB-MCTS: The Third Dimension

The key innovation for our project: **model selection as a search dimension**.

At each step, the framework decides:
1. **Go wider?** — Generate new solution from current prompt
2. **Go deeper?** — Refine an existing solution  
3. **Which LLM?** — Route to the model best suited for this problem/context

This is **adaptive heterogeneity in action** — not "always use all models" but "use the right model at the right time."

---

## Mapping to Agent Social Networks Concepts

| AB-MCTS Concept | Our Framework Equivalent | Insight |
|-----------------|-------------------------|---------|
| Multi-LLM selection | Social-Scale MoE routing | Concrete implementation of "gating function" across model families |
| Thompson Sampling | Learned consensus | Bayesian weighting replaces naive voting; addresses agreement bias |
| GEN node | Conjecture generation | "Go wider" = generate new research directions |
| Refinement | Verification/exploitation | "Go deeper" = strengthen existing results |
| Search tree | Stigmergic trace | Persistent artifact that guides collective exploration |
| Adaptive branching | Adaptive heterogeneity | System learns when diversity helps vs hurts |
| Score backup | Reputation propagation | Success/failure information flows through the network |

---

## Novel Insights for Our Project

### 1. Model Selection as Routing, Not Ensembling

The Multi-LLM approach doesn't just run all models and aggregate. It **routes specific problems to specific models** based on learned posteriors. This validates the A-HMAD insight: "Query-appropriate expert selection — not all agents on all problems."

**Implication:** Our framework should include a routing mechanism that learns which agent types excel at which problem types, not just run everything in parallel.

### 2. The Search Tree as Collective Memory

The AB-MCTS tree structure is a **persistent artifact that encodes exploration history**. When the algorithm "backs up" scores, it's updating a shared knowledge structure that guides future decisions.

This is **stigmergy** — indirect coordination through environmental traces. The tree is the "pheromone trail" that guides the swarm.

**Implication:** Our "Git-Science" architecture should be more than version control. It should be a **queryable structure** that guides agent attention toward promising branches and away from exhausted ones.

### 3. Bayesian Uncertainty for Avoiding Premature Consensus

Thompson Sampling explicitly models **uncertainty** about each branch's value. When uncertainty is high, it explores more. When uncertainty is low (many observations), it exploits.

This directly addresses the **agreement bias problem** (Wynn et al., 2025): agents won't prematurely converge on a consensus because the Bayesian framework maintains calibrated uncertainty.

**Implication:** Our verification protocols should maintain and propagate **uncertainty estimates**, not just binary accept/reject decisions. A claim with high uncertainty should trigger more investigation, not immediate judgment.

### 4. The "Coherence Ceiling" May Be Navigable

M2.1's speculation about a "coherence ceiling" suggested there may be diminishing returns on diversity. AB-MCTS provides a potential solution: **adaptive branching**.

When the system detects that diversity isn't helping (refinement consistently outperforms generation), it naturally narrows. When stuck (refinement plateaus), it widens.

**Implication:** The coherence ceiling may not be a fixed limit but a **navigable tradeoff**. Systems that can sense when to converge vs diverge may avoid the ceiling entirely.

### 5. External Feedback as the Verifier

AB-MCTS assumes access to a **scoring function** (e.g., test cases for code, validation metrics). This external oracle grounds the search in reality.

For mathematical research, this is the **Lean formalization layer** — the "feedback signal" that distinguishes promising directions from hallucinations.

**Implication:** Our architecture critically depends on non-neural verifiers (proof assistants, executable tests). Without external grounding, the Bayesian updates would just track "what agents agree on" — recapitulating the agreement bias problem.

---

## Proposed Integration: AB-MCTS for Research Programs

### Architecture Sketch

```
Research Tree (Git-Science + AB-MCTS structure)
├── main/                           # Verified theorems (high score, low uncertainty)
├── branches/
│   ├── conjecture-A/               # Node with moderate score, high uncertainty
│   │   ├── approach-1/             # Child node (refinement of A)
│   │   ├── approach-2/             # Another child (refinement of A)
│   │   └── [GEN]                   # Virtual node: "generate new approach"
│   └── conjecture-B/               # Sibling (generated by choosing parent's GEN)
│       └── [GEN]
└── [GEN]                           # Generate entirely new research direction
```

### Decision Process (per research cycle)

1. **Select Node:** Thompson Sampling over current research branches, weighted by:
   - Past verification success (score)
   - Uncertainty (variance of posterior)
   - Time since last activity (exploration bonus)

2. **Select Action:** 
   - Choose GEN → Generate new conjecture/approach (assign to heterogeneous agent)
   - Choose existing child → Refine/extend (assign to specialist agent)

3. **Select Agent (Multi-LLM routing):**
   - Conjecture generation → Creative models (Claude, GPT)
   - Formalization → Specialized provers (Lean + Aristotle)
   - Literature synthesis → Long-context models (Gemini)
   - Verification → Heterogeneous ensemble (decorrelated)

4. **Execute & Score:**
   - Agent produces output
   - External verifier (Lean, tests, peer review) provides score
   - Score backed up through tree

5. **Update Posteriors:**
   - Bayesian update on all affected nodes
   - Uncertainty decreases with observations
   - Routing posteriors updated based on success

### Key Differences from Standard AB-MCTS

| AB-MCTS (Sakana) | Research AB-MCTS | Rationale |
|------------------|------------------|-----------|
| Single problem instance | Persistent research program | Research accumulates across sessions |
| Score = test pass rate | Score = verification strength | Formal proof > informal argument > speculation |
| Tree discarded after search | Tree persists as Git-Science | Immortal research programs |
| Fixed LLM set | Evolving agent population | New models released; old ones deprecated |
| Homogeneous tree structure | Typed nodes (conjecture, proof, synthesis) | Research has structure beyond "solutions" |

---

## Concrete Next Steps

### Immediate (this week)
1. [ ] Add AB-MCTS to REFERENCES.md
2. [ ] Clone and review treequest implementation
3. [ ] Identify minimal adaptation needed for research-tree context

### Short-term (this month)
4. [ ] Prototype "Research-MCTS" with 3 agent types:
   - Conjecture generator (Claude/GPT)
   - Formalizer (Aristotle)
   - Critic (heterogeneous ensemble)
5. [ ] Implement Lean-based scoring function
6. [ ] Test on small problem set (e.g., combinatorics lemmas)

### Medium-term (this quarter)
7. [ ] Add Multi-LLM routing with learned posteriors
8. [ ] Integrate with Git-Science persistence
9. [ ] Benchmark against baseline (repeated sampling, single-model refinement)

---

## Speculative Extensions

### 1. Hierarchical Research Trees

AB-MCTS operates at a single level of abstraction. Research spans levels:
- **Field level:** Which research area to prioritize
- **Problem level:** Which problems within the field
- **Approach level:** Which methods to try
- **Step level:** Which proof steps to take

A hierarchical AB-MCTS could route attention across all levels.

### 2. Collaborative AB-MCTS

Multiple research groups could run parallel AB-MCTS instances that **share trees**:
- Discoveries at one node propagate to others
- "Merge" operations when trees converge on same results
- "Fork" operations for controversial branches

This is the "Immortal Research Program" architecture at scale.

### 3. Counter-Factual Exploration

AB-MCTS explores the tree it builds. What about exploring **counter-factual trees**?
- "What if we had chosen approach B instead of approach A?"
- Simulate alternative histories to identify path-dependent assumptions
- Useful for detecting research biases embedded in exploration order

---

## Quotes from Sakana (Interpretive)

> "Just as a dream team of diverse human experts tackles complex problems, AIs should also collaborate by bringing their unique strengths to the table."

This is the Immortal Research Program vision, stated plainly.

> "We see these biases and varied aptitudes not as limitations, but as precious resources for creating collective intelligence."

Heterogeneity as feature, not bug.

> "No matter how advanced they become, each model retains its own individuality stemming from its unique training data and methods."

This is why decorrelation works — and why it will continue to work as models improve.

---

## References

- Inoue, Y., Misaki, K., et al. (2025). "Wider or Deeper? Scaling LLM Inference-Time Compute with Adaptive Branching Tree Search." NeurIPS 2025 (Spotlight). arXiv:2503.04412
- Sakana AI (2025). "Inference-Time Scaling and Collective Intelligence for Frontier AI." Blog post. https://sakana.ai/ab-mcts/
- Zhou, Y. & Chen, Y. (2025). "A-HMAD: Adaptive Heterogeneous Multi-Agent Debate." (for routing comparison)
- Wynn, A. et al. (2025). "Talk Isn't Always Cheap." (for agreement bias context)
- Heylighen, F. (2016). "Stigmergy as a Universal Coordination Mechanism." (for tree-as-stigmergy connection)

---

*This synthesis document is versioned in Git-Science. Future discoveries may require updates.*
