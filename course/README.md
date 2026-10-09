# 🎓 The FDE Field Course

A self-paced course built on top of this roadmap. The roadmap tells you *what* a Forward Deployed Engineer knows; this course is how you **learn it, say it out loud, and use it to move real work forward at your organization**.

Every module has the same four parts:

| Part | What you do | Why |
| :--- | :--- | :--- |
| **Learn** | Read the concepts, explained as mental models, not just definitions | Understand |
| **Lab** | Build or analyze something small on your laptop | Learn by doing |
| **Articulate** | Out-loud drills: 30-second exec version, 2-minute engineer version, push-back answers | Explain it to anyone |
| **Drive it at work** | Apply the module to a real initiative and produce an artifact | Get things moving |

Each module ends with **Check yourself** questions (answers are folded underneath) and **Go deeper** links taken from the main [README](../README.md).

---

## 🗺 Syllabus

About 10–12 weeks at 4–6 hours a week. You can move faster; don't skip the *Drive it at work* sections, because that's where most of the value is.

| # | Module | Theme | Time |
| :-- | :--- | :--- | :--- |
| 0 | [Orientation: Pick Your Mission](00-orientation.md) | Set up your field notebook and choose a real initiative at work to carry through the course | 2 h |
| 1 | [The FDE Mindset & The Delta](01-fde-mindset-and-the-delta.md) | What the role is, and the one concept everything else depends on | 3 h |
| 2 | [Data Foundations](02-data-foundations.md) | SQL, modeling, medallion layers, data quality circuit breakers | 6 h |
| 3 | [Cloud Landing Zones](03-cloud-landing-zones.md) | Identity, networking, perimeters, IaC: where the code lives | 5 h |
| 4 | [Applied AI I: Enterprise RAG](04-enterprise-rag.md) | Ingestion, retrieval, hybrid search, grounding | 6 h |
| 5 | [Applied AI II: Agents & Orchestration](05-agents-and-orchestration.md) | When to use an agent, workflow vs. LLM planning, ADK, A2A | 6 h |
| 6 | [Evals: Proving It Works](06-evals.md) | Golden datasets, the two loops, LLM-as-judge, the RAG triad | 6 h |
| 7 | [Regulated & Disconnected Deployment](07-regulated-and-disconnected.md) | Compliance, supply chain, air gaps, and what they teach any regulated enterprise | 4 h |
| 8 | [Discovery & Diagnosis](08-discovery-and-diagnosis.md) | Three Whys, the discovery checklist, champions, blockers, red flags | 4 h |
| 9 | [Executive Communication & Trust](09-communication-and-trust.md) | Pyramid Principle, MECE, the trust equation, demos as narratives | 4 h |
| 10 | [Scoping & Field Artifacts](10-scoping-and-artifacts.md) | Site Survey, PRD, SOW, MVA, ADRs, the weekly executive summary | 4 h |
| 11 | [Capstone: Drive One Initiative](11-capstone.md) | A 30-day plan, an exec pitch, and a case-study defense | 8 h+ |
| ★ | [Toolkit: Drills, Flashcards & Rubrics](toolkit.md) | Spaced-repetition glossary, articulation drill bank, senior-vs-junior rubric | ongoing |

### Suggested pacing

```
Week 1   ── Module 0 + 1      (pick your mission; that choice shapes the rest)
Week 2-3 ── Module 2          (data is where most FDE projects start)
Week 4   ── Module 3
Week 5-6 ── Module 4 + 5
Week 7   ── Module 6          (do not skip: evals are what make AI work credible)
Week 8   ── Module 7 + 8
Week 9   ── Module 9 + 10
Week 10+ ── Module 11 capstone, run in parallel with real work
Daily    ── 10 min of toolkit flashcards / one articulation drill
```

The soft-skill modules (8–10) are short, but you should start practicing them early. From Week 1, do one *Articulate* drill out loud every day.

---

## ✅ Progress Tracker

Check items off as you go. The course is done when you've shipped the capstone artifacts, not when you've finished reading.

- [ ] **M0** Field notebook created · mission chosen · baseline self-assessment done
- [ ] **M1** "What is an FDE / the Delta" pitch recorded · Delta map for my mission
- [ ] **M2** DuckDB lab done · data audit of my mission's source systems
- [ ] **M3** Landing-zone diagram for my mission · identity & perimeter questions answered
- [ ] **M4** Hybrid-search RAG lab done · retrieval design note for my mission
- [ ] **M5** Workflow-vs-agent lab done · agent decision memo for my mission
- [ ] **M6** Golden dataset (≥25 cases) + eval harness · success metrics agreed with a stakeholder
- [ ] **M7** Compliance & control map for my mission
- [ ] **M8** Discovery interviews held (≥3) · champion/blocker map · red-flag log
- [ ] **M9** One-page Pyramid memo sent · one demo given as a value narrative
- [ ] **M10** Site Survey + Technical PRD + one ADR written
- [ ] **M11** 30-day plan · exec pitch delivered · case-study defense · first Weekly Executive Summary sent
- [ ] **Re-take** the baseline self-assessment and compare

---

## 🧭 How to get the most from this

1. **Pick a real mission in Module 0 and keep it.** All the *Drive it at work* exercises build on one initiative, so by the end you have a complete deployment package for real work instead of 11 unrelated exercises.
2. **Say it out loud.** Reading something doesn't mean you can explain it. Record yourself on your phone, listen back, and cut it down.
3. **Write in your field notebook, not your head.** Use the template in [Module 0](00-orientation.md). It will turn into your Site Survey, PRD, and status reports.
4. **Find a sparring partner.** A peer, your manager, or an AI assistant playing a skeptical CTO. The push-back drills only work if someone actually pushes back.
5. **Translate the vendor names.** The roadmap uses Google Cloud as its reference stack. If your organization runs on AWS, Azure, or on-prem, use the translation table in [Module 3](03-cloud-landing-zones.md). The patterns carry over even when the product names don't.
6. **Product names go out of date quickly.** Several Google Cloud AI products were renamed in 2026 (for example, Vertex AI became Gemini Enterprise Agent Platform). Learn the *pattern*, and check the current product names before you put them in front of an executive.

> *"The FDE's goal is to become obsolete at a client site—because the system you built is so good, it runs itself."*
