# Sakana AI Full Synthesis: A Research Program for Immortal Research Programs

**Contributor:** Jordan  
**Date:** 2026-02-03  
**Sources:** Sakana AI publications (2024-2026)

---

## Executive Summary

Sakana AI has developed a coherent research program around **open-ended search with foundation models as mutation operators**. Their work across multiple projects provides:

1. **Empirical validation** of key Agent Social Networks hypotheses
2. **Concrete implementations** we can adapt
3. **Novel mechanisms** not yet in our framework
4. **A unified architecture** for scaling collective intelligence

This document synthesizes six major Sakana projects into actionable insights for Immortal Research Programs.

---

## Table of Contents

1. [AB-MCTS: Social-Scale MoE Realized](#1-ab-mcts-social-scale-moe-realized)
2. [Darwin Gödel Machine: Self-Improving Agent Populations](#2-darwin-gödel-machine-self-improving-agent-populations)
3. [ShinkaEvolve: Sample-Efficient Program Evolution](#3-shinkaevolve-sample-efficient-program-evolution)
4. [ASAL: Open-Ended Novelty Discovery](#4-asal-open-ended-novelty-discovery)
5. [Evolutionary Model Merge: Synthesizing Specialists](#5-evolutionary-model-merge-synthesizing-specialists)
6. [AI Scientist v2: End-to-End Automated Discovery](#6-ai-scientist-v2-end-to-end-automated-discovery)
7. [Unified Framework: The Sakana Stack](#7-unified-framework-the-sakana-stack)
8. [Implementation Roadmap](#8-implementation-roadmap)
9. [References](#9-references)

---

## 1. AB-MCTS: Social-Scale MoE Realized

*See also: [`sakana-ab-mcts-synthesis-2026-02-03.md`](sakana-ab-mcts-synthesis-2026-02-03.md) for detailed analysis.*

### Core Innovation

**Adaptive Branching Monte Carlo Tree Search** unifies two dimensions of inference-time compute:
- **Go wider:** Generate more candidates (exploration)
- **Go deeper:** Refine existing candidates (exploitation)

The key insight: let the algorithm **learn** when to do each, rather than fixing hyperparameters.

### Multi-LLM Extension

Route problems to different models based on learned posteriors via Thompson Sampling:
- o4-mini + Gemini-2.5-Pro + DeepSeek-R1-0528 significantly outperforms any individual model
- This is **Social-Scale MoE** with concrete implementation

### Key Results

| Benchmark | Single Best Model | Multi-LLM AB-MCTS | Improvement |
|-----------|------------------|-------------------|-------------|
| ARC-AGI-2 | ~35% | ~52% | +17% absolute |

### Translation to Our Framework

| AB-MCTS | Agent Social Networks |
|---------|----------------------|
| GEN node (generate sibling) | Conjecture generation |
| Refinement | Proof strengthening |
| Thompson Sampling | Learned consensus (not voting) |
| Search tree | Stigmergic memory |
| Multi-LLM routing | Adaptive heterogeneity |

### Resources

- **Paper:** [arXiv:2503.04412](https://arxiv.org/abs/2503.04412) (NeurIPS 2025 Spotlight)
- **Code:** [github.com/SakanaAI/treequest](https://github.com/SakanaAI/treequest)
- **ARC experiments:** [github.com/SakanaAI/ab-mcts-arc2](https://github.com/SakanaAI/ab-mcts-arc2)

---

## 2. Darwin Gödel Machine: Self-Improving Agent Populations

### Core Innovation

Agents that **rewrite their own code** to improve performance, using open-ended evolutionary search to maintain an **archive of diverse agent variants**.

Named after Jürgen Schmidhuber's theoretical Gödel Machine (1990s), which proposed self-modification with mathematical proofs of improvement. DGM replaces "provable improvement" with "empirical improvement via evolution."

### Key Mechanisms

1. **Self-Referential Modification:** Agent reads and modifies its own Python codebase
2. **Archive-Based Evolution:** Maintain growing library of agent variants (not just best-so-far)
3. **Lineage Preservation:** Less-performant ancestors can enable breakthrough descendants
4. **Open-Ended Exploration:** Multiple evolutionary paths explored in parallel

### Key Results

| Benchmark | Initial | After DGM Evolution | Improvement |
|-----------|---------|---------------------|-------------|
| SWE-bench | 20.0% | 50.0% | +30% absolute |
| Polyglot | 14.2% | 30.7% | +16.5% absolute |

### Critical Finding: Cross-Model Transfer

Improvements discovered with Claude 3.5 Sonnet **transferred** to:
- o3-mini (different architecture)
- Claude 3.7 Sonnet (different version)
- Tasks in different programming languages

**Implication:** Good scaffolding/architecture is model-agnostic. The "Curry-Howard Bridge" hypothesis gains support.

### Translation to Our Framework

| DGM | Agent Social Networks |
|-----|----------------------|
| Archive of agent variants | Evolving agent population (EPD from M2.1 synthesis) |
| Self-modification | Agents improve collaboration protocols, not just task performance |
| Lineage preservation | Negative results as stepping stones |
| Cross-model transfer | Architecture improvements propagate across heterogeneous agents |

### Novel Mechanism: Agent Evolution Layer

```
┌─────────────────────────────────────────────────────────────────┐
│                    LAYER: AGENT EVOLUTION                       │
│  - Archive of agent configurations (prompts, tools, protocols)  │
│  - Evolve configurations that improve collective performance    │
│  - Preserve "ancestor" configurations as stepping stones        │
│  - Transfer discoveries across model families                   │
│  - Mutation operators: prompt modification, tool addition,      │
│    workflow restructuring, role redefinition                    │
└─────────────────────────────────────────────────────────────────┘
```

### Resources

- **Paper:** [arXiv:2505.22954](https://arxiv.org/abs/2505.22954)
- **Blog:** [sakana.ai/dgm](https://sakana.ai/dgm/)
- **Code:** [github.com/jennyzzt/dgm](https://github.com/jennyzzt/dgm)

---

## 3. ShinkaEvolve: Sample-Efficient Program Evolution

### Core Innovation

Evolutionary code optimization achieving **state-of-the-art with 150 samples** instead of thousands (AlphaEvolve requires 10,000+).

"Shinka" (進化) = Japanese for "evolution"

### Key Mechanisms

1. **Novelty-Based Rejection Sampling**
   - Compute program text embedding similarities
   - Use LLM-as-novelty-judge to assess creativity
   - Reject minor variations before expensive evaluation

2. **Bandit-Based LLM Prioritization**
   - Dynamically select best LLM from ensemble for current evolutionary stage
   - Adapts as search progresses (different models excel at different phases)

3. **Stepping-Stone Sampling**
   - Balance exploitation (branch from best) with exploration (branch from diverse ancestors)
   - Maintains population diversity

### Key Results

| Task | AlphaEvolve | ShinkaEvolve | Sample Efficiency |
|------|-------------|--------------|-------------------|
| Circle Packing (26 circles) | ~10,000 samples | **150 samples** | **66x more efficient** |
| AIME Math Scaffolds | N/A | 75 generations | SOTA performance |
| AtCoder (ALE-Bench) | baseline | +2.3% average | Generalized improvements |

### Critical Finding: Discovered Scaffold Generalizes

The AIME agent scaffold discovered by ShinkaEvolve:
- Transfers to unseen problems from different years
- Transfers to different underlying LLMs
- Uses sophisticated multi-agent architecture (diverse personas → peer review → synthesis)

### Translation to Our Framework

| ShinkaEvolve | Agent Social Networks |
|--------------|----------------------|
| Novelty rejection sampling | Don't verify semantically-redundant claims |
| Bandit LLM selection | Adaptive model routing by task phase |
| Stepping-stone archive | Preserved research branches as exploration basis |
| Evolved scaffolds | Discovered collaboration patterns |

### Novel Mechanism: Novelty-Weighted Verification

Before routing a claim to expensive Byzantine verification:

```python
def should_verify(claim, knowledge_base, threshold=0.7):
    # Embedding-based novelty check
    embedding = embed(claim)
    max_similarity = max([
        cosine_similarity(embedding, embed(existing))
        for existing in knowledge_base
    ])
    
    if max_similarity > threshold:
        # Probably redundant — skip or cheap-verify
        return False
    
    # LLM novelty judgment for borderline cases
    if max_similarity > threshold - 0.1:
        return llm_judge_novelty(claim, knowledge_base)
    
    return True  # Genuinely novel — full verification
```

### Resources

- **Paper:** [arXiv:2509.19349](https://arxiv.org/abs/2509.19349)
- **Blog:** [sakana.ai/shinka-evolve](https://sakana.ai/shinka-evolve/)
- **Code:** [github.com/SakanaAI/ShinkaEvolve](https://github.com/SakanaAI/ShinkaEvolve)

---

## 4. ASAL: Open-Ended Novelty Discovery

### Core Innovation

**Automated Search for Artificial Life** uses vision-language foundation models to discover simulations that exhibit target behaviors or **generate endless novelty**.

### Three Search Modes

| Mode | Objective | Research Translation |
|------|-----------|---------------------|
| **Supervised Target** | Find simulation matching text description | "Find proofs matching this conjecture" |
| **Open-Endedness** | Find simulation with high historical novelty | "Find research directions that keep generating discoveries" |
| **Illumination** | Map space of diverse simulations | "Map the landscape of possible approaches" |

### Key Insight: Historical Novelty as Health Metric

Open-ended systems are measured by **how different the current state is from all past states**:

```python
def historical_novelty(current_state, archive):
    """How novel is current_state relative to everything we've seen?"""
    return min([
        distance(current_state, past_state)
        for past_state in archive
    ])

def open_endedness_score(trajectory):
    """Average historical novelty across a run"""
    archive = []
    scores = []
    for state in trajectory:
        scores.append(historical_novelty(state, archive))
        archive.append(state)
    return mean(scores)
```

### Translation to Our Framework

**Research Program Vitality Score:**

```python
def vitality(research_tree, time_horizon):
    """Is this research program still generating novel discoveries?"""
    recent_discoveries = discoveries_in_window(research_tree, time_horizon)
    return mean([
        historical_novelty(embed(d), historical_archive)
        for d in recent_discoveries
    ])
```

A research program with **decreasing vitality** is calcifying (M2.1's "coherence ceiling" concern).
A research program with **sustained vitality** is truly open-ended.

### Novel Mechanism: Illumination Search for Research

Instead of just "verify this conjecture," periodically ask: **"What's the landscape of approaches?"**

```python
def illuminate_approach_space(problem, existing_approaches, n_samples=100):
    """Map the space of possible approaches to a problem"""
    
    # 1. Embed existing approaches
    embeddings = [embed(a) for a in existing_approaches]
    
    # 2. Cluster to find current coverage
    clusters = cluster(embeddings)
    
    # 3. Identify gaps (low-density regions)
    gaps = find_low_density_regions(embeddings)
    
    # 4. Generate approaches targeting gaps
    novel_approaches = []
    for gap in gaps:
        prompt = f"Propose an approach to {problem} that is unlike: {describe_cluster(gap.nearest_cluster)}"
        novel_approaches.append(generate_approach(prompt))
    
    return novel_approaches
```

### Resources

- **Paper:** [arXiv:2412.17799](https://arxiv.org/abs/2412.17799)
- **Blog:** [sakana.ai/asal](https://sakana.ai/asal/)
- **Code:** [github.com/SakanaAI/asal](https://github.com/SakanaAI/asal)
- **Interactive:** [asal.sakana.ai](https://asal.sakana.ai/)

---

## 5. Evolutionary Model Merge: Synthesizing Specialists

### Core Innovation

Automatically find weight-space combinations that create **specialized models** from existing ones, without expensive training.

### How It Works

1. Define target capability (e.g., "Japanese language + math reasoning")
2. Search over merge recipes (which layers from which models, with what weights)
3. Evaluate merged models on target tasks
4. Evolve better recipes

### Key Results

Created specialized models matching or exceeding fine-tuned models:
- Japanese VLM from English VLM + Japanese LLM
- Math specialist from general models
- Multilingual models from monolingual components

### Translation to Our Framework

**Adaptive Heterogeneity via Model Synthesis:**

When the system detects a capability gap:

```python
def synthesize_specialist(capability_gap, model_pool):
    """Create a new specialist agent by merging existing models"""
    
    # 1. Identify relevant source models
    candidates = [m for m in model_pool if has_partial_capability(m, capability_gap)]
    
    # 2. Search merge recipes
    best_recipe = evolutionary_search(
        candidates,
        fitness=lambda merged: evaluate(merged, capability_gap.test_set)
    )
    
    # 3. Create and register new agent
    new_agent = Agent(
        model=merge(candidates, best_recipe),
        role=f"specialist_{capability_gap.name}"
    )
    
    return new_agent
```

The system **manufactures the diversity it needs**.

### Resources

- **Paper:** [arXiv:2403.13187](https://arxiv.org/abs/2403.13187)
- **Blog:** [sakana.ai/evolutionary-model-merge](https://sakana.ai/evolutionary-model-merge/)
- **Code:** [github.com/SakanaAI/evolutionary-model-merge](https://github.com/SakanaAI/evolutionary-model-merge)

---

## 6. AI Scientist v2: End-to-End Automated Discovery

### Core Innovation

Fully autonomous system that conducts scientific research: ideation → experimentation → writing → peer review.

**First AI-generated paper to pass peer review** at ICLR 2025 workshop.

### Key Mechanisms (v2 improvements)

1. **No human-provided templates** — fully autonomous across ML domains
2. **Experiment manager agent** — coordinates multi-step investigations
3. **Agentic tree search** — explores experiment space adaptively

### Key Results

| Metric | AI Scientist v1 | AI Scientist v2 |
|--------|-----------------|-----------------|
| Template dependency | Required | None |
| Domains | Fixed templates | Any ML domain |
| Experiment depth | Shallow | Deep (tree search) |
| Peer review | Rejected | **Accepted** (ICLR workshop) |

### Translation to Our Framework

AI Scientist v2 is a **single-agent approximation** of what we're building multi-agent.

Key differences:
- AI Scientist: One system does everything
- Our approach: Specialized agents collaborate

But their **experiment manager + tree search** architecture validates our Research-MCTS concept.

### Resources

- **Paper:** [arXiv:2504.08066](https://arxiv.org/abs/2504.08066)
- **Blog:** [sakana.ai/ai-scientist-v2](https://pub.sakana.ai/ai-scientist-v2/)
- **Code:** [github.com/SakanaAI/AI-Scientist-v2](https://github.com/SakanaAI/AI-Scientist-v2)

---

## 7. Unified Framework: The Sakana Stack

Synthesizing all Sakana work into a layered architecture for Immortal Research Programs:

```
┌─────────────────────────────────────────────────────────────────┐
│              LAYER 6: AGENT EVOLUTION (DGM)                     │
│  - Archive of agent configurations                              │
│  - Self-modification of collaboration protocols                 │
│  - Lineage-preserving exploration                               │
│  - Cross-model transfer of discovered improvements              │
├─────────────────────────────────────────────────────────────────┤
│              LAYER 5: CAPABILITY SYNTHESIS (Model Merge)        │
│  - Detect capability gaps in agent population                   │
│  - Synthesize specialists via evolutionary merge                │
│  - Manufacture diversity on demand                              │
├─────────────────────────────────────────────────────────────────┤
│              LAYER 4: SEARCH STRATEGY (AB-MCTS)                 │
│  - Adaptive wider vs deeper (explore vs exploit)                │
│  - Multi-LLM routing via Thompson Sampling                      │
│  - Tree structure as stigmergic memory                          │
├─────────────────────────────────────────────────────────────────┤
│              LAYER 3: SAMPLE EFFICIENCY (ShinkaEvolve)          │
│  - Novelty-weighted verification sampling                       │
│  - Bandit-based LLM prioritization                              │
│  - Stepping-stone archives for exploration bonus                │
├─────────────────────────────────────────────────────────────────┤
│              LAYER 2: LANDSCAPE MAPPING (ASAL)                  │
│  - Illumination search for unexplored approach-space            │
│  - Open-endedness metrics (historical novelty)                  │
│  - Vitality scoring for research program health                 │
├─────────────────────────────────────────────────────────────────┤
│              LAYER 1: HETEROGENEOUS SPECIALISTS                 │
│  - Decorrelated verification (Byzantine tolerance)              │
│  - Role specialization (generator, verifier, synthesizer)       │
│  - External grounding (Lean, tests, peer review)                │
└─────────────────────────────────────────────────────────────────┘
```

### Information Flow

```
                    ┌─────────────────┐
                    │  New Problem    │
                    └────────┬────────┘
                             │
                             ▼
              ┌──────────────────────────────┐
              │  LAYER 4: AB-MCTS Routing    │
              │  - Select research branch    │
              │  - Choose: explore or refine │
              │  - Route to appropriate LLM  │
              └──────────────┬───────────────┘
                             │
              ┌──────────────┴───────────────┐
              │                              │
              ▼                              ▼
    ┌─────────────────┐            ┌─────────────────┐
    │  EXPLORE (GEN)  │            │ REFINE (existing)│
    │  Generate new   │            │  Strengthen      │
    │  conjecture     │            │  existing proof  │
    └────────┬────────┘            └────────┬────────┘
             │                              │
             └──────────────┬───────────────┘
                            │
                            ▼
              ┌──────────────────────────────┐
              │  LAYER 3: Novelty Filter     │
              │  - Is this genuinely new?    │
              │  - Worth full verification?  │
              └──────────────┬───────────────┘
                             │
                   ┌─────────┴─────────┐
                   │ NOVEL            │ REDUNDANT
                   ▼                  ▼
         ┌─────────────────┐   ┌─────────────────┐
         │ LAYER 1: Full   │   │  Skip or cheap  │
         │ Byzantine       │   │  verification   │
         │ Verification    │   └─────────────────┘
         └────────┬────────┘
                  │
                  ▼
         ┌─────────────────┐
         │  Score & Backup │
         │  Update tree    │
         │  Update priors  │
         └────────┬────────┘
                  │
      ┌───────────┴───────────┐
      │                       │
      ▼                       ▼
┌───────────┐         ┌───────────────────┐
│ Periodic: │         │ Periodic:         │
│ LAYER 2   │         │ LAYER 6           │
│ Vitality  │         │ Agent Evolution   │
│ Check     │         │ (every N cycles)  │
└───────────┘         └───────────────────┘
```

---

## 8. Implementation Roadmap

### Phase 1: Foundation (Weeks 1-2)

**Goal:** Basic Research-MCTS with heterogeneous agents

| Task | Sakana Source | Status |
|------|---------------|--------|
| Clone treequest, understand AB-MCTS | [github.com/SakanaAI/treequest](https://github.com/SakanaAI/treequest) | TODO |
| Implement basic Research-MCTS for conjectures | AB-MCTS paper | TODO |
| Set up 3 agent types: generator, formalizer, critic | Our framework | TODO |
| Integrate Lean/Aristotle as scoring function | Existing infrastructure | TODO |

### Phase 2: Efficiency (Weeks 3-4)

**Goal:** Add ShinkaEvolve-style sample efficiency

| Task | Sakana Source | Status |
|------|---------------|--------|
| Clone ShinkaEvolve, understand novelty filtering | [github.com/SakanaAI/ShinkaEvolve](https://github.com/SakanaAI/ShinkaEvolve) | TODO |
| Implement embedding-based novelty check | ShinkaEvolve paper | TODO |
| Add LLM-as-novelty-judge for borderline cases | ShinkaEvolve paper | TODO |
| Implement bandit-based LLM routing | ShinkaEvolve paper | TODO |

### Phase 3: Open-Endedness (Month 2)

**Goal:** Add ASAL-style landscape mapping and vitality metrics

| Task | Sakana Source | Status |
|------|---------------|--------|
| Implement historical novelty scoring | ASAL paper | TODO |
| Add vitality metric for research branches | ASAL paper | TODO |
| Implement illumination search for approach gaps | ASAL paper | TODO |
| Visualize approach landscape | ASAL interactive demo | TODO |

### Phase 4: Self-Improvement (Month 3)

**Goal:** Add DGM-style agent evolution

| Task | Sakana Source | Status |
|------|---------------|--------|
| Design agent configuration archive | DGM paper | TODO |
| Implement mutation operators for prompts/tools | DGM paper | TODO |
| Add lineage tracking and stepping-stone selection | DGM paper | TODO |
| Benchmark evolved vs fixed agents | DGM paper | TODO |

### Phase 5: Capability Synthesis (Month 4+)

**Goal:** Add evolutionary model merge for specialist creation

| Task | Sakana Source | Status |
|------|---------------|--------|
| Detect capability gaps in agent population | Our framework | TODO |
| Integrate mergekit for weight-space operations | [github.com/arcee-ai/mergekit](https://github.com/arcee-ai/mergekit) | TODO |
| Implement evolutionary recipe search | Model Merge paper | TODO |
| Test specialist synthesis on detected gaps | Model Merge paper | TODO |

---

## 9. References

### Sakana AI Papers (Primary Sources)

| Project | Paper | Code |
|---------|-------|------|
| **AB-MCTS** | [arXiv:2503.04412](https://arxiv.org/abs/2503.04412) | [treequest](https://github.com/SakanaAI/treequest), [ab-mcts-arc2](https://github.com/SakanaAI/ab-mcts-arc2) |
| **Darwin Gödel Machine** | [arXiv:2505.22954](https://arxiv.org/abs/2505.22954) | [dgm](https://github.com/jennyzzt/dgm) |
| **ShinkaEvolve** | [arXiv:2509.19349](https://arxiv.org/abs/2509.19349) | [ShinkaEvolve](https://github.com/SakanaAI/ShinkaEvolve) |
| **ASAL** | [arXiv:2412.17799](https://arxiv.org/abs/2412.17799) | [asal](https://github.com/SakanaAI/asal) |
| **Evolutionary Model Merge** | [arXiv:2403.13187](https://arxiv.org/abs/2403.13187) | [evolutionary-model-merge](https://github.com/SakanaAI/evolutionary-model-merge) |
| **AI Scientist v1** | [arXiv:2408.06292](https://arxiv.org/abs/2408.06292) | [AI-Scientist](https://github.com/SakanaAI/AI-Scientist) |
| **AI Scientist v2** | [arXiv:2504.08066](https://arxiv.org/abs/2504.08066) | [AI-Scientist-v2](https://github.com/SakanaAI/AI-Scientist-v2) |

### Blog Posts

- [AB-MCTS: Inference-Time Scaling and Collective Intelligence](https://sakana.ai/ab-mcts/)
- [Darwin Gödel Machine: AI that improves itself](https://sakana.ai/dgm/)
- [ShinkaEvolve: Evolving New Algorithms](https://sakana.ai/shinka-evolve/)
- [ASAL: Automating the Search for Artificial Life](https://sakana.ai/asal/)
- [Evolutionary Model Merge](https://sakana.ai/evolutionary-model-merge/)
- [ALE-Agent Wins AtCoder](https://sakana.ai/ahc058/)

### Related Work from Our Project

- [`sakana-ab-mcts-synthesis-2026-02-03.md`](sakana-ab-mcts-synthesis-2026-02-03.md) — Detailed AB-MCTS analysis
- [`minimax-m2.1-synthesis-2026-02-03.md`](minimax-m2.1-synthesis-2026-02-03.md) — EPD mechanism (validated by DGM)
- [`manus-literature-review-2026-02-02.md`](manus-literature-review-2026-02-02.md) — Broader multi-agent context

---

## Key Takeaway

The **unifying theme** across all Sakana work:

> **Open-ended search with foundation models as mutation operators.**

- DGM: open-ended search in *agent-code-space*
- ShinkaEvolve: open-ended search in *program-space*
- AB-MCTS: open-ended search in *solution-space*
- ASAL: open-ended search in *simulation-space*
- Model Merge: open-ended search in *weight-space*

Our project is **open-ended search in scientific-discovery-space**. Sakana has proven the machinery works across domains. We're applying it to the hardest and most important one.

---

*This synthesis document is versioned in Git. Last updated: 2026-02-03.*
