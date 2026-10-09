# Course Labs

Small, laptop-sized labs. Everything uses synthetic data and none of them need cloud accounts or API keys (Module 5's ADK build and Module 6's LLM judge are optional add-ons).

| Lab | Module | Run |
| :--- | :--- | :--- |
| [`m2_data_audit.sql`](m2_data_audit.sql) | [2: Data Foundations](../02-data-foundations.md) | `duckdb m2_lab.duckdb < m2_data_audit.sql` |
| [`m4_hybrid_search.py`](m4_hybrid_search.py) | [4: Enterprise RAG](../04-enterprise-rag.md) | `python m4_hybrid_search.py` |
| [`m6_eval_harness.py`](m6_eval_harness.py) + [`m6_golden.jsonl`](m6_golden.jsonl) | [6: Evals](../06-evals.md) | `python m6_eval_harness.py` |

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

The first run of the Python labs downloads a small embedding model (~90 MB). After that they run offline. Run all commands from this `labs/` folder, since the eval harness imports the Module 4 retrievers.
