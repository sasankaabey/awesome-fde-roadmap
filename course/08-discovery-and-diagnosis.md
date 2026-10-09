# Module 8 — Discovery & Diagnosis

**Time:** ~4 hours (plus the interviews themselves) · **You'll be able to:** run a discovery conversation that gets past the stated ask to the real business pain, map the people who will make or break the project, and spot red flags early.

[← Module 7](07-regulated-and-disconnected.md) · [Course home](README.md) · [Next: Module 9 →](09-communication-and-trust.md)

---

## The big idea

Stakeholders describe solutions ("we need an AI chatbot"), not problems. The FDE's first job is **diagnosis**: find the root pain, the system of record, the cost of doing nothing, and who will own it after you leave. Most failed projects solved the stated ask perfectly and the real problem not at all. Discovery is also when you build the relationships that will carry the project through its first crisis.

---

## Learn

### 1. The Three Whys (the roadmap's diagnostic core)

1. **"What is the system of record?"** Where does the ground-truth data live? If it's a spreadsheet on someone's desktop, the project is already at risk.
2. **"What is the cost of inaction?"** What happens if we *don't* build this? That sets priority and funding. If the answer is "not much," move on.
3. **"What does Day 2 look like?"** Who maintains it after launch? No internal owner means the project will decay.

Then use **"5 Whys"** to drill from symptom to root cause:

> "We need an AI assistant for client questions." → *Why?* "Service reps take too long to answer." → *Why?* "They search five systems." → *Why?* "Client data is split across systems that don't talk." → *Why?* "Nobody owns the integration."
> The root problem is **integration and ownership**. An assistant built on top of five unintegrated systems will be slow and wrong. Maybe the first deliverable is a unified view, and the assistant comes second.

### 2. Discovery question bank

Ask open questions, listen far more than you talk, and write down their exact words.

| Area | Questions |
| :--- | :--- |
| **Pain** | "Walk me through the last time this went wrong." · "What do you do today instead?" · "What does that cost you per week?" |
| **Success** | "If this worked perfectly, what would be different in 90 days?" · "How would you measure it?" · "What number would your boss care about?" |
| **Data** | "Where does that information come from?" · "Who fixes it when it's wrong?" · "Can I see a real example today?" |
| **People** | "Who else cares about this?" · "Who might be nervous about it?" · "Who has tried to solve this before, and what happened?" |
| **Constraints** | "What has to be true for security/risk to say yes?" · "Any deadlines driving this?" · "What's off-limits?" |
| **Day 2** | "Who would own this once it's live?" · "Who gets the call when it breaks at month-end?" |

### 3. The people map

From the roadmap's Discovery Checklist:
- **Champion:** the internal person fighting for the project. Without one, stop.
- **Blocker:** often IT, Security, Legal, or a team that feels threatened. Find them early and bring them in rather than routing around them.
- **Sponsor:** the senior person who funds it and clears escalations.
- **Day-2 owner:** who runs it after launch.
- **Users:** the people whose behavior must change. If they don't change, it failed.

Plot each person by **influence** (low/high) and **attitude** (resistant/neutral/supportive). Your job is to move high-influence people toward supportive, one conversation at a time.

### 4. The hostile stakeholder

From the roadmap's interview blackbook: *"The client's Lead Engineer hates our product and refuses to give you access."* → **That's a trust problem, not a technical one.** Have a 1:1, understand their concerns (often a fear of being replaced or blamed), show how the work removes their grunt work, and **offer them co-authorship**. People rarely sabotage something they helped build.

### 5. The discovery checklist

**Administrative & political**
- [ ] Champion identified
- [ ] Likely blocker identified, and met
- [ ] Success metric agreed (latency? accuracy? hours saved? risk reduced?)

**Data & security**
- [ ] Data classification known
- [ ] Ingestion pattern known (streaming vs. batch)
- [ ] Compliance controls needed (perimeter, DLP masking, residency)

**Infrastructure**
- [ ] Access level confirmed in the target environment
- [ ] Connectivity path known (private network? VPN? interconnect?)
- [ ] Quotas/capacity confirmed (e.g., GPU quota, API rate limits)

### 6. Red flags: escalate immediately

1. **"Data will be ready in 2 weeks."** It never is. Ask for a sample today.
2. **"We don't need a project manager on our side."** The project will lose direction.
3. **"Can we just run this on-prem for now?"** Often signals deep distrust that will block you later. Surface it now.
4. Add your own: *no named Day-2 owner* · *success metric is "it should be good"* · *sponsor is never available* · *"just build what we said."*

---

## Lab — Mock discovery (60 min, with a partner or an AI role-player)

Have a partner (or an AI assistant) play this stakeholder. Give them the hidden brief; you only get the opening line.

> **Opening line (what you hear):** "We need an AI chatbot for our operations team. Can you have something by end of quarter?"
>
> **Hidden brief (for the role-player only):** The real pain is that month-end reconciliation takes 4 people 3 days because two systems disagree on account IDs. The ops lead is skeptical of AI after a failed pilot last year. Data lives in a warehouse plus a shared spreadsheet that one analyst maintains. Nobody has thought about who'd maintain a chatbot. Reveal each fact only if asked a good question.

Run 20 minutes of discovery. Then score yourself:
- [ ] Found the root pain (reconciliation, not "chatbot")
- [ ] Found the system of record *and* the shadow spreadsheet
- [ ] Quantified the cost of inaction (4 people × 3 days × 12 months)
- [ ] Surfaced the failed pilot and the skeptic
- [ ] Asked about Day 2
- [ ] Talked less than 30% of the time

---

## Articulate

**Drill 8.1 — Playback (90 seconds).** After any discovery conversation, play it back: *"What I heard is: the real problem is ___, it costs ___, success looks like ___, and the biggest risk is ___. Did I get that right?"* This is the most useful sentence in consulting, so practice it until it sounds natural.

**Drill 8.2 — Reframe (30 seconds).** Practice redirecting a solution-ask to a problem without making the stakeholder feel wrong:
> *"A chatbot could help. Before we pick the tool, can I understand the moment it would save you the most time? I want to make sure we hit the real bottleneck first."*

**Drill 8.3 — Escalating a red flag (60 seconds),** tactfully, to your sponsor: *"One risk I want on your radar early: ___. If it's not resolved by ___, it'll push ___. What I need from you is ___."*

---

## Drive it at work

- [ ] Hold **at least three discovery conversations** for your mission: the champion/sponsor, a real user, and the likely blocker. Use the question bank.
- [ ] Complete the **people map** (influence × attitude) in **Section 8** of your field notebook.
- [ ] Fill in the discovery checklist and start a **red-flag log** with dates.
- [ ] Send a written **playback** to your sponsor after the conversations (feeds directly into Module 9).
- [ ] Rewrite your mission statement. It has probably changed, and that's a good sign.

---

## Check yourself

<details><summary>1. What are the Three Whys?</summary>
What is the system of record? What is the cost of inaction? What does Day 2 look like?
</details>

<details><summary>2. Why meet the blocker early instead of routing around them?</summary>
Blockers usually have legitimate concerns (security, workload, job risk) and real veto power. Bringing them in early turns objections into design requirements and can turn a blocker into a co-owner.
</details>

<details><summary>3. A stakeholder says "data will be ready in two weeks." What do you do?</summary>
Treat it as a red flag. Ask for a sample today, profile it (Module 2), plan around reality, and log the dependency with an owner and date.
</details>

<details><summary>4. What makes a discovery conversation successful?</summary>
You leave knowing the root pain, the cost of inaction, the system of record, the success metric, the key people, and the Day-2 owner, and the stakeholder feels understood.
</details>

---

## Go deeper

- [The Trusted Advisor](https://trustedadvisor.com/books/the-trusted-advisor): moving from vendor to partner
- [How to Win Friends and Influence People](https://www.amazon.com/How-Win-Friends-Influence-People/dp/0671027034): for resistant IT staff
- [Good Strategy / Bad Strategy](https://www.amazon.com/Good-Strategy-Bad-Strategy-Difference/dp/0307886239): finding the crux
- Roadmap: [The Diagnostic Mindset](../README.md#-the-diagnostic-mindset) · [Discovery Checklist](../README.md#-the-forward-deployment-discovery-checklist) · [Red Flags](../README.md#-red-flags-for-fdes)

[Next: Module 9 — Executive Communication & Trust →](09-communication-and-trust.md)
