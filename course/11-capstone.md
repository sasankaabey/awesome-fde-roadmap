# Module 11 — Capstone: Drive One Initiative

**Time:** 8+ hours, spread over real work · **Outcome:** a complete deployment package for your mission, an exec pitch you've actually delivered, and a case-study defense you can handle under pressure.

[← Module 10](10-scoping-and-artifacts.md) · [Course home](README.md) · [Toolkit →](toolkit.md)

---

## The big idea

Everything so far comes together here. The capstone is **real work**: you'll pitch a 30-day plan for your mission to the people who can say yes, then run it. The course is finished when something has moved at your organization, not when you've read all the modules.

---

## Part 1 — The 30-day plan (2 hours)

Use the roadmap's hospital-readmission case as the shape and replace every line with your mission:

| Days | Technical | Strategy & people |
| :--- | :--- | :--- |
| **1–7: Discovery & trust** | Profile the source data (M2). Confirm system of record. | Define success with the sponsor (M6). Meet the blocker (M8). |
| **8–15: Secure landing zone** | MVA landing zone via IaC inside existing controls (M3, M7). | Start approvals with the longest lead time (M7). |
| **16–25: Build the Delta** | Build the glue: pipeline, retrieval, agent/workflow (M4, M5). Golden-set evals running (M6). | Weekly WES (M10). Co-build with the Day-2 owner. |
| **26–30: Prove value** | Full eval run; compare against baseline. | Put it in front of 5 real users. **If they don't change their behavior, it hasn't worked yet.** Demo as a value narrative (M9). |

For each week, write the **one result** that proves the week succeeded, and the **one risk** most likely to stop it.

---

## Part 2 — The exec pitch (2 hours prep, 10 minutes delivery)

Build a **5-slide (or 1-page) pitch**:

1. **The answer:** what you recommend and what you need (BLUF).
2. **The pain:** cost of inaction, in their numbers (M8).
3. **The plan:** 30-day plan + MVA diagram (M3, Part 1).
4. **The proof:** how success will be measured, which golden set, which thresholds (M6).
5. **The risks & asks:** top three risks, each with an owner and an ask (M7, M10).

**Deliver it** to your sponsor or the decision-maker. Before you go in, write down the three questions you're most afraid of and draft BLUF answers to each.

---

## Part 3 — The case-study defense (90 min, with a partner)

This is the roadmap's FDE interview format, and it's also good preparation for any high-stakes architecture review. Use the **C.A.S.E. framework**:

1. **Clarify:** data volume, sensitivity, definition of done.
2. **Architect:** data flow from source to user, using real primitives.
3. **Solve the Delta:** what doesn't work out of the box and what glue you'll build.
4. **Evaluate:** how you'll prove it isn't hallucinating and how you'll monitor it.

Have a partner (or an AI assistant playing a skeptical interviewer) give you one of these, with 5 minutes to think and 15 minutes to present, while they interrupt with push-back:

- **Case A (roadmap):** a hospital chain wants to predict readmission. 20 years of data in on-prem SQL Server, no cloud presence, extreme HIPAA concerns. Walk through your first 30 days.
- **Case B (roadmap):** a client has 5 PB on-prem and needs it in the cloud warehouse in 48 hours. *(Hint: bandwidth is the bottleneck, so ship a transfer appliance and design schema/partitioning while it's in transit.)*
- **Case C (roadmap):** a bank wants real-time fraud detection (<100 ms) "using an LLM." *(Hint: two tiers. A fast deterministic model makes the decision; an LLM agent writes the asynchronous explanation for the analyst.)*
- **Case D (yours):** your own mission, presented to a skeptical architecture board.

### Scoring rubric: junior vs. senior

| Dimension | Junior answer | Senior answer |
| :--- | :--- | :--- |
| **Clarify** | Jumps to solution | Asks about data, sensitivity, success metric, and Day-2 owner first |
| **Architecture** | Names tools | Explains data flow, identity, network path, and *why* each choice |
| **The Delta** | "The product handles it" | Names the specific gap and the glue, and what could be productized later |
| **AI design** | "Use an LLM / agent" | Picks the lowest sufficient rung; guardrails; human approval on writes |
| **Evaluation** | "We'll test it" | Golden set with business sign-off, metrics with thresholds, drift monitoring |
| **Security & compliance** | Mentioned at the end, if at all | Built into the design: classification, perimeter, least privilege, approvals |
| **Cost** | Not considered | FinOps aware: partitioning, scale-to-zero, model cost per request |
| **People** | Not considered | Champion, blocker, user adoption, Day-2 handover |
| **Communication** | Chronological, technical detail first | BLUF, MECE, ends with a clear ask |

Score yourself 1–3 on each row after every run. Repeat until you're mostly 3s.

---

## Part 4 — Run it and report (ongoing)

- [ ] Execute the 30-day plan. Send the **WES** every week.
- [ ] Keep the **red-flag log** and **ADR** folder current.
- [ ] At day 30, write a one-page **retrospective**: what moved (metrics), what you'd do differently, and what from this mission could be **productized** for the next team (Module 1).
- [ ] Re-take the **baseline self-assessment** from [Module 0](00-orientation.md). Compare the scores.

---

## Capstone completion checklist

- [ ] Field notebook complete (all sections filled)
- [ ] Site Survey · Scoping Doc · ≥2 ADRs · ≥4 WES sent
- [ ] Golden dataset (≥25 cases) signed off by a business owner, with eval results
- [ ] Control map reviewed by someone in security or risk
- [ ] Exec pitch delivered, with the outcome recorded
- [ ] Case-study defense: mostly 3s on the rubric
- [ ] Day-30 retrospective written
- [ ] One thing from your mission proposed for reuse by another team

When every box is checked, you've done the work of a Forward Deployed Engineer. After that, pick the next mission.

> *"The FDE's goal is to become obsolete at a client site—because the system you built is so good, it runs itself."*
