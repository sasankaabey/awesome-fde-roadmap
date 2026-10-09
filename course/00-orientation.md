# Module 0 — Orientation: Pick Your Mission

**Time:** ~2 hours · **Outcome:** a field notebook, a chosen mission, and a baseline you can measure yourself against later.

[← Course home](README.md) · [Next: Module 1 →](01-fde-mindset-and-the-delta.md)

---

## The big idea

FDEs learn by being **dropped into a mission**. This course works the same way. Before you study anything, pick one real initiative at your organization, ideally one that's stuck, fuzzy, or politically awkward, and carry it through every module. By Module 11 you'll have a complete deployment package for it: a data audit, an architecture, an eval plan, a stakeholder map, a PRD, and a 30-day plan.

---

## Step 1 — Choose your mission (30 min)

List 3–5 candidate initiatives and score each one 1–5 on these criteria:

| Criterion | Question to ask |
| :--- | :--- |
| **Real pain** | Is someone senior already frustrated that this isn't done? |
| **Data exists** | Is there a system of record you could get read access to within a month? |
| **Delta-shaped** | Is there a gap between what a tool or platform does out of the box and what your organization needs? |
| **Your reach** | Can you influence it from your seat, through access, relationships, or credibility? |
| **30-day win possible** | Could some slice show measurable value in 30 days? |

Pick the highest scorer. If two tie, take the one with the more frustrated sponsor, because frustration gives you leverage.

> **Good missions look like:** "Teams keep asking for an AI assistant over our internal docs and nobody owns it." · "Reporting pipeline X breaks every month-end." · "We bought platform Y a year ago and adoption is weak."
>
> **Weak missions look like:** "Learn Kubernetes." (That's a skill, not a mission.) · "Make everything more efficient." (No system of record, no metric.)

---

## Step 2 — Set up your field notebook (20 min)

Create one document, private to you, and copy in this skeleton. You'll fill in each section as you go through the course.

```markdown
# Field Notebook — [Mission Name]

## 0. Mission statement (one sentence, rewrite it every module)
Enable [who] to [do what] so that [measurable outcome] by [when].

## 1. The Delta (M1)
- What exists today out of the box:
- What the mission actually needs:
- The gap (the Delta):

## 2. Data landscape (M2)
- Systems of record:
- Volumes / freshness / quality issues:

## 3. Landing zone (M3)
- Where it would run, identity model, network path, perimeter:

## 4–6. AI design & evals (M4–M6)
- Retrieval design · agent vs workflow decision · golden dataset location · success metrics:

## 7. Controls (M7)
- Data classification · applicable policies · approvals needed:

## 8. People (M8)
- Champion · Blocker · Sponsor · Day-2 owner · Red-flag log:

## 9–10. Artifacts (M9–M10)
- Links to: Pyramid memo, Site Survey, PRD, ADRs, WES:

## Running log
- YYYY-MM-DD — what I learned / who I talked to / what changed
```

---

## Step 3 — Baseline self-assessment (20 min)

Rate yourself 1–5 (1 = "couldn't explain it," 5 = "could teach it and have done it"). Save the scores in your notebook and re-take this at the end of the course.

| # | Skill | Score now | Score at end |
| :-- | :--- | :---: | :---: |
| 1 | Explain what an FDE is and what "the Delta" means to a non-technical exec | | |
| 2 | Read an `EXPLAIN` plan and spot why a query is slow | | |
| 3 | Design bronze / silver / gold layers for a messy source | | |
| 4 | Sketch a secure landing zone (identity, network, perimeter, IaC) | | |
| 5 | Design a RAG pipeline and explain why hybrid search matters | | |
| 6 | Decide when to use an LLM agent and when to use a deterministic workflow | | |
| 7 | Build a golden dataset and an eval harness; defend a success metric | | |
| 8 | Map compliance/control requirements to architectural choices | | |
| 9 | Run a discovery conversation that gets to the root business pain | | |
| 10 | Write a one-page BLUF memo an exec acts on | | |
| 11 | Write a scope document that holds up against scope creep | | |
| 12 | Present a 30-day plan and defend it under pressure | | |

---

## Step 4 — Read the origin story (30 min)

Read **[Palantir: Dev vs. Delta](https://blog.palantir.com/dev-versus-delta-demystifying-engineering-roles-at-palantir-ad44c2a6e87)**. While you read, note:

- Three things a "Delta" engineer does that a "Dev" engineer doesn't.
- One sentence explaining why the company needs both.

---

## Articulate

**Drill 0.1 — The mission in one breath.** Say your mission statement out loud in under 15 seconds. If you can't, it's too fuzzy, so rewrite it until you can.

**Drill 0.2 — Why you.** In 30 seconds, explain why *you* are a good person to drive this mission. Mention one relationship, one skill, and one piece of access you already have.

---

## Drive it at work

- [ ] Tell one person (your manager or a trusted peer) which mission you picked and why. Ask them: *"Who else cares about this?"* Write the names down; they're your first stakeholder list for Module 8.
- [ ] Book 30 minutes on your calendar every week for the *Drive it at work* sections. Treat them as meetings.

[Next: Module 1 — The FDE Mindset & The Delta →](01-fde-mindset-and-the-delta.md)
