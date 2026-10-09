"""Module 4 Lab: keyword vs. semantic vs. hybrid retrieval, measured.

    pip install rank_bm25 sentence-transformers
    python m4_hybrid_search.py

Runs offline after the first model download (~90 MB). No API keys needed.
The corpus is a fictional internal knowledge base. Swap in your own docs later.
"""
import re

from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer

# --- 1. A tiny "enterprise" corpus: policies, runbooks, jargon, IDs -----------
DOCS = {
    "pol-7731": "Policy POL-7731: Client data may only be stored in approved regions. "
                "Copies to personal devices or unapproved SaaS tools are prohibited.",
    "pol-2210": "Policy POL-2210: All production model changes require a model risk review "
                "and sign-off from the model owner before release.",
    "rb-ingest": "Runbook: when the nightly ingestion job fails, check the SFTP drop folder "
                 "for a zero-byte file, then re-trigger the loader from the scheduler.",
    "rb-access": "Runbook: to request read access to the reporting warehouse, open an access "
                 "ticket with your manager's approval and the dataset name.",
    "faq-pto": "FAQ: Employees accrue paid time off monthly. Unused days carry over up to "
               "the annual cap described in the HR handbook.",
    "gloss-nav": "Glossary: NAV (net asset value) is the per-share value of a fund, computed "
                 "at market close from total assets minus liabilities.",
    "gloss-aum": "Glossary: AUM (assets under management) is the total market value of "
                 "assets a firm manages on behalf of clients.",
    "arch-rag": "Architecture note: the assistant retrieves documents using hybrid search "
                "and only answers from retrieved passages, citing the source.",
    "inc-0412": "Incident INC-0412: month-end report showed duplicated accounts because an "
                "upstream export changed its ID format. Fixed by adding a uniqueness check.",
    "sec-keys": "Security standard: service account keys must not be created. Workloads "
                "authenticate with platform-managed identities instead.",
    "onb-laptop": "Onboarding: new joiners receive a laptop on day one; VPN setup instructions "
                  "are in the IT portal under Remote Access.",
    # Near-duplicates that differ mainly by ID: common in real policy/incident libraries
    "pol-7713": "Policy POL-7713: Client data must be retained for seven years and then "
                "deleted from approved regions according to the retention schedule.",
    "inc-0398": "Incident INC-0398: month-end report was delayed because an upstream "
                "export arrived late. Fixed by adding a freshness alert.",
    "pol-2201": "Policy POL-2201: All production dashboard changes require a peer review "
                "before release.",
    "faq-expense": "FAQ: Submit travel expenses within 30 days with itemized receipts. "
                   "Meals above the daily limit need manager approval.",
}

# --- 2. A small golden set: (question, id of the doc that answers it) ---------
GOLDEN = [
    ("What does POL-7731 say?", "pol-7731"),                                   # exact ID
    ("Can I keep a copy of customer files on my own laptop?", "pol-7731"),    # paraphrase
    ("What happened in INC-0412?", "inc-0412"),                                # exact ID
    ("Why were there double-counted clients in the monthly report?", "inc-0412"),  # paraphrase
    ("How is NAV calculated?", "gloss-nav"),                                   # jargon
    ("What's the per-share worth of a fund?", "gloss-nav"),                    # paraphrase of jargon
    ("The overnight load broke, what do I do?", "rb-ingest"),                  # paraphrase
    ("How do I get permission to query the data warehouse?", "rb-access"),
    ("Who has to approve a new version of a production model?", "pol-2210"),
    ("Are JSON keys allowed for service accounts?", "sec-keys"),
    ("How long do I have to file a travel claim?", "faq-expense"),
    ("Does vacation roll over to next year?", "faq-pto"),
    ("POL-7713", "pol-7713"),                                                  # bare ID
    ("INC-0398 root cause", "inc-0398"),                                       # ID + intent
    ("Summary of POL-2201", "pol-2201"),                                       # ID + intent
]

ids, texts = list(DOCS), list(DOCS.values())
tokenize = lambda s: re.findall(r"[a-z0-9\-]+", s.lower())

# --- 3. Three retrievers -------------------------------------------------------
bm25 = BM25Okapi([tokenize(t) for t in texts])
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
doc_vecs = model.encode(texts, normalize_embeddings=True)


def keyword(q, k=3):
    scores = bm25.get_scores(tokenize(q))
    return [ids[i] for i in sorted(range(len(ids)), key=lambda i: -scores[i])[:k]]


def semantic(q, k=3):
    sims = doc_vecs @ model.encode([q], normalize_embeddings=True)[0]
    return [ids[i] for i in sorted(range(len(ids)), key=lambda i: -sims[i])[:k]]


def hybrid(q, k=3, rrf_k=60):
    """Reciprocal Rank Fusion: score = sum over retrievers of 1 / (rrf_k + rank)."""
    fused = {}
    for ranking in (keyword(q, k=len(ids)), semantic(q, k=len(ids))):
        for rank, doc_id in enumerate(ranking):
            fused[doc_id] = fused.get(doc_id, 0) + 1 / (rrf_k + rank + 1)
    return sorted(fused, key=lambda d: -fused[d])[:k]


# --- 4. Measure: hit rate @1 and @3 per retriever ------------------------------
if __name__ == "__main__":
    for name, fn in [("keyword (BM25)", keyword), ("semantic", semantic), ("hybrid (RRF)", hybrid)]:
        hit1 = sum(fn(q)[0] == gold for q, gold in GOLDEN)
        hit3 = sum(gold in fn(q) for q, gold in GOLDEN)
        print(f"{name:16} hit@1 {hit1}/{len(GOLDEN)}   hit@3 {hit3}/{len(GOLDEN)}")
    print("\nPer-question top-1 (keyword | semantic | hybrid):")
    for q, gold in GOLDEN:
        row = [fn(q)[0] for fn in (keyword, semantic, hybrid)]
        marks = ["✓" if r == gold else "✗" for r in row]
        print(f"  {q[:55]:55} {' '.join(marks)}")
