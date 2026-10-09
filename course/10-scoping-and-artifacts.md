# Module 10 — Scoping & Field Artifacts

**Time:** ~4 hours · **You'll be able to:** write the documents that define reality, protect scope, record decisions, and prove value: Site Survey, Technical PRD, SOW-style scope, ADR, and the Weekly Executive Summary.

[← Module 9](09-communication-and-trust.md) · [Course home](README.md) · [Next: Module 11 →](11-capstone.md)

---

## The big idea

In the field, **your documentation is your contract.** A good document turns a conversation into a commitment, so nobody can later claim success meant something else. You don't write these for bureaucracy. They protect the project from scope creep, forgotten decisions, and losing the sponsor's attention. Each artifact below answers one question:

| Artifact | Answers | When |
| :--- | :--- | :--- |
| **Site Survey** | "What's the messy reality?" | Week 1 |
| **Technical PRD / Scoping doc** | "What exactly does success look like?" | Week 1–2 |
| **SOW-style scope** | "Where does the work end?" | Before building |
| **MVA** | "What's the simplest thing that proves value?" | Week 2 |
| **ADR** | "Why did we decide this?" | Every significant decision |
| **WES** (Weekly Executive Summary) | "Is this worth continuing?" | Every week |

---

## Learn

### 1. Site Survey (discovery report)

Records the messy reality before you build. It pulls together your notebook sections from Modules 2, 3, 7, and 8.

```markdown
### 🕵️ Site Survey: [Team] - [Mission]
**Date:** YYYY-MM-DD | **Lead:** [Your Name]

#### 1. The Data Landscape (Ground Truth)
- **Source Systems:** [systems of record + shadow IT]
- **Data Gravity:** [volume, growth, residency constraints]
- **Known Quality Issues:** [from your profiling, with numbers]

#### 2. Technical & Security Constraints
- **Identity:** [IdP, how workloads authenticate]
- **Connectivity:** [network path, private access]
- **Controls:** [perimeters, DLP, approvals needed + lead times]

#### 3. The Delta (The Gap)
- **Product/Platform Gap:** [what doesn't work out of the box]
- **Proposed Glue:** [what you'll build]

#### 4. The Quick Win (Week 2 Objective)
- [one measurable result that proves value fast]
```

### 2. Technical Scoping Doc / PRD

Defines success in measurable terms, using the eval metrics from Module 6.

```markdown
### 📐 Technical Scoping Document: [Feature Name]

#### 1. Objective & User Persona
Enable **[user group]** to **[action]** by leveraging **[approach]**.

#### 2. Definition of Success (The Evals)
- **Retrieval:** >90% hit rate @3 on the agreed golden set
- **Quality:** ≥85% pass on golden set; 100% on "never" cases
- **Latency:** p95 < 5 s end to end
- **Adoption:** ≥X weekly active users in the pilot group by week 6

#### 3. Phased Delivery
- **Phase 1 (MVA):** [simplest version]
- **Phase 2 (Scale):** [what's added once Phase 1 proves value]

#### 4. Out of Scope
- [explicitly deferred items, with "deferred to" dates]

#### 5. Day 2
- **Owner:** [named team/person] · **Monitoring:** [what, where] · **Eval cadence:** [weekly]
```

### 3. Scope: your protection against scope creep

Inside an enterprise you may not sign a legal SOW (Statement of Work), but you need its function: **a written fence**. The most important section is **Out of Scope**. When a new request arrives, don't say no. Say *"Great idea. It's not in Phase 1, so I'll add it to the Phase 2 list. Should it replace something in Phase 1?"* That puts the trade-off decision with the stakeholder, where it belongs.

### 4. MVA: Minimum Viable Architecture

The simplest architecture that proves value in under 30 days (e.g., Cloud Run + BigQuery + IAP, inside the existing perimeter). Avoid gold-plating: the **80/20 rule** says find the 20% of features that remove 80% of the pain and build only those first.

### 5. ADR: Architecture Decision Record

A short record of *why* a decision was made, so in six months nobody re-debates it and your successor understands it.

```markdown
# ADR-003: Use hybrid search instead of semantic-only retrieval
**Status:** Accepted · **Date:** YYYY-MM-DD · **Deciders:** [names]

## Context
Users query by policy IDs and internal acronyms. On our golden set, semantic-only
retrieval missed 3/15 ID lookups at top-1.

## Decision
Use hybrid (BM25 + vector) retrieval with reciprocal rank fusion.

## Consequences
+ Robust to IDs and jargon; hit@3 15/15 on golden set.
− Two indexes to maintain; slightly higher latency (+~20 ms).
Revisit if: the managed search service adds native hybrid with equal results.
```

### 6. WES: Weekly Executive Summary

The weekly document that keeps the sponsor engaged and justifies continued investment. BLUF (Module 9) in a fixed format.

```markdown
## 🛰️ Weekly Executive Summary: [Mission]
**Period:** [dates] | **Status:** 🟢 GREEN / 🟡 AMBER / 🔴 RED

#### 🚀 Value Delivered This Week
- **Metric move:** [number, before → after]
- **Milestone:** [what's done]

#### ⚠️ Risks & Blockers
- **Risk:** [what] · **Impact:** [days/$] · **Action required:** [who must do what by when]

#### 🗓️ Next Week / Day-30 Horizon
- [2–3 items]
```

Rules: send it on the same day every week. Lead with a metric. Make every risk carry an ask with an owner. Never let RED be a surprise; it should have been AMBER the week before.

---

## Lab — Write the package (2 hours)

Using your field notebook, write a first draft of:

1. **Site Survey** for your mission
2. **Technical Scoping Doc** with the success metrics from Module 6
3. **Two ADRs:** one technical (e.g., your autonomy-ladder rung from Module 5) and one organizational (e.g., who owns Day 2)
4. **First WES**, even if "value delivered" so far is just discovery findings

Then do a **red-pen review** of each against these questions:
- Could a stranger understand it in 3 minutes?
- Is every success criterion a number?
- Does every risk have an owner and an ask?
- Is "Out of Scope" explicit?

---

## Articulate

**Drill 10.1 — Scope defense (30 seconds).** Practice the scope-creep response out loud until it sounds friendly: *"Love that. It's not in Phase 1, so I'll add it to Phase 2. Should it replace something in Phase 1?"*

**Drill 10.2 — Explaining an ADR (60 seconds).** Walk through one of your ADRs as context → decision → trade-off → when we'd revisit.

**Drill 10.3 — Delivering a RED status (60 seconds).** BLUF, no excuses: *"We're red on ___ because ___. Impact is ___. Here's the recovery plan, and I need ___ from you by ___."*

---

## Drive it at work

- [ ] Share your **Site Survey** and **Scoping Doc** with your sponsor and champion. Ask them to correct anything wrong. Their edits are free discovery.
- [ ] Get explicit agreement on the **success metrics** and **out-of-scope** list (a reply email saying "agreed" is enough).
- [ ] Start sending the **WES** weekly from now on. This habit is one of the clearest signs of an FDE-style operator.
- [ ] Start an `/adr` folder or page for your mission and record decisions as they happen.

---

## Check yourself

<details><summary>1. What's the most important section of a scope document, and why?</summary>
Out of Scope. It makes the boundary explicit, so new requests become visible trade-off decisions instead of silent scope creep.
</details>

<details><summary>2. What makes a success criterion good?</summary>
It's a number with a threshold, measured on an agreed dataset or system, with a named owner who accepts it.
</details>

<details><summary>3. When should you write an ADR?</summary>
Whenever a decision is significant, hard to reverse, or likely to be questioned later: architecture choices, vendor/framework choices, ownership models, and trade-offs you accepted.
</details>

<details><summary>4. Why should RED never be a surprise in a WES?</summary>
Because surprise destroys credibility and reliability (the trust equation). Risks should appear as AMBER with an ask early enough for the sponsor to help.
</details>

---

## Go deeper

- [Architecture Decision Records](https://github.com/joelparkerhenderson/architecture-decision-record): templates and examples
- [Staff Engineer (Will Larson)](https://staffeng.com/book): writing as a leadership tool
- Roadmap: [Artifact Templates (Copy-Paste)](../README.md#-artifact-templates-copy-paste) · [Practical Scoping & Artifacts](../README.md#%EF%B8%8F-practical-scoping--artifacts)

[Next: Module 11 — Capstone →](11-capstone.md)
