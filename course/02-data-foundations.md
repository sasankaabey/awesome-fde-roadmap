# Module 2 — Data Foundations

**Time:** ~6 hours · **You'll be able to:** audit a messy source, design bronze/silver/gold layers, write the SQL that FDEs live in, and stop bad data before an executive sees it.

[← Module 1](01-fde-mindset-and-the-delta.md) · [Course home](README.md) · [Next: Module 3 →](03-cloud-landing-zones.md)

---

## The big idea

Almost every FDE mission starts with a **data audit**, and most AI projects that fail do so because of data, not models. If you can't untangle a 20-year-old schema, you can't build anything reliable on top of it. Your job is to find the **system of record**, measure how bad things are, and build a pipeline that tells you when it breaks *before* your stakeholder notices.

---

## Learn

### 1. System of record first

For every field your mission needs, ask: *where is the authoritative version?* (Finance → the ledger. Client data → the CRM. Not "the extract Dave emails on Mondays.") Building on a stale copy is the most common silent failure in enterprise data work. **Shadow IT**, the rogue spreadsheet or Access database a team actually relies on, is often where the useful data lives. Find it, respect it, and plan a path to make it official.

### 2. The medallion architecture

| Layer | Contains | Rule | Who reads it |
| :--- | :--- | :--- | :--- |
| **Bronze** | Raw data exactly as landed | Immutable, append-only. Never "fix" bronze. | Engineers, for replay and audit |
| **Silver** | Typed, cleaned, de-duplicated, conformed | One row per real-world entity. This is your single source of truth. | Engineers, analysts, AI retrieval |
| **Gold** | Business-ready aggregates and features | Shaped for one use case (a dashboard, an agent tool) | Executives, apps, agents |

**Why bother with three layers?** Because you *will* get the cleaning logic wrong, and the lab below shows it happening. Keeping bronze immutable means you can fix the silver logic and rebuild everything without asking the client for the data again.

### 3. Modeling: Star schema vs. One Big Table

- **Star schema:** a fact table (events: transactions, trades, visits) surrounded by dimension tables (who, what, when, where). Flexible, avoids duplicated data, and scales across many questions.
- **One Big Table (OBT):** pre-joined and wide. Fast and simple for one use case, and convenient for LLM tools because one table is easier for a model to query correctly.
- **The FDE answer:** a star schema in silver/gold for flexibility, plus purpose-built OBTs in gold for specific dashboards or agent tools. Weigh write performance against how easily people (and models) can read it.

### 4. SQL beyond JOINs

The three things the roadmap calls out, and why they matter in the field:

- **Window functions** (`ROW_NUMBER`, `LAG`, running `SUM ... OVER`): de-duplication ("keep the latest row per key"), time-series deltas, running totals. You'll use them weekly.
- **Recursive CTEs:** walking hierarchies such as org charts, account parent/child structures, and bills of materials.
- **Reading `EXPLAIN`:** before you blame the database, read the plan. Look for full scans where you expected a filter, joins that blow up row counts, and filters applied *after* a join instead of pushed down before it. On cloud warehouses, **partitioning** (prune whole chunks by date) and **clustering** (co-locate rows by a key) usually decide whether a query scans 10 GB or 10 TB, and that difference shows up directly in the bill.

### 5. Distributed computing: just enough

When data doesn't fit on one machine (Spark, Ray, BigQuery), two failure modes come up most:
- **Data skew:** one key (say, the largest client) holds 40% of rows, so one worker does 40% of the work while the others sit idle. Fixes: salting the key, broadcast joins for small tables, pre-aggregation.
- **OOM (out of memory):** usually a skewed join, an unbounded `collect()`, or too few partitions.

You don't need to be a Spark expert. You do need to recognize these two and know what to ask for.

### 6. Data quality circuit breakers

A **circuit breaker** is an automated check that *blocks publication* when data looks wrong: duplicate keys, too many nulls, orphan foreign keys, a row count that dropped 50% overnight, freshness older than X hours. If upstream breaks, the pipeline should alert you and stop, so the executive dashboard shows "data delayed" instead of a wrong number. One wrong number in front of a CEO costs more trust than a week of delays.

---

## Lab — Audit a messy legacy export (90 min)

Everything is synthetic and runs on your laptop.

```bash
pip install duckdb            # or: brew install duckdb
cd course/labs
duckdb m2_lab.duckdb < m2_data_audit.sql
```

The script, [`labs/m2_data_audit.sql`](labs/m2_data_audit.sql), builds a "legacy" accounts export with realistic problems (inconsistent casing, two date formats, sentinel values like `-999999`, `N/A` balances, `USA` vs `US`), then walks through **profile → bronze → silver → gold → circuit breaker → EXPLAIN**.

**Your tasks:**

1. Run it and read the profiling output. Write down in your own words each data-quality problem it found.
2. One circuit-breaker check **fails**. Before reading the answer below, work out *why*. Hint: compare row counts in bronze and silver, then look at how `account_id` is generated for every 20th row.
3. Fix the silver logic so the check passes *for the right reason*. (Deleting the check doesn't count.)
4. Add two checks of your own: a **freshness** check (max `txn_date` within N days of today) and a **volume** check (row count within ±20% of an expected value).
5. Run the `EXPLAIN`, find the scan and the aggregation in the plan, and explain them out loud.
6. Stretch: write a recursive CTE that walks a small parent/child account hierarchy you create yourself.

<details><summary>Why does the orphan check fail?</summary>

Every 20th row is keyed `ACC-(i-1)` instead of `acc-i`. It looks like a duplicate of the previous account, so the de-dup step "helpfully" collapses it, and accounts `acc-20`, `acc-40`, … disappear from silver. Their transactions become orphans.

**The lesson:** what looks like a duplicate is sometimes a *keying error*. De-duplication is a business decision, not a cleanup step. In the field you'd take this to the data owner ("we see ~5% of IDs that appear to be off-by-one — which is right?") before deciding the rule. Bronze is untouched, so you can rebuild once they answer.
</details>

---

## Articulate

**Drill 2.1 — "Why can't we just point the AI at the data?" (30 seconds, exec)**
> *"We can, and it'll confidently give wrong answers, because about X% of the source records have problems like duplicate IDs and missing dates. We're putting a cleaning layer in front with automated checks, so if the source breaks, the dashboard says 'delayed' instead of showing a wrong number."*

**Drill 2.2 — Medallion in 2 minutes (engineer).** Explain bronze/silver/gold and give a concrete reason for keeping bronze immutable, using the orphan-key story from the lab.

**Drill 2.3 — Push-back answers:**
- *"That's over-engineered, just clean it in the dashboard."* → Cleaning logic duplicated across tools drifts apart, there's no audit trail, and the AI and the dashboard end up disagreeing.
- *"The data will be ready in two weeks."* → (Roadmap red flag: it never is.) Ask for a sample *today* and profile it. Plan around what you find, not what was promised.

---

## Drive it at work

- [ ] For your mission, list every **system of record** and name its **owner**. Mark any shadow-IT sources.
- [ ] Get read access to a **sample** of the key source, even 1,000 rows, and run the lab's profiling query pattern on it. Record what you find in **Section 2** of your field notebook.
- [ ] Draft a bronze/silver/gold sketch for your mission: tables, keys, and the 3–5 circuit breakers that matter most.
- [ ] Find the one data-quality issue that would most embarrass the sponsor if it reached them. That's your first circuit breaker.

---

## Check yourself

<details><summary>1. Why keep bronze immutable?</summary>
So you can rebuild silver and gold after you discover your cleaning logic was wrong, without re-requesting data, and so you have an audit trail of exactly what the source sent.
</details>

<details><summary>2. A BigQuery query over a 5-year table filtered to last week costs as much as a full scan. What's the likely cause and the fix?</summary>
The table isn't partitioned by date, or the filter isn't on the partition column (or wraps it in a function that prevents pruning). Partition on the date column, filter on it directly, and consider clustering by the most common filter or join key.
</details>

<details><summary>3. One Spark task runs 50× longer than the others. What do you suspect?</summary>
Data skew: one key holds a disproportionate share of rows. Check key distribution, then salt the key, broadcast the small side of the join, or pre-aggregate.
</details>

<details><summary>4. Name five circuit-breaker checks.</summary>
Uniqueness of keys, null-rate thresholds, referential integrity (orphans), freshness (max timestamp), volume (row count vs. expected), plus value ranges and accepted-values lists.
</details>

---

## Go deeper

- [Select Star SQL](https://selectstarsql.com/): interactive SQL practice on real data (required if your SQL is rusty)
- [DuckDB docs](https://duckdb.org/docs/): your local analysis workhorse
- [dbt Fundamentals](https://courses.getdbt.com/courses/fundamentals): turns the lab's pattern into a maintainable, tested project
- [Designing Data-Intensive Applications](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/): ch. 1–3 now; the rest over the course
- [BigQuery performance best practices](https://docs.cloud.google.com/bigquery/docs/best-practices-performance-overview)
- Roadmap: [Phase 1: Data Engineering](../README.md#phase-1-data-engineering-the-bedrock)

[Next: Module 3 — Cloud Landing Zones →](03-cloud-landing-zones.md)
