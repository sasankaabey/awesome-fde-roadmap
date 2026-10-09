# Module 1 — The FDE Mindset & The Delta

**Time:** ~3 hours · **You'll be able to:** explain the FDE role and "the Delta" to anyone, and map the Delta for your own mission.

[← Module 0](00-orientation.md) · [Course home](README.md) · [Next: Module 2 →](02-data-foundations.md)

---

## The big idea

Products are built for the average customer, and no real customer is average. The **Delta** is the gap between what a product does out of the box and what one specific organization needs before it gets real value. FDEs are the engineers who close that gap: with code, with architecture, and just as often with conversations.

---

## Learn

### 1. Mission over persona

A traditional software engineer builds for a *user persona*: millions of anonymous users in a controlled environment. An FDE builds for a *mission*: a few high-stakes stakeholders in an environment that is legacy, hostile, hybrid, or disconnected.

| | Software Engineer | Forward Deployed Engineer |
| :--- | :--- | :--- |
| **User** | Millions of anonymous users | A handful of high-stakes stakeholders |
| **Environment** | Controlled, uniform cloud | Legacy, hybrid, locked-down, sometimes air-gapped |
| **Goal** | Scale and stability | Speed-to-value and problem-solving |
| **Work mix** | ~90% features | ~50% integration/glue, ~50% strategy |

**Mental model:** a SWE optimizes the *product*, while an FDE optimizes the *outcome at one site*. Neither is better; the company needs both, and the FDE feeds what they learn in the field back to the product team.

### 2. The Delta, decomposed

The Delta is never only technical. In practice it has four layers, so learn to list all four:

| Layer | Example gap | Typical FDE move |
| :--- | :--- | :--- |
| **Data** | Product expects clean, keyed records; site has 20-year-old schemas with no primary keys | Data audit, cleaning pipeline, entity resolution |
| **Integration** | Product speaks REST/JSON; site has SFTP drops, a mainframe, and a SharePoint | Glue services, adapters, event bridges |
| **Environment** | Product assumes public cloud; site has private networks, perimeters, approval gates | Landing zone, private deployment, offline packaging |
| **Organization** | Product assumes someone owns it; site has no owner, a skeptical IT team, an unclear metric | Champion-building, success metrics, Day-2 handover |

Most failed deployments solved the first two layers and ignored the last two.

### 3. Productized consulting

An FDE solves one customer's problem *in a way that can be generalized*. The glue you write at site #1 should become a feature, connector, or template by site #3. That's the difference between an FDE and a contractor: the contractor's work stays at one site, while the FDE's work makes the product better for everyone.

**Inside an enterprise like yours**, "the product" might be an internal platform, a vendor tool your organization bought, or a shared AI capability. "Sites" are the business teams adopting it. The same logic applies: solve it for team #1, generalize for team #3.

### 4. Embedded, not advisory

A consultant tells you what to do. An FDE has credentials, sits in your channels, and ships to production. That gives you credibility, and it also means you're accountable for what you ship. Day 2 (who runs it after you leave) is part of your job from day 1.

### 5. The stack, briefly

The roadmap's "Modern FDE Stack" is `Python` + `SQL` + `Go`; `dbt` / `DuckDB` / `Spark`; `Terraform` / `Helm` / a cloud; `Prometheus` / `Grafana` / `Loki`. Don't try to master all of it now. The rest of the course covers each piece at the depth an FDE needs: enough to diagnose, design, and ship the glue.

---

## Lab — Delta teardown of a real case (60 min)

Pick one case study from the roadmap:

- [Palantir & UK NHS (COVID-19)](https://www.palantir.com/uk/healthcare/)
- [OpenAI & Morgan Stanley](https://openai.com/customer-stories/morgan-stanley)
- [Scale AI & the US Army](https://scale.com/blog/scale-ai-dod-expand-army-rd-partnership)

Read it and fill in this table:

| Layer | What the product provided | What the site needed | How the gap was (probably) closed |
| :--- | :--- | :--- | :--- |
| Data | | | |
| Integration | | | |
| Environment | | | |
| Organization | | | |

Then answer: *Which part of the Delta work could the vendor productize for the next customer?*

---

## Articulate

**Drill 1.1 — "What's an FDE?" (30 seconds, for an exec)**
> Template: *"Products are built for the average customer; we aren't average. An FDE is an engineer who embeds with a team and closes the gap — data, integration, environment, and people — between what a tool does out of the box and what we actually need. They're measured on outcomes, not features."*

Make it your own. Record it, play it back, and cut 20%.

**Drill 1.2 — "What's the Delta on X?" (2 minutes, for an engineer)**
Take your mission and walk through the four layers out loud. Finish with: *"The riskiest layer is ___ because ___."*

**Drill 1.3 — Push-back answers.** Practice an answer to each:
- *"Isn't that just a solutions engineer / consultant?"* → (Hint: embedded, ships to production, owns outcomes, feeds back to the product.)
- *"Why not just make the product better instead?"* → (Hint: you can't know what to generalize until you've solved it in the field. The Delta work is how the product learns.)
- *"Why does this need an engineer and not a project manager?"* → (Hint: most of the gap is data and integration work, and someone has to write the glue.)

---

## Drive it at work

- [ ] Fill in **Section 1 (The Delta)** of your field notebook using the four-layer table.
- [ ] Identify which layer is the **riskiest** and which is the **cheapest to close**. These are often different, and the cheapest one is usually your first quick win.
- [ ] Rewrite your one-sentence mission statement.

---

## Check yourself

<details><summary>1. Name the four layers of the Delta and give one example of each.</summary>

Data (dirty or unkeyed source records), Integration (legacy interfaces like SFTP or a mainframe), Environment (private networks, perimeters, approvals), Organization (no owner, skeptical IT, undefined metric).
</details>

<details><summary>2. What separates an FDE from a contractor?</summary>

Productized consulting: an FDE solves the problem in a way that can be generalized back into the product, so the next deployment is easier. A contractor's work stays at the one site.
</details>

<details><summary>3. Why is "Day 2" an FDE concern from Day 1?</summary>

If nobody inside the organization can own and run the system after the FDE leaves, it decays and the value disappears. Ownership, monitoring, and handover have to be designed in from the start, not added at the end.
</details>

<details><summary>4. The roadmap says FDE work is ~50% glue, ~50% strategy. What does "strategy" mean in practice?</summary>

Defining success metrics, scoping (what's in and out), managing stakeholders, building trust with skeptical teams, and turning vague asks into concrete technical requirements.
</details>

---

## Go deeper

- [Palantir: Dev vs. Delta](https://blog.palantir.com/dev-versus-delta-demystifying-engineering-roles-at-palantir-ad44c2a6e87) (required)
- [OpenAI: Customer Stories](https://openai.com/customer-stories): skim three and spot the Delta in each
- [Staff Engineer (Will Larson)](https://staffeng.com/book): FDE scope often looks like staff-plus scope
- Roadmap: [The FDE Persona & Mission](../README.md#-the-fde-persona--mission) · [Glossary: Foundational Concepts](../README.md#-the-fde-glossary)

[Next: Module 2 — Data Foundations →](02-data-foundations.md)
