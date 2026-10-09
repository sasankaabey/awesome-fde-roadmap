-- Module 2 Lab: Data audit, medallion layers & a circuit breaker in DuckDB.
-- Run with:  duckdb m2_lab.duckdb < m2_data_audit.sql      (CLI)
--       or:  python -c "import duckdb; duckdb.connect('m2_lab.duckdb').execute(open('m2_data_audit.sql').read())"
-- Everything is synthetic, so no client data is needed.

------------------------------------------------------------------------------
-- 0. BRONZE: land the "messy legacy export" exactly as received (immutable)
------------------------------------------------------------------------------
CREATE OR REPLACE TABLE bronze_accounts AS
SELECT
    i AS row_id,
    -- duplicate account ids (~5%) and inconsistent casing/whitespace
    CASE WHEN i % 20 = 0 THEN 'ACC-' || (i - 1) ELSE 'acc-' || i END AS account_id,
    CASE WHEN i % 7 = 0 THEN '  ' || upper('client_' || (i % 300)) || ' '
         ELSE 'client_' || (i % 300) END                                  AS client_name,
    -- 3% missing timestamps, dates stored as text in two formats
    CASE WHEN i % 33 = 0 THEN NULL
         WHEN i % 2 = 0 THEN strftime(DATE '2020-01-01' + (i % 1500)::INT, '%Y-%m-%d')
         ELSE strftime(DATE '2020-01-01' + (i % 1500)::INT, '%d/%m/%Y') END AS opened_on,
    -- balances as text, with a few sentinel values
    CASE WHEN i % 97 = 0 THEN 'N/A'
         WHEN i % 89 = 0 THEN '-999999'
         ELSE CAST(round(random() * 250000, 2) AS VARCHAR) END             AS balance,
    (['US', 'us', 'USA', 'GB', 'UK', 'DE', NULL])[1 + (i % 7)]             AS country
FROM range(1, 10001) t(i);

CREATE OR REPLACE TABLE bronze_transactions AS
SELECT
    j AS txn_id,
    'acc-' || (1 + (j * 7919) % 10000) AS account_id,     -- skewed-ish fan-out
    DATE '2024-01-01' + (j % 365)::INT  AS txn_date,
    round((random() - 0.3) * 5000, 2)   AS amount
FROM range(1, 200001) t(j);

------------------------------------------------------------------------------
-- 1. PROFILE: the first thing you do on day 1 of a data audit
------------------------------------------------------------------------------
SUMMARIZE bronze_accounts;

SELECT
    count(*)                                         AS rows,
    count(DISTINCT lower(trim(account_id)))          AS distinct_accounts,
    count(*) - count(opened_on)                      AS null_opened_on,
    count(*) FILTER (WHERE TRY_CAST(balance AS DOUBLE) IS NULL) AS unparseable_balance,
    count(*) FILTER (WHERE balance = '-999999')      AS sentinel_balance,
    count(*) FILTER (WHERE country IS NULL)          AS null_country
FROM bronze_accounts;

------------------------------------------------------------------------------
-- 2. SILVER: cleaned, typed, de-duplicated, conformed ("single source of truth")
------------------------------------------------------------------------------
CREATE OR REPLACE TABLE silver_accounts AS
WITH typed AS (
    SELECT
        lower(trim(account_id))                                AS account_id,
        lower(trim(client_name))                               AS client_name,
        coalesce(TRY_STRPTIME(opened_on, '%Y-%m-%d'),
                 TRY_STRPTIME(opened_on, '%d/%m/%Y'))::DATE    AS opened_on,
        CASE WHEN balance = '-999999' THEN NULL
             ELSE TRY_CAST(balance AS DECIMAL(14,2)) END       AS balance,
        CASE upper(country) WHEN 'USA' THEN 'US' WHEN 'UK' THEN 'GB'
             ELSE upper(country) END                           AS country,
        row_id
    FROM bronze_accounts
),
ranked AS (   -- window function: keep the latest landed row per account
    SELECT *, row_number() OVER (PARTITION BY account_id ORDER BY row_id DESC) AS rn
    FROM typed
)
SELECT * EXCLUDE (rn, row_id) FROM ranked WHERE rn = 1;

------------------------------------------------------------------------------
-- 3. GOLD: business-ready aggregate that powers a dashboard or an AI tool
------------------------------------------------------------------------------
CREATE OR REPLACE TABLE gold_client_monthly AS
SELECT
    a.client_name,
    date_trunc('month', t.txn_date)  AS month,
    count(*)                         AS txn_count,
    sum(t.amount)                    AS net_flow,
    -- window over an aggregate: running total per client
    sum(sum(t.amount)) OVER (PARTITION BY a.client_name
                             ORDER BY date_trunc('month', t.txn_date)) AS running_net_flow
FROM bronze_transactions t
JOIN silver_accounts a USING (account_id)
GROUP BY a.client_name, date_trunc('month', t.txn_date);

SELECT * FROM gold_client_monthly ORDER BY client_name, month LIMIT 12;

------------------------------------------------------------------------------
-- 4. CIRCUIT BREAKER: fail loudly before a broken table reaches the exec dashboard
------------------------------------------------------------------------------
CREATE OR REPLACE VIEW dq_checks AS
SELECT 'silver_accounts: duplicate keys' AS check_name,
       (SELECT count(*) - count(DISTINCT account_id) FROM silver_accounts) AS failures, 0 AS tolerance
UNION ALL
SELECT 'silver_accounts: null opened_on > 5%',
       (SELECT CASE WHEN avg(CASE WHEN opened_on IS NULL THEN 1 ELSE 0 END) > 0.05 THEN 1 ELSE 0 END FROM silver_accounts), 0
UNION ALL
SELECT 'transactions: orphan account_id',
       (SELECT count(*) FROM bronze_transactions t ANTI JOIN silver_accounts a USING (account_id)), 0;

SELECT *, CASE WHEN failures > tolerance THEN 'FAIL - block publish' ELSE 'PASS' END AS status
FROM dq_checks;

------------------------------------------------------------------------------
-- 5. EXPLAIN: read the plan before you blame the database
------------------------------------------------------------------------------
EXPLAIN
SELECT client_name, sum(net_flow) FROM gold_client_monthly
WHERE month >= DATE '2024-06-01' GROUP BY client_name;
