"""Module 6 Lab: a minimal eval harness — golden set, deterministic checks, A/B compare.

    pip install rank_bm25 sentence-transformers
    python m6_eval_harness.py

The "system under test" is a tiny extractive RAG built on the Module 4 retrievers:
it returns the best passage if retrieval looks confident, otherwise refuses.
Swap `answer()` for your real system (an API call, an ADK agent, a vendor tool);
the harness doesn't care what's behind it.
"""
import json
import time

from m4_hybrid_search import DOCS, doc_vecs, hybrid, model

REFUSAL = "I don't know based on the approved documents."


def make_system(threshold):
    """Version knob: the minimum similarity required before we answer."""
    def answer(question):
        top_ids = hybrid(question, k=3)
        best = top_ids[0]
        sim = float(doc_vecs[list(DOCS).index(best)] @ model.encode([question], normalize_embeddings=True)[0])
        if sim < threshold:
            return {"answer": REFUSAL, "retrieved": top_ids, "citation": None}
        return {"answer": DOCS[best], "retrieved": top_ids, "citation": best}
    return answer


def score(case, out):
    """Deterministic, explainable checks. Add an LLM judge only for what these can't see."""
    should_refuse = case["expected_doc"] is None
    refused = out["answer"] == REFUSAL
    checks = {"refusal_correct": refused == should_refuse}
    if not should_refuse:
        checks["retrieval_hit@3"] = case["expected_doc"] in out["retrieved"]
        checks["cited_correct_doc"] = out["citation"] == case["expected_doc"]
        checks["contains_facts"] = all(f.lower() in out["answer"].lower() for f in case["must_include"])
    return checks


def run(system, golden):
    results = []
    for case in golden:
        t0 = time.perf_counter()
        out = system(case["question"])
        latency_ms = (time.perf_counter() - t0) * 1000
        checks = score(case, out)
        results.append({"id": case["id"], "category": case["category"], "pass": all(checks.values()),
                        "checks": checks, "latency_ms": latency_ms})
    return results


def summarize(name, results):
    passed = sum(r["pass"] for r in results)
    p95 = sorted(r["latency_ms"] for r in results)[int(0.95 * (len(results) - 1))]
    print(f"\n== {name}: {passed}/{len(results)} passed  (p95 latency {p95:.0f} ms)")
    by_cat = {}
    for r in results:
        by_cat.setdefault(r["category"], []).append(r["pass"])
    for cat, ps in sorted(by_cat.items()):
        print(f"   {cat:13} {sum(ps)}/{len(ps)}")
    for r in results:
        if not r["pass"]:
            failed = [k for k, v in r["checks"].items() if not v]
            print(f"   FAIL {r['id']}: {', '.join(failed)}")
    return passed


if __name__ == "__main__":
    golden = [json.loads(line) for line in open("m6_golden.jsonl")]
    # A/B compare two versions of the system on the same golden set
    a = summarize("v1 (answers everything, threshold=0.0)", run(make_system(0.0), golden))
    b = summarize("v2 (refuses when unsure, threshold=0.35)", run(make_system(0.35), golden))
    print(f"\nDelta v2 - v1: {b - a:+d} cases. Read the failures before trusting the total.")
