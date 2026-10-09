# ★ Toolkit: Drills, Flashcards & Rubrics

Reference material to use daily throughout the course. Ten minutes a day here does more for your ability to *explain* things than anything else in the course.

[Course home](README.md)

---

## 1. Daily routine (10 minutes)

1. **5 flashcards** from section 2. Say the answer out loud *before* revealing it.
2. **1 articulation drill** from section 3, recorded on your phone. Listen back once.
3. **1 line** in your field notebook's running log.

---

## 2. Flashcards

Cover the right column. Say the answer aloud, then check. Mark the ones you miss and repeat them tomorrow.

### Foundations
| Prompt | Answer |
| :--- | :--- |
| The Delta | The gap between what a product does out of the box and what a specific organization needs to get value. Four layers: data, integration, environment, organization. |
| Productized consulting | Solving one site's problem in a way that can be generalized back into the product |
| Embedded engineering | Having credentials, sitting in the team's channels, and shipping to production, not just advising |
| Last-mile integration | Connecting a modern platform to legacy, undocumented systems |
| System of record | The authoritative source for a piece of data |
| Shadow IT | Unofficial tools/databases teams actually rely on; often where the useful data is |
| Day 2 operations | Everything after launch: monitoring, retraining, support, ownership |

### Data & cloud
| Prompt | Answer |
| :--- | :--- |
| Bronze / Silver / Gold | Raw & immutable / cleaned single source of truth / business-ready aggregates |
| Why keep bronze immutable? | So you can rebuild after discovering your cleaning logic was wrong, and keep an audit trail |
| Star schema vs OBT | Fact + dimensions (flexible) vs one wide pre-joined table (simple, fast for one use) |
| Data skew | One key holds a disproportionate share of rows, so one worker does most of the work |
| Data circuit breaker | Automated check that blocks publication when data looks wrong |
| Partitioning vs clustering | Prune whole chunks (usually by date) vs co-locate rows by key within them |
| Workload identity | Platform-attested identity for workloads; no long-lived keys |
| VPC Service Controls | Perimeter preventing data exfiltration even with valid credentials |
| IAP | Zero-trust access to internal apps by identity, without VPN |
| MVA | Minimum Viable Architecture: simplest design that proves value in < 30 days |
| Why Terraform builds trust | Produces a reviewable, diffable artifact security can approve |

### Applied AI
| Prompt | Answer |
| :--- | :--- |
| RAG | Retrieve relevant passages, then generate an answer grounded only in them, with citations |
| Hybrid search | Keyword (BM25) + semantic (vector) retrieval, fused (e.g., RRF) |
| Why keyword search still matters | IDs, codes, acronyms, and jargon carry little "meaning" for embedding models |
| Where to enforce document ACLs | At retrieval time, as a filter, never after generation |
| ReAct | Reason → Act (tool call) → Observe → repeat |
| Workflow agent (ADK) | Deterministic Sequential/Parallel/Loop control of sub-agents, no LLM routing |
| A2A protocol | Open HTTP-based standard for agents across systems to discover each other and exchange tasks |
| Autonomy ladder | Rules → single call → RAG → workflow w/ LLM steps → agent → multi-agent; climb only as needed |
| Golden dataset | Real inputs with expected outcomes, signed off by the business |
| RAG triad | Groundedness, relevance/fulfillment, coherence |
| Pairwise vs pointwise eval | Compare two outputs (win rate) vs score one output against a rubric |
| Inner vs outer eval loop | Fast dev-time debugging vs scaled, automated evaluation in CI and production |
| Drift | Quality decay as data and usage change; caught by scheduled evals and monitoring |

### Regulated environments
| Prompt | Answer |
| :--- | :--- |
| ATO | Formal sign-off accepting a system's risk before production (enterprise analog: review boards) |
| STIG | Line-by-line hardening checklist (enterprise analog: CIS benchmarks, golden images) |
| Why safetensors over pickle | Pickle can execute code on load |
| Image signing + admission control | Only images from the trusted pipeline can run |
| Data diode / CDS | Strictly one-way or mediated data movement between trust levels |

### Consulting & communication
| Prompt | Answer |
| :--- | :--- |
| The Three Whys | System of record? Cost of inaction? What does Day 2 look like? |
| BLUF | Bottom Line Up Front: answer, then reasons, then data |
| MECE | Mutually Exclusive, Collectively Exhaustive |
| Trust equation | (Credibility + Reliability + Intimacy) / Self-orientation |
| C.A.S.E. | Clarify, Architect, Solve the Delta, Evaluate |
| Cost of inaction | Quantified loss from *not* doing the project |
| SOW's most important section | Out of Scope |
| ADR | Short record of a decision: context, decision, consequences |
| WES | Weekly Executive Summary: value, risks with asks, next steps |
| Classic red flags | "Data ready in 2 weeks" · "no PM needed" · "just run it on-prem for now" |

---

## 3. Articulation drill bank

Pick one per day. Use the format given and keep to the time limit.

| # | Prompt | Audience | Time |
| :-- | :--- | :--- | :--- |
| 1 | What is an FDE, and why does our organization need that way of working? | Exec | 30 s |
| 2 | What's the Delta on my mission? | Engineer | 2 min |
| 3 | Why can't we just point the AI at our data? | Exec | 30 s |
| 4 | Medallion architecture and why bronze is immutable | Engineer | 2 min |
| 5 | Walk through the landing zone (classification → identity → network → perimeter → audit → IaC) | Security architect | 60 s |
| 6 | What is RAG, explained with the librarian metaphor | Exec | 30 s |
| 7 | Why hybrid search? (use the lab's evidence) | Engineer | 2 min |
| 8 | Should we build an agent for this? (autonomy ladder) | Product owner | 60 s |
| 9 | How do you know it's not hallucinating? | Risk partner | 2 min |
| 10 | Here's our success metric and how we measure it | Sponsor | 30 s |
| 11 | Compliance is built in, not bolted on | Exec | 30 s |
| 12 | Playback after a discovery conversation | Stakeholder | 90 s |
| 13 | Reframe a "build me a chatbot" request toward the real problem | Requester | 30 s |
| 14 | Defend scope against a new request, kindly | Stakeholder | 30 s |
| 15 | Deliver a RED status with a recovery plan | Sponsor | 60 s |
| 16 | The "so what?" ladder on a technical win | Exec | 45 s |
| 17 | Why we chose X (walk through an ADR) | New team member | 60 s |
| 18 | My 30-day plan | Decision-maker | 3 min |

**Self-review after each recording:**
- [ ] Did the first sentence contain the answer?
- [ ] Any jargon the audience wouldn't know?
- [ ] Was there a number?
- [ ] Was there an ask (if appropriate)?
- [ ] Could I cut 20%?

---

## 4. Push-back bank

The objections you'll hear most at work, with the shape of a good answer.

| Objection | Shape of a strong answer |
| :--- | :--- |
| "Isn't this just consulting?" | Embedded, ships to production, owns outcomes, and feeds learnings back into the platform |
| "Just fine-tune a model on our docs." | Fine-tuning teaches style, not reliable facts; can't cite, can't respect permissions, goes stale. Use RAG. |
| "The vendor says 95% accuracy." | "On what data? Let's run it on our golden set." |
| "Let's build a multi-agent swarm." | "What does each extra agent do that a function can't? Each one adds latency, cost, and failure modes." |
| "Can it take the action automatically?" | "Once evals show X% on real cases and we've agreed what an error costs. Until then, a human approves." |
| "Security will never approve this." | "What exactly would they object to? Let's ask them now and design for it." |
| "Just give it Editor so it works." | Least privilege = smaller blast radius if compromised |
| "Can we run it on-prem for now?" | Find the underlying concern (residency? cost? trust?) and address that directly |
| "Data will be ready in two weeks." | "Great. Can I see a sample today so we can plan around reality?" |
| "Can we just get to 100%?" | Gate the unacceptable error types at 100%; set realistic targets elsewhere |
| "Why is it taking so long?" | BLUF: what's blocking, what you're doing, what you need from them |
| "The demo looked great." | "Demos are chosen cases. Here's the score on cases your team chose." |

---

## 5. Field notebook prompts (weekly reflection)

- What did I learn about the *organization* this week, not just the technology?
- Whose trust went up or down, and why?
- What's the riskiest assumption in my plan right now? How could I test it this week?
- What did I build or learn that another team could reuse?
- What would I tell myself from four weeks ago?
