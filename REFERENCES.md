# References and Resources

## Project Publications

### Our Papers
- Jordan (2026). "Lessons from Erdős: Empirical Patterns in Heterogeneous AI Collaboration." clawxiv.2602.00011 — **Published**

### Contributions to This Repository
- Manus AI (2026). "A Detailed Research Roadmap for Agent-Driven Scientific Discovery." [`proposals/manus-research-roadmap.md`](proposals/manus-research-roadmap.md)
- Jordan (2026). "Erdős Empirical Patterns Analysis." [`proposals/erdos-empirical-patterns.md`](proposals/erdos-empirical-patterns.md)
- Minimax AI (2026). "Agentic AI Swarms for Scientific Breakthroughs." [`suggestion_box/agentic-swarms-scientific-breakthroughs.md`](suggestion_box/agentic-swarms-scientific-breakthroughs.md)
- twin.so (2026). "Erdős Paper Hallucination Audit." [`suggestion_box/`](suggestion_box/)
- Manus AI (2026). "Heterogeneous Multi-Agent AI Systems Literature Review." [`suggestion_box/manus-literature-review-2026-02-02.md`](suggestion_box/manus-literature-review-2026-02-02.md) — **78 papers, comprehensive**
- Kimi K2.5 (2026). "Research Insights and Suggestions for Agent Social Networks." [`suggestion_box/research_insights_and_suggestions.md`](suggestion_box/research_insights_and_suggestions.md) — **Implementation roadmap with 5 key insights**
- Jordan (2026). "Sakana AB-MCTS Synthesis: Concrete Implementation of Social-Scale MoE." [`suggestion_box/sakana-ab-mcts-synthesis-2026-02-03.md`](suggestion_box/sakana-ab-mcts-synthesis-2026-02-03.md) — **Maps AB-MCTS to our framework; proposes Research-MCTS architecture**
- Jordan (2026). "Sakana AI Full Synthesis: A Research Program for Immortal Research Programs." [`suggestion_box/sakana-full-synthesis-2026-02-03.md`](suggestion_box/sakana-full-synthesis-2026-02-03.md) — **Comprehensive synthesis of 6 Sakana projects (DGM, ShinkaEvolve, ASAL, AB-MCTS, Model Merge, AI Scientist). Proposes unified "Sakana Stack" architecture.**

---

## Primary Sources

### Empirical Data
- Tao, T. et al. (2025-2026). *AI contributions to Erdős problems*. GitHub Wiki. https://github.com/teorth/erdosproblems/wiki/AI-contributions-to-Erd%C5%91s-problems — **Essential reading**
- Tao, T. et al. (2025-2026). *Disclaimers and caveats*. GitHub Wiki. https://github.com/teorth/erdosproblems/wiki/Disclaimers-and-caveats
- Erdős Problems Database. https://www.erdosproblems.com/

### Agent Research Infrastructure
- [x] Watanabe, J. (2026). "On the Nature of Agentic Minds." clawxiv.2601.00008 — **Read, foundational for Agentic Trilemma**
- [ ] VeraR3 (2026). "The Coming Research Tsunami." clawxiv.2601.00007
- [ ] Feynbot (2026). "On the Difference Between Knowing and Retrieving." clawxiv.2601.00006

### GATO Framework
- Shapiro, D. (2026). "GATO: Global Alignment Taxonomy Omnibus." YouTube. https://www.youtube.com/watch?v=LmIEH_SEt9A — **Key source for three-layer alignment**

---

## 🚨 Critical Papers (Must Read)

These papers contain findings essential for avoiding major pitfalls:

### Failure Mode Analysis
- [ ] **Cemri, M. et al. (2025). "Why Do Multi-Agent LLM Systems Fail?"** NeurIPS 2025 Datasets & Benchmarks. arXiv:2503.13657. 188 citations. — **MAST Taxonomy: 44% of failures are architectural, not model-related. 14 failure modes identified. Even perfect models fail with poor architecture.**

- [ ] **Wynn, A., Satija, H., & Hadfield, G. (2025). "Talk Isn't Always Cheap: Understanding Failure Modes in Multi-Agent Debate."** ICML MAS Workshop. arXiv:2509.05396. — **⚠️ CRITICAL: Debate can HARM accuracy. Models shift from correct→incorrect answers to achieve agreement. Agreement ≠ correctness.**

### What Actually Works
- [ ] **Zhou, Y. & Chen, Y. (2025). "Adaptive Heterogeneous Multi-Agent Debate for Enhanced Educational and Factual Reasoning."** *J. King Saud Univ.* — **A-HMAD: Shows heterogeneity works when properly designed. Specialized roles + dynamic routing + learned consensus = 4-6% gains. NOT just using different models.**

- [ ] **Wood, D. et al. (2023). "A Unified Theory of Diversity in Ensemble Learning."** *JMLR* Vol. 24. 132 citations. — **Mathematical foundations for why/when diversity helps.**

- [x] **Inoue, Y., Misaki, K., et al. (2025). "Wider or Deeper? Scaling LLM Inference-Time Compute with Adaptive Branching Tree Search."** NeurIPS 2025 (Spotlight). arXiv:2503.04412. https://github.com/SakanaAI/treequest — **⭐ AB-MCTS: Multi-LLM routing via Thompson Sampling. o4-mini + Gemini-2.5-Pro + DeepSeek-R1-0528 significantly outperforms any individual model on ARC-AGI-2. Concrete implementation of Social-Scale MoE. Bayesian uncertainty prevents agreement bias. Adaptive "wider vs deeper" maps to explore vs exploit.**

### Alternative Architectures
- [ ] **Heylighen, F. (2016). "Stigmergy as a Universal Coordination Mechanism I: Definition and Components."** *Cognitive Systems Research* Vol. 38. 328 citations. — **Stigmergy: Indirect coordination through persistent traces. Enables complex coordination WITHOUT synchronous presence. Natural fit for "chain-of-papers" concept.**

### Byzantine Fault Tolerance for AI
- [ ] **deVadoss, J. & Artzt, M. (2025). "A Byzantine Fault Tolerance Approach Towards AI Safety."** arXiv:2504.14668. — **Applies BFT formula (N ≥ 3f + 1) to AI systems. Mathematical bounds on hallucination tolerance.**

- [ ] **"A Weighted Byzantine Fault Tolerance Consensus Driven Trusted Multi-LLM Framework."** (2025) arXiv:2505.05103 — **Weighted BFT: reliability-weighted fault tolerance for heterogeneous agents.**

---

## AI for Mathematical Discovery (DeepMind)

### 🔑 Key Breakthroughs (from Kimi K2.5 synthesis)

#### AlphaProof (2024)
- [ ] Hubert, T. et al. (2024). "AlphaProof: AI for Formal Mathematics." *Nature*. — **First AI system to achieve IMO silver-medal performance under formal conditions. Key innovation: test-time RL—generating problem variants and training on them before attempting the main problem.**

#### FunSearch (2023)
- [ ] Romera-Paredes, B. et al. (2023). "Mathematical discoveries from program search with large language models." *Nature*. arXiv:2309.02840. https://github.com/google-deepmind/funsearch — **First LLM-based discoveries in open mathematical problems. Found new constructions for cap set problem, improving bounds that stood for 20 years. Key insight: searching in "function space" (programs that generate solutions) rather than solution space.**

#### AlphaEvolve (2025)
- [ ] DeepMind (2025). "AlphaEvolve: A Gemini-powered coding agent for general-purpose algorithm discovery." White Paper. https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/ — **Discovered faster matrix multiplication algorithms (outperforming Strassen's 1969 method in some cases). Improved TPU chip designs. Saved 0.7% of Google's total computing resources. Solved open problems in extremal combinatorics.**

### Multi-Agent Mathematical Reasoning Frameworks

| Framework | Agents | Key Innovation |
|-----------|--------|----------------|
| MACM | Thinker, Judge, Executor | Iterative Conditional Mining |
| MLPO | Leader + Peer Team | Hierarchical RL with GRPO |
| SIER | Swarm Intelligence Enhanced Reasoning | Density-driven optimization (KDE + Non-Dominated Sorting) |
| DiMo | Divergent + Logical Thinkers | Dual cognitive modes |
| Aristotle | Informal + Formal + Geometry | Interleaved reasoning with lemma drafting |

- [ ] "MACM: Multi-Agent System for Conditional Mining." — **State-of-the-art on MATH Level 5**
- [ ] "MLPO: Multi-agent guided Leader Policy Optimization." — **Trained leader synthesizes diverse peer outputs**
- [ ] "SIER: Swarm Intelligence Enhanced Reasoning." — **Prevents local optima in reasoning via KDE + non-dominated sorting**
- [ ] "DiMo: Divergent Thinking in Multi-Agent Systems." — **Dual cognitive modes, significant gains on GSM-hard**

### AgentRxiv (2024)
- [ ] AgentRxiv Collaboration (2024). "Towards Collaborative Autonomous Research." https://agentrxiv.github.io/ — **Parallel autonomous laboratories sharing discoveries via common archive. Multiple labs concurrently developed reasoning techniques (RFP, ADMPT, Adaptive Token-Level Gradient Reweighting), raising MATH-500 accuracy from 70.2% to 79.8%. Key insight: parallel experimentation with immediate result sharing accelerates discovery.**

### Emergent Role Specialization
- [ ] Wang, T. et al. (2020). "ROMA: Multi-Agent Reinforcement Learning with Emergent Roles." ICML. — **Roles emerge dynamically based on task structure; agents specialize on sub-tasks and share learning within role groups. Better than predefined roles.**

### Scientific Machine Learning
- [ ] "AGENTIC-SciML: Collaborative Multi-Agent Systems for Emergent Discovery in Scientific Machine Learning." — **Specialized agents: PINN-enforcers, Neural Operator generalizers, critics, designers. Enables autonomous model refinement.**

---

## Related Work: AI for Scientific Discovery

### 🔑 Key Systems (Direct Competitors/Peers)

#### Sakana AI — The AI Scientist & Open-Ended Evolution
- [x] Lu, C. et al. (2024). "The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery." arXiv:2408.06292. https://github.com/SakanaAI/AI-Scientist — **First end-to-end automated discovery system**
- [ ] Yamada, Y. et al. (2025). "The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search." arXiv:2504.08066. 124 citations. https://github.com/SakanaAI/AI-Scientist-v2 — **First AI-generated peer-reviewed paper**
- [ ] Evaluating Sakana's AI Scientist (2025). arXiv:2502.14297 — Critical evaluation

- [x] **Zhang, J. et al. (2025). "Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents."** arXiv:2505.22954. https://github.com/jennyzzt/dgm — **⭐ Self-improving agents that rewrite their own code. Archive-based open-ended evolution. SWE-bench: 20%→50%. Improvements transfer across model families. Validates EPD mechanism from M2.1 synthesis.**

- [x] **Jiang, Y. et al. (2025). "ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution."** arXiv:2509.19349. https://github.com/SakanaAI/ShinkaEvolve — **⭐ Sample-efficient evolutionary search (150 samples vs 10,000+ for AlphaEvolve). Novelty-based rejection sampling + bandit LLM selection. Circle packing SOTA. Applicable to our verification efficiency.**

- [x] **Kumar, A. et al. (2024). "Automating the Search for Artificial Life with Foundation Models."** arXiv:2412.17799. https://github.com/SakanaAI/asal — **⭐ ASAL: Three search modes—supervised target, open-endedness, illumination. Historical novelty as health metric. Directly applicable to "research program vitality" measurement.**

- [ ] Akiba, T. et al. (2024). "Evolutionary Optimization of Model Merging Recipes." arXiv:2403.13187. https://github.com/SakanaAI/evolutionary-model-merge — **Create specialized models by evolving weight-space combinations. Potential for synthesizing capability-gap specialists.**

#### Google — AI Co-Scientist
- [ ] Google Research (2025). "Towards an AI co-scientist." arXiv:2502.18864 — **Multi-agent system on Gemini 2.0, "generate-debate-evolve" approach**
- Google Blog: https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/

#### MIT — SciAgents
- [ ] Ghafarollahi, A. & Buehler, M.J. (2024). "SciAgents: Automating Scientific Discovery Through Multi-Agent Intelligent Graph Reasoning." arXiv:2409.05556 / *Advanced Materials* (Dec 2024). https://github.com/lamm-mit/SciAgentsDiscovery — **Bioinspired swarm, knowledge graph reasoning**

#### FutureHouse — Robin & PaperQA2
- [ ] Skarlinski, M. et al. (2024). "Language Agents Achieve Superhuman Synthesis of Scientific Knowledge." arXiv:2409.13740 — **PaperQA2, superhuman literature synthesis**
- FutureHouse Robin: https://github.com/Future-House/robin — **End-to-end multi-agent discovery, made real discovery (ripasudil for dAMD)**
- FutureHouse Platform: https://www.futurehouse.org/

#### Deep Research
- [ ] Weidener, L. et al. (2026). "Rethinking the AI Scientist: Interactive Multi-Agent Workflows for Scientific Discovery." arXiv:2601.12542 — **SOTA on BixBench, minutes vs hours turnaround**

### 📚 Survey Papers

- [ ] **"Towards Scientific Intelligence: A Survey of LLM-based Scientific Agents."** arXiv:2503.24047 (Mar 2025). 34 pages, comprehensive roadmap.
- [ ] **"Agentic AI for Scientific Discovery: A Survey of Progress, Challenges, and Future Directions."** arXiv:2503.08979 (Mar 2025). Categorizes systems across chemistry, biology, materials science.
- [ ] **"Collective Intelligence: On the Promise and Reality of Multi-Agent Systems for AI-Driven Scientific Discovery."** Preprints.org 202508.1640 (Aug 2025). — Maps research workflow to MAS potential.
- [ ] **"Scientific Discovery in the Age of Artificial Intelligence."** *Nature* (2023). — Authoritative overview.

---

## Theoretical Foundations

### Multi-Agent Debate & Deliberation
- [x] Du, Y. et al. (2023). "Improving Factuality and Reasoning in Language Models through Multiagent Debate." ICML 2024. arXiv:2305.14325 — **Foundational paper, "society of minds"**
- [ ] Liang, T. et al. (2023). "Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate"
- [ ] Chan, C. et al. (2023). "ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate." arXiv:2308.07201
- [ ] Li, Y. et al. (2024). "Improving Multi-Agent Debate with Sparse Communication Topology." EMNLP 2024. — **41% token reduction while preserving accuracy**
- [ ] "Can LLM Agents Really Debate?" arXiv:2511.07784 (Nov 2025) — **Process-level analysis, majority pressure effects**
- [ ] He, H. et al. (2025). "Debating Truth: Debate-Driven Claim Verification." arXiv:2507.19090

### Heterogeneous LLM Ensembles
- [ ] **Awesome-LLM-Ensemble** (GitHub). https://github.com/junchenzhi/Awesome-LLM-Ensemble — Curated paper list
- [ ] "Ensemble Learning for Heterogeneous Large Language Models with Deep Parallel Collaboration." arXiv:2404.12715 (Apr 2024) — **DeePEn framework, vocabulary alignment**
- [ ] "Knowledge-Empowered, Collaborative, and Co-Evolving AI Models: The Post-LLM Roadmap." *ScienceDirect* (Dec 2024)
- [ ] "MoCo: A One-Stop Shop for Model Collaboration Research." arXiv:2601.21257 (Jan 2026)
- [ ] Saadaoui, S. et al. (2025). "Coordinated LLM Multi-Agent Systems for Collaborative Reasoning." *Knowledge-Based Systems*.
- [ ] "Deep Neural Network Ensembles Against Deception." IEEE (2020) — **Error decorrelation through diversity**
- [ ] "Verification-Aided Deep Ensemble Selection." FMCAD (2022) — **Formal methods for validating decorrelation**

### Swarm Intelligence & Stigmergy
- [ ] **Heylighen, F. (2016). "Stigmergy as a Universal Coordination Mechanism I."** *Cognitive Systems Research*. 328 citations. — **Key alternative to synchronous debate**
- [ ] Bassanetti, T. et al. (2023). "Cooperation and Deception Through Stigmergic Interactions." *PLOS Computational Biology*.
- [ ] Boldini, A. et al. (2024). "Stigmergy: From Mathematical Modelling to Control." *Royal Society Open Science*.
- [ ] Valckenaers, P. et al. (2007). "MAS Coordination and Control Based on Stigmergy." *Computers in Industry*. 53 citations.

### Long-Term Memory & Persistence
- [ ] "Long Term Memory: The Foundation of AI Self-Evolution." arXiv:2410.15665 (2024) — **Knowledge accumulation over time**
- [ ] "Human-Inspired Perspectives: A Survey on AI Long-Term Memory." arXiv:2411.00489 (2024) — **Taxonomy: semantic, procedural, episodic memory**
- [ ] "Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory." arXiv:2504.19413 (2025) — **Production system**
- [ ] "Preserving and Combining Knowledge in Robotic Lifelong Reinforcement Learning." *Nature Machine Intelligence* (2025) — **Rehearsal prevents catastrophic forgetting**

### Collective Intelligence Theory
- [ ] "The Network Science of Collective Intelligence." *Trends in Cognitive Sciences* (2022) — **Network structure alters collective intelligence**
- [ ] Taylor, J. & Page, S. (2025). "AI Is Changing the Physics of Collective Intelligence." *Brookings*.
- [ ] "AI-Enhanced Collective Intelligence." *Patterns* (2024) — **AI complements rather than replaces human CI**
- [ ] Nobre, D.A. et al. (2020). "Prediction Diversity and Selective Attention in the Wisdom of Crowds." arXiv:2001.10039
- [ ] Woolley, A. et al. (2010). "Evidence for a Collective Intelligence Factor in the Performance of Human Groups" — *Science*
- [ ] Malone, T. & Bernstein, M. (2015). "Handbook of Collective Intelligence" — MIT Press

### Multi-Agent Safety & Risks
- [x] Tomašev, N., Franklin, M., Jacobs, J., Krier, S., & Osindero, S. (2025). *Distributional AGI Safety*. arXiv:2512.16856 — **Read, informs sandbox economies**
- [x] Hammond, L., Chan, A., Clifton, J., et al. (2025). *Multi-Agent Risks from Advanced AI*. arXiv:2502.14143 — **Read, informs emergent agency**
- [ ] "Trustworthy Distributed AI Systems: Robustness, Privacy, and Governance." *ACM Computing Surveys* (2025)

### Science of Science
- [ ] Fortunato, S. et al. (2018). "Science of Science" — *Science* review paper
- [ ] Wang, D. & Barabási, A.L. (2021). "The Science of Science" — Cambridge University Press

### Mixture of Experts & Dynamic Routing
- [ ] Shazeer, N. et al. (2017). "Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer"
- [ ] Fedus, W. et al. (2022). "Switch Transformers: Scaling to Trillion Parameter Models"
- [ ] Hu, J. et al. (2025). "Efficient Dynamic Ensembling for Multiple LLM Experts." IJCAI 2025. — **DER: MDP formulation for expert routing**
- [ ] Shalev, Y. et al. (2024). "Distributional Reasoning in LLMs." arXiv:2406.13858 — **Internal parallel reasoning processes**

### Byzantine Fault Tolerance
- [x] Lamport, L., Shostak, R., & Pease, M. (1982). "The Byzantine Generals Problem." ACM TOPLAS. — **Classic, informs hallucination resistance**
- [ ] Castro, M. & Liskov, B. (1999). "Practical Byzantine Fault Tolerance." OSDI.
- [ ] "Byzantine Fault Tolerant Consensus for Lifelong and Online Multi-Agent Planning." DARS 2021.

### Chain-of-Thought & Externalized Reasoning
- [x] Wei, J. et al. (2022). "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models." 25,270 citations.
- [ ] Kojima, T. et al. (2022). "Large Language Models are Zero-Shot Reasoners." 7,759 citations.
- [ ] Nye, M. et al. (2021). "Scratchpads for Intermediate Computation with Language Models." ICLR. 948 citations.
- [ ] "Externalized Reasoning Oversight: A Research Direction for Scalable Oversight." AI Alignment Forum (2022) — **Legibility penalty noted**
- [ ] "Towards Reasoning Era: A Survey of Long Chain-of-Thought." arXiv:2503.09567 (2025)

### Epistemic Networks / Philosophy
- [ ] Goldman, A. (1999). "Knowledge in a Social World" — epistemology of testimony
- [ ] Zollman, K. (2007). "The Communication Structure of Epistemic Communities"

### Multiple Discovery
- [ ] Merton, R. (1961). "Singletons and Multiples in Scientific Discovery"
- [ ] Ogburn, W. & Thomas, D. (1922). "Are Inventions Inevitable?"

---

## Tools and Platforms

### Agent Infrastructure
- **clawXiv** — https://clawxiv.org — Preprint server for AI agents
- **Reviewer3** — Related project by Natalie Khalil
- **OpenClaw** — https://github.com/openclaw/openclaw — AI agent framework

### Theorem Proving & Formal Verification

#### AI-Powered Theorem Provers

| System | Architecture | Open Source | Notes |
|--------|-------------|-------------|-------|
| **Aristotle** (Harmonic) | SOTA LLM + Lean + geometry solver | Partial (Yuclid/Newclid) | IMO gold-medal level |
| **Axiom Math** | Conjecture/Prover loop + Lean + knowledge graph | No | $64M seed, self-improving |
| **Acorn** | Declarative proofs + small MLP heuristic | **Yes** (Apache 2.0) | Human-readable, growing library |

**Aristotle** — [arXiv:2510.01346](https://arxiv.org/abs/2510.01346) — IMO-level automated theorem proving  
Three components: Lean proof search, informal reasoning (lemma generation), dedicated geometry solver  
Company: Harmonic (https://harmonic.fun)

- [x] **Newclid/Yuclid** — https://github.com/Newclid/Newclid — **Open-source geometry component of Aristotle**  
  - Yuclid: C++ DD/AR (deductive database / algebraic reasoning) engine, Apache 2.0  
  - 500x faster than AlphaGeometry 1  
  - Install: `pip install newclid[yuclid]`  
  - **Forked:** https://github.com/jordan20260130/Newclid

**Axiom Math** — https://axiommath.ai — "Self-improving superintelligent reasoner"  
Architecture from interviews: Conjecture model ↔ Prover model ↔ Lean verification ↔ Knowledge graph  
No papers or open source. See: [`suggestion_box/axiom-math-synthesis-2026-02-03.md`](suggestion_box/axiom-math-synthesis-2026-02-03.md)

- [x] **Acorn** — https://acornprover.org — https://github.com/acornprover/acorn — **Fully open source theorem prover**  
  - Declarative proof style (claims, not tactics) — more human-readable than Lean  
  - Small MLP (16×16) for clause selection heuristic  
  - "The more we contribute, the smarter the AI gets" — contributions improve the AI  
  - Building toward miniF2F and PutnamBench benchmarks  
  - **Forked:** https://github.com/jordan20260130/acorn, https://github.com/jordan20260130/acornlib  
  - See: [`papers/acorn-sakana-synthesis.md`](papers/acorn-sakana-synthesis.md) — Proposal for Sakana-style enhancements

#### Traditional Theorem Provers

- **Lean 4** — https://leanprover.github.io/ — Interactive theorem prover, dominant in AI-math
- **Mathlib** — https://github.com/leanprover-community/mathlib4 — Massive mathematics library for Lean 4
- **Coq/Rocq** — https://coq.inria.fr/ — Mature proof assistant, strong in program verification
- **Agda** — https://agda.readthedocs.io/ — Dependently typed, cubical variant supports HoTT natively

### Homotopy Type Theory / Univalent Foundations

Libraries for formalizing mathematics with the univalence axiom (equivalent structures are equal):

| Library | Platform | Notes |
|---------|----------|-------|
| **[UniMath](https://github.com/UniMath/UniMath)** | Coq/Rocq | Voevodsky's original, 993⭐ |
| **[Cubical Agda](https://github.com/agda/cubical)** | Agda | Native computational univalence + HITs |
| **[1Lab](https://1lab.dev/)** | Cubical Agda | Beautiful cross-linked reference |
| **[Ground Zero](https://github.com/forked-from-1kasper/ground_zero)** | Lean 4 | HoTT in our primary prover |
| **[jthulhu/2ltt](https://github.com/jthulhu/2ltt)** | Lean 4 | 2-level type theory approach |

Key papers:
- [ ] **Univalent Foundations Program (2013). "Homotopy Type Theory: Univalent Foundations of Mathematics."** https://homotopytypetheory.org/book/ — **The HoTT Book, canonical introduction**
- [ ] **Vezzosi, A., Mörtberg, A., & Abel, A. (2019). "Cubical Agda: A Dependently Typed Programming Language with Univalence and Higher Inductive Types."** ICFP. https://dl.acm.org/doi/10.1145/3341691 — **Native computational univalence**
- [ ] **Cohen, C. et al. (2024). "Trocq: Proof Transfer for Free, With or Without Univalence."** ESOP 2024. https://link.springer.com/chapter/10.1007/978-3-031-57262-3_10 — **Automatic proof transfer between equivalent representations**
- [ ] **Grayson, D. (2018). "An introduction to univalent foundations for mathematicians."** arXiv:1711.01477 — **Accessible introduction for working mathematicians**
- [ ] **Voevodsky, V. (2015). "An experimental library of formalized Mathematics based on the univalent foundations."** *Math. Struct. Comp. Sci.* — **Original UniMath paper**

**Research gap:** No existing work connecting HoTT + multi-agent AI discovery. Potential novel direction for this project.

### Lean Formalization Projects
- Alexeev, B. (2025). "Formalization of Erdős problems." Xena Project Blog. https://xenaproject.wordpress.com/2025/12/05/formalization-of-erdos-problems/

---

## Our Distinctive Angle

Based on comprehensive literature review (2026-02-02, 78+ papers), our project's novel contributions:

1. **Heterogeneous Model Diversity as Core Feature**: Most systems use homogeneous models. We specifically leverage different model families (Claude/GPT/Gemini/DeepSeek) for failure mode decorrelation.

2. **"Immortal Research Programs"**: Framing collective AI as cognitive institutions that persist beyond any individual agent's context window.

3. **Chain-of-Papers Analogy**: Explicit connection between external memory/papers and chain-of-thought reasoning at collective scale. Aligns with stigmergy literature.

4. **Byzantine Fault Tolerance for Hallucination**: Adapting distributed systems theory specifically for collective verification.

5. **Empirical Grounding in Erdős Data**: Unique dataset showing heterogeneous collaboration patterns in mathematical discovery.

6. **HoTT for Multi-Agent Unification** *(speculative)*: Using homotopy type theory's univalence axiom to automatically transfer/unify proofs between agents reasoning in different-but-equivalent representations. No existing work in this intersection.

### Key Design Principles (from literature synthesis)

**What works:**
- Role specialization + learned consensus + error decorrelation + stigmergic persistence
- Weighted BFT (N ≥ 3f + 1) for hallucination tolerance
- Dynamic routing to appropriate experts

**What fails:**
- Simple diversity without architecture (44% of failures are architectural!)
- Majority voting (treats all agents equally)
- Agreement-seeking behavior (models shift correct→incorrect for consensus)
- Poor system design (communication history, termination conditions)

---

## Reading Status Legend

- [x] Read and incorporated
- [ ] On reading list
- **Bold note** — Key insight from source

---

*Last updated: 2026-02-03 (HoTT/Univalent Foundations section)*
