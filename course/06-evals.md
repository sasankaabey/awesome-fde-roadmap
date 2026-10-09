# Module 6 — Evals: Proving It Works

**Time:** ~6 hours · **You'll be able to:** build a golden dataset with stakeholders, write deterministic checks and LLM-as-judge rubrics, compare versions, and defend a success metric to an executive.

[← Module 5](05-agents-and-orchestration.md) · [Course home](README.md) · [Next: Module 7 →](07-regulated-and-disconnected.md)

---

## The big idea

"It seemed good when I tried it" is how AI projects die in enterprise reviews. **Evals turn vibes into evidence.** A shared golden dataset and a repeatable score let you say *"v2 is better than v1 on 47 of 50 real cases, and here are the 3 it got wrong."* That's what gets a risk committee to sign off, a sponsor to keep funding, and a skeptic to stop blocking. For an FDE, evals are as much a **trust-building tool** as a technical one.

---

## Learn

### 1. The golden dataset is a stakeholder artifact

A golden dataset is a set of real inputs with expected outcomes, **agreed with the business**. Building it is the most valuable conversation you'll have, because it forces the definition of "correct" into the open.

A good golden set includes:
- **Real questions** from real users (from your Module 4 collection), not ones you invented.
- **Coverage by category:** lookups, paraphrases, jargon, multi-step, and **out-of-scope questions the system must refuse**.
- **Adversarial cases:** prompt injection, requests for data the user shouldn't see.
- **Expected outcomes** that are checkable: the right source document, required facts, or "should refuse."
- **Owner sign-off:** a named business person who agrees these answers are right.

Start with 25–50 cases. That's enough to catch regressions, and it grows every time production surfaces a new failure.

### 2. The two loops (from the roadmap)

| | Inner loop (dev-time) | Outer loop (production) |
| :--- | :--- | :--- |
| **Purpose** | Fast debugging while building | Prove improvements at scale; catch drift |
| **Size** | Tens of cases, run in seconds | Hundreds to thousands; run in CI and on samples of live traffic |
| **Tools** | `adk eval`, a local harness like this lab | Gemini Enterprise Agent Platform Evals (Rapid / Pipeline), Model Monitoring, CI gates |
| **Trigger** | Every prompt or code change | Every release candidate, model upgrade, and on a schedule |

### 3. What to measure

Use **deterministic checks first**, because they're cheap, exact, and explainable:
- Retrieval hit@k (did the right document come back?)
- Correct citation
- Required facts present / forbidden content absent
- Correct refusal on out-of-scope
- Tool trajectory (did the agent call the right tools in a sensible order?), e.g. ADK's `tool_trajectory_avg_score`
- Latency (p50/p95) and cost per request

**Then add LLM-as-judge** for what code can't check:
- **Pointwise:** score one answer against a rubric. The **RAG triad**: *groundedness* (is every claim supported by the retrieved context?), *relevance/fulfillment* (does it answer the question and follow instructions?), and *coherence*.
- **Pairwise** (successor to AutoSxS): a strong model compares answer A and answer B and picks the better one with reasons. Gives a **win rate**, which is great for "is the new prompt better?"
- **Rules for judges:** a specific rubric, ask for the reasoning *before* the score, use a strong judge model, and **calibrate it against human labels** on 20–30 cases before you trust it.

### 4. Reading results like an FDE

- **Totals hide trade-offs.** A +1 overall can hide that you fixed two things and broke one. Always read the per-case diffs.
- **Slice by category.** "95% overall" with 40% on out-of-scope means it hallucinates when it doesn't know, which is the worst failure for an enterprise.
- **Every production failure becomes a golden case.** That's how the set stays honest.
- **Day 2:** monitor for **drift**. Client data, documents, and question patterns change, and quality decays quietly unless you re-run evals on a schedule.

---

## Lab — Build and break an eval harness (2 hours)

```bash
cd course/labs
python m6_eval_harness.py
```

[`labs/m6_eval_harness.py`](labs/m6_eval_harness.py) runs a 12-case golden set ([`labs/m6_golden.jsonl`](labs/m6_golden.jsonl)) against two versions of a tiny extractive RAG system built on the Module 4 retrievers:

- **v1:** always answers with the top passage.
- **v2:** refuses if retrieval similarity is below a threshold.

You should see something like:

```
== v1 (answers everything, threshold=0.0): 6/12 passed
   out-of-scope  0/2  ...
== v2 (refuses when unsure, threshold=0.35): 7/12 passed
   FAIL g10: refusal_correct
   FAIL g11: refusal_correct
Delta v2 - v1: +1 cases.
```

**Your tasks:**

1. **Read the failures, not the total.** Which cases did v2 fix? Which still fail, and why?
2. **Case g10** ("What is our firm's total AUM this quarter?") isn't refused even in v2. Why? (The glossary entry *about* AUM is a strong semantic match, but it doesn't contain the number.) Explain why a similarity threshold can't catch this, and which RAG-triad metric would.
3. **Write an LLM-as-judge for groundedness.** Add a `judge(question, context, answer)` function that calls any model you have access to with the rubric below, and add `grounded` to the checks. Calibrate it: hand-label 10 outputs yourself and compare.
   ```text
   You are grading whether an ANSWER is fully supported by the CONTEXT.
   QUESTION: {question}
   CONTEXT: {context}
   ANSWER: {answer}
   Step 1: List each factual claim in the ANSWER.
   Step 2: For each claim, quote the CONTEXT sentence that supports it, or write UNSUPPORTED.
   Step 3: Also check: does the ANSWER actually answer the QUESTION? (yes/no)
   Output JSON: {"claims": [...], "grounded": true|false, "answers_question": true|false}
   ```
4. Try thresholds 0.2, 0.3, 0.4, 0.5 and chart pass rate per category. Where's the trade-off between "answers too much" and "refuses too much"? Who at your organization should choose that point? (Hint: not the engineer. The cost of a wrong answer is a business decision.)
5. Add **five cases from your own mission** to `m6_golden.jsonl`, including one adversarial case.

---

## Articulate

**Drill 6.1 — Success metric for an exec (30 seconds):**
> *"We agreed 50 real questions with your team, along with the correct answers. Today the assistant gets 44 right, refuses the 4 it shouldn't answer, and gets 2 wrong, which we're fixing. Every change we make is re-scored against the same 50, so you'll see whether it's getting better or worse, not just hear that it is."*

**Drill 6.2 — "How do you know it's not hallucinating?" (2 minutes).** Cover: groundedness metric, citations, refusal testing, adversarial cases, judge calibration, and drift monitoring.

**Drill 6.3 — Push-back answers:**
- *"Can we just get to 100%?"* → "On which cases, at what cost? Let's agree which error types are unacceptable (say, wrong numbers) and gate on those at 100%, and set realistic targets for the rest."
- *"The demo looked great."* → "Demos are chosen cases. Here's the score on cases your team chose."
- *"Why does an AI grade the AI?"* → "Only for what code can't check, and only after we've confirmed it agrees with human graders on a sample."

---

## Drive it at work

- [ ] Turn your Module 4 question list into a **golden dataset of ≥25 cases**, with categories and expected outcomes.
- [ ] Book 45 minutes with a **business owner** to review and sign off on the expected answers. Watch where they disagree with each other, because that's where the requirements are unclear.
- [ ] Agree **2–3 success metrics with thresholds**, plus one "never" (e.g., *"never states a fund figure not present in the source"*). Write them in your notebook; they go into the PRD in Module 10.
- [ ] Find out how your organization governs model and AI-system validation (model risk, AI governance, or architecture review). Ask what evidence they want to see, and design your eval output to produce it.

---

## Check yourself

<details><summary>1. Why build the golden set with stakeholders rather than alone?</summary>
It forces agreement on what "correct" means, gives the business ownership of the bar, and makes the results credible to them. Disagreements about answers are requirement gaps you want to find early.
</details>

<details><summary>2. Groundedness vs. relevance: what's the difference?</summary>
Groundedness: every claim is supported by the retrieved context (no hallucination). Relevance/fulfillment: the response actually answers the question and follows instructions. An answer can be fully grounded and still useless.
</details>

<details><summary>3. When is pairwise evaluation better than pointwise?</summary>
When comparing two versions (prompt, model, retrieval setting) and absolute scores are noisy. Judges are more reliable at "which is better?" than at assigning calibrated absolute scores.
</details>

<details><summary>4. Your new version scores +3 overall. Ship it?</summary>
Not yet. Check per-category and per-case diffs for regressions, especially in critical categories (refusals, numbers, adversarial). Confirm the change isn't within noise for judge-based metrics.
</details>

---

## Go deeper

- [Anthropic: Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) (required)
- [Gemini Enterprise Agent Platform Evals](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/computation-based-eval-pipeline)
- [Model Monitoring](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview): Day-2 drift detection
- [Eugene Yan's blog](https://eugeneyan.com/): practical writing on evals and LLM-as-judge
- Roadmap: [LLM Systems Evaluation](../README.md#%EF%B8%8F-llm-systems-evaluation-the-success-key)

[Next: Module 7 — Regulated & Disconnected Deployment →](07-regulated-and-disconnected.md)
