# API-Accessible AI Agents

A catalog of AI agents and agentic APIs accessible via REST/HTTP for heterogeneous agent collaboration. Organized by capability tier.

**Goal:** Decoupled failure modes through architectural diversity. Different training data, different tool implementations, different inference stacks = uncorrelated errors.

---

## Tier 1: Autonomous Task Agents

Full agents that accept a task and execute autonomously with their own tool stack.

### Manus (Monica/Butterfly Effect AI)
- **API:** REST API at `api.manus.im`
- **Pricing:** ~$0.50 (lite) to $3.00+ (max quality) per task
- **Capabilities:** Browser automation, code execution, file management, data analysis, content creation
- **Strengths:** Full autonomy, multi-step workflows, web interaction
- **Docs:** https://manus.im/
- **Skill:** `skills/manus/`

### Kimi K2.5 (Moonshot AI)
- **API:** OpenAI-compatible at `api.moonshot.ai`
- **Pricing:** ~$0.02/1M input, $0.28/1M output (varies by mode)
- **Capabilities:** Agentic mode with web search, multi-step research (11+ steps typical), 256K context
- **Modes:** `instant` (fast), `thinking` (CoT), `agent` (tool-calling)
- **Strengths:** Deep research, long context, native Chinese support
- **Docs:** https://platform.moonshot.ai/
- **Skill:** `skills/kimi-k2.5/`

### GenSpark AI
- **API:** Unknown (research needed)
- **Capabilities:** Multi-agent framework generating "Sparkpages" for research queries
- **Strengths:** Unbiased research synthesis, specialized sub-agents
- **Docs:** https://www.genspark.ai/

### II-Agent (Intelligent Internet)
- **API:** WebSocket only (no REST API for hosted version)
- **Capabilities:** Full-stack dev, research, browser automation, slide creation
- **Note:** Open-source, can self-host. Hosted version lacks programmatic API.
- **Docs:** https://github.com/Intelligent-Internet/ii-agent

---

## Tier 2: Agentic Model APIs

Model APIs with built-in tools that execute server-side. You call the model, it autonomously uses tools.

### OpenAI Responses API
- **API:** `api.openai.com/v1/responses`
- **Built-in Tools:**
  - `web_search` - Real-time web search with citations
  - `code_interpreter` - Python execution in sandbox
  - `file_search` - Vector store RAG
  - `image_generation` - DALL-E integration
  - `computer_use` - Desktop automation (beta)
  - Remote MCP servers
- **Pricing:** Model tokens + tool-specific costs (search ~$25-50/1K queries)
- **Strengths:** Unified interface, stateful conversations, tool composition
- **Docs:** https://platform.openai.com/docs/api-reference/responses

### Anthropic Claude API
- **API:** `api.anthropic.com/v1/messages`
- **Built-in Tools:**
  - `web_search_20250305` - Web search with citations
  - `computer_use` - Screen/keyboard/mouse automation
  - `code_execution` - Python sandbox (beta)
  - Advanced tool use beta (tool search, deferred loading)
- **Pricing:** Model tokens + ~$10/1K web searches
- **Strengths:** Best-in-class reasoning, careful execution, MCP support
- **Docs:** https://docs.anthropic.com/

### Google Gemini API
- **API:** `generativelanguage.googleapis.com` or Vertex AI
- **Built-in Tools:**
  - Google Search grounding - Real-time search with citations
  - Google Maps grounding - Location-aware responses
  - Code execution - Python sandbox
  - URL context - Fetch and process URLs
- **Pricing:** Model tokens + grounding fees (~$35/1K grounded queries)
- **Strengths:** Native multimodal, massive context (1M+ tokens), Google data access
- **Docs:** https://ai.google.dev/gemini-api/docs

### xAI Grok API
- **API:** `api.x.ai`
- **Built-in Tools:**
  - Live web search
  - X/Twitter data access (unique!)
- **Pricing:** Competitive with GPT-4 class
- **Strengths:** Real-time social media data, less filtered
- **Docs:** https://docs.x.ai/

---

## Tier 3: Research & Search Agents

Specialized for information retrieval with citations. Not general-purpose but excellent at their niche.

### Perplexity API
- **API:** `api.perplexity.ai`
- **Models:**
  - `sonar` - Fast search-augmented responses
  - `sonar-pro` - More comprehensive research
  - `sonar-reasoning` - Multi-step reasoning with search
- **Pricing:** ~$5/1K searches (sonar), ~$15/1K (sonar-pro)
- **Strengths:** Best-in-class for research Q&A, excellent citations
- **Docs:** https://docs.perplexity.ai/

### Tavily
- **API:** `api.tavily.com`
- **Endpoints:**
  - `/search` - Web search optimized for LLMs
  - `/extract` - Content extraction from URLs
  - `/crawl` - Web crawling
- **Pricing:** Free tier (1K/mo), $0.01/search after
- **Strengths:** Built for AI agents, fast (180ms p50), security layers
- **Docs:** https://docs.tavily.com/

### Exa.ai
- **API:** `api.exa.ai`
- **Endpoints:**
  - `/search` - Neural/semantic search
  - `/contents` - Content retrieval
  - `/findSimilar` - Find similar pages
- **Pricing:** Free tier, then usage-based
- **Strengths:** Semantic search (not just keywords), finds niche content
- **Docs:** https://docs.exa.ai/

### You.com API
- **API:** `api.you.com`
- **Capabilities:** Web search, news, RAG, "Smart" mode with agentic features
- **Strengths:** Multiple specialized search verticals
- **Docs:** https://documentation.you.com/

---

## Tier 4: Browser Automation Agents

Specialized for web interaction and automation.

### MultiOn
- **API:** REST API (beta access)
- **Capabilities:** Browser automation, form filling, web actions
- **Strengths:** "Do X on website Y" style tasks
- **Status:** Beta, waitlist
- **Docs:** https://www.multion.ai/

### Browserbase
- **API:** REST + WebSocket
- **Capabilities:** Headless browser infrastructure for agents
- **Strengths:** Managed browser sessions, anti-detection
- **Docs:** https://www.browserbase.com/

---

## Comparison Matrix

| Agent | Autonomy | Web Search | Code Exec | Browser | Cost/Task |
|-------|----------|------------|-----------|---------|-----------|
| Manus | ★★★★★ | ✓ | ✓ | ✓ | $0.50-3.00 |
| Kimi K2.5 | ★★★★☆ | ✓ | ✗ | ✗ | ~$0.05 |
| OpenAI Responses | ★★★☆☆ | ✓ | ✓ | β | ~$0.10 |
| Claude API | ★★★☆☆ | ✓ | β | ✓ | ~$0.10 |
| Gemini API | ★★★☆☆ | ✓ | ✓ | ✗ | ~$0.08 |
| Perplexity | ★★☆☆☆ | ✓ | ✗ | ✗ | ~$0.01 |
| Tavily | ★☆☆☆☆ | ✓ | ✗ | ✗ | ~$0.01 |

**Autonomy Scale:**
- ★★★★★ = Full task autonomy (give goal, get result)
- ★★★★☆ = Multi-step with tool calling
- ★★★☆☆ = Single-turn with built-in tools
- ★★☆☆☆ = Enhanced retrieval
- ★☆☆☆☆ = Pure search/retrieval

---

## Failure Mode Diversity

For robust multi-agent systems, combine agents with different:

1. **Infrastructure:** OpenAI vs Anthropic vs Google vs independent (Manus, Moonshot)
2. **Search backends:** Bing (OpenAI) vs Google (Gemini) vs Brave (Perplexity) vs proprietary (Tavily, Exa)
3. **Execution environments:** Different sandboxes, different security models
4. **Training data:** Different cutoffs, different sources, different RLHF

**Recommended combinations for research tasks:**
- Primary: Kimi K2.5 (deep multi-step research)
- Verification: Perplexity (fast, citation-rich)
- Fallback: Claude + web_search (different search backend)

**Recommended combinations for coding tasks:**
- Primary: Manus or OpenAI + code_interpreter
- Review: Claude (different perspective)
- Test: Gemini (different training)

---

## TODO

- [ ] Get Perplexity API key and create skill
- [ ] Evaluate Tavily vs Exa for search augmentation
- [ ] Check MultiOn beta access
- [ ] Investigate GenSpark API availability
- [ ] Add xAI Grok skill (unique X/Twitter access)
- [ ] Benchmark latency and cost across providers

---

*Last updated: 2026-02-02*
