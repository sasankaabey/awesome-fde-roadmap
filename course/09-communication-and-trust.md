# Module 9 — Executive Communication & Trust

**Time:** ~4 hours · **You'll be able to:** write a one-page memo an executive acts on, structure any messy problem into a clean plan, give a demo that tells a value story, and build the kind of trust that keeps projects alive.

[← Module 8](08-discovery-and-diagnosis.md) · [Course home](README.md) · [Next: Module 10 →](10-scoping-and-artifacts.md)

---

## The big idea

Technical excellence that nobody understands doesn't get funded. Executives have minutes, not hours, and they decide based on **clarity and trust**. An FDE who can say *"Here's the answer, here's why, here's what I need from you"* in 60 seconds will move work forward that a better engineer with a worse explanation can't. This is a skill you can learn, and the only way to learn it is by practicing.

---

## Learn

### 1. The Pyramid Principle (BLUF: bottom line up front)

Start with the answer. Then give 2–4 supporting arguments. Then the data under each argument.

```
                 ┌──────────────────────────────┐
                 │  ANSWER / RECOMMENDATION     │   ← first sentence
                 └──────────────┬───────────────┘
        ┌───────────────────────┼───────────────────────┐
   ┌────┴─────┐            ┌────┴─────┐            ┌────┴─────┐
   │ Reason 1 │            │ Reason 2 │            │ Reason 3 │   ← MECE
   └────┬─────┘            └────┬─────┘            └────┬─────┘
     data/evidence           data/evidence           data/evidence
```

**Engineers usually do the opposite**: background → method → findings → "so, in conclusion…". By that point the executive has stopped listening. Flip it.

> ❌ "We looked at the ingestion logs and found that the upstream export changed format in March, which caused the dedupe step to…"
> ✅ "**We need one decision from you: approve two weeks to fix the source export.** It's causing ~5% of accounts to drop from the month-end report. The fix is small and we have a check in place to catch it until then."

### 2. MECE: Mutually Exclusive, Collectively Exhaustive

Break a problem into parts that **don't overlap** and **cover everything**. That's how you turn "make us more efficient with AI" into a plan without gaps or double-counting.

- Not MECE: "Data issues, the pipeline, quality problems, the dashboard" (overlapping).
- MECE: "**Source** (is the data right when it arrives?) → **Transform** (do we process it correctly?) → **Serve** (do users see it correctly?)."

Useful ready-made MECE splits: *people / process / technology* · *source / transform / serve* · *build / buy / partner* · *now / next / later* · *revenue up / cost down / risk down*.

### 3. The trust equation

From *The Trusted Advisor*:

$$Trust = \frac{Credibility + Reliability + Intimacy}{Self\text{-}Orientation}$$

| Factor | What it means | How an FDE raises it |
| :--- | :--- | :--- |
| **Credibility** | They believe what you say | Get facts right; say "I don't know, I'll find out" |
| **Reliability** | You do what you say | Small promises, kept every time; weekly updates without being asked |
| **Intimacy** | They feel safe telling you things | Confidentiality; listen to the political context without judging |
| **Self-orientation** (divide by) | How much you seem to be about *you* | Focus on their win, not your tool, your architecture, or your credit |

Self-orientation is in the denominator, so it has the largest effect. When you push your favorite technology, it shows.

### 4. The demo is a value narrative, not a feature tour

From the roadmap: show **how the data moves from their messy reality into a clean insight**. Structure:
1. **Their pain, in their words:** "Today, month-end takes 4 people 3 days."
2. **The before:** show the messy reality (the actual spreadsheet, the actual 5 systems).
3. **The after:** one real task, done end-to-end with *their* data.
4. **The proof:** eval results (Module 6). "47 of 50 of your team's questions."
5. **The ask:** what you need to go to the next stage.

Rules: use their data, not toy data. Rehearse failure paths. Show a refusal ("it says 'I don't know' when the documents don't cover it"); it builds more trust than a perfect run.

### 5. The Delta concept, as a communication frame

When an exec asks "why can't we just buy X?", answer with the Delta: *"X does 80% out of the box. The remaining 20% — our data, our controls, our workflows — is where the value and the risk are. That's what we're building."*

---

## Lab — Rewrite into a pyramid (60 min)

**Part A.** Rewrite this status update as a 5-sentence BLUF memo:

> "So this week we continued working on the ingestion layer. We had some problems with the VPN because the network team needed a change ticket, which took a few days. Meanwhile we profiled the data and found some issues with duplicates in about 5% of records which we think comes from the source system. We also got the first version of the retrieval working and tested it on some questions, and it seems pretty good, about 85% of questions found the right document. Next week we hope to finish the VPN and start on the evaluation. One concern is that we still don't know who will own this after launch."

<details><summary>One good rewrite</summary>

**Status: on track for the pilot, with one decision needed from you: name a Day-2 owner by the 15th.**
- **Value:** retrieval finds the right document for 85% of real user questions (target: 90%).
- **Risk:** a 5% duplicate-ID problem in the source system; a data-quality check is in place so it can't reach users.
- **Blocker cleared:** network access approved after a change ticket (3-day delay absorbed).
- **Next week:** connect the live source and run the full evaluation against the agreed 50 questions.
</details>

**Part B.** Take one sprawling problem at work and break it into a **MECE tree** three levels deep. Check every branch: do any overlap? Is anything missing?

**Part C.** Record a 3-minute demo script of your mission using the five-step value narrative, even if the "after" is just a mock-up.

---

## Articulate

**Drill 9.1 — The elevator BLUF (30 seconds).** Pick any project. State the answer first, three reasons, and the ask. Time yourself.

**Drill 9.2 — The "so what?" ladder.** Say any technical fact, then ask "so what?" three times until you reach a business outcome.
> "We added hybrid search." → so what? → "It finds documents by policy ID." → so what? → "Reps stop escalating ID lookups to compliance." → so what? → "**~6 hours/week back for compliance and faster client answers.**"

**Drill 9.3 — Hard questions from an exec**, answered in BLUF:
- "Is this going to work?" → "On the 50 cases your team picked, it's at 88% today. The remaining risk is ___, and we'll know by ___."
- "Why is it taking so long?" → "Two weeks of the delay are waiting on ___. I need your help with ___ to recover it."
- "What would you do if it were your money?" → Give a straight recommendation. Hedging lowers credibility.

---

## Drive it at work

- [ ] Send your sponsor a **one-page BLUF memo** on your mission: recommendation, three MECE reasons, the ask. Note the response time and what they asked about.
- [ ] Give one **demo as a value narrative** (even a 5-minute one to your team). Ask for feedback on clarity, not on the technology.
- [ ] Score yourself on the trust equation with each key stakeholder from your people map. Pick the lowest factor for the most important person and plan one action to raise it.

---

## Check yourself

<details><summary>1. What does BLUF stand for, and why does it work with executives?</summary>
Bottom Line Up Front. Executives have limited attention and decide quickly; leading with the answer and the ask lets them act even if they stop reading after one sentence.
</details>

<details><summary>2. Is "Cost, Speed, Quality, Data issues" a MECE breakdown?</summary>
No. "Data issues" overlaps with the others (bad data affects quality, cost, and speed). Pick one dimension for splitting, e.g., source / transform / serve.
</details>

<details><summary>3. Which factor of the trust equation matters most, and why?</summary>
Self-orientation, because it's the denominator: high self-interest undermines even high credibility and reliability.
</details>

<details><summary>4. Why show a refusal in a demo?</summary>
It shows the system knows its limits, which is what risk-aware stakeholders actually worry about. That builds more trust than a flawless run.
</details>

---

## Go deeper

- [The Pyramid Principle (summary)](https://medium.com/lessons-from-mckinsey/the-pyramid-principle-f0885dd3c5c7) (required) · [the book (Barbara Minto)](https://www.amazon.com/Pyramid-Principle-Logic-Writing-Thinking/dp/0273710516)
- [The MECE Principle](https://en.wikipedia.org/wiki/MECE_principle)
- [The Trusted Advisor](https://trustedadvisor.com/books/the-trusted-advisor)
- [The McKinsey Way](https://www.amazon.com/McKinsey-Way-Ethan-M-Rasiel/dp/0070534489)
- Roadmap: [Strategic Frameworks](../README.md#-strategic-frameworks)

[Next: Module 10 — Scoping & Field Artifacts →](10-scoping-and-artifacts.md)
