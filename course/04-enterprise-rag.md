# Module 4 — Applied AI I: Enterprise RAG

**Time:** ~6 hours · **You'll be able to:** design a retrieval-augmented generation (RAG) system for messy enterprise documents, explain why hybrid search matters, and measure retrieval quality instead of guessing.

[← Module 3](03-cloud-landing-zones.md) · [Course home](README.md) · [Next: Module 5 →](05-agents-and-orchestration.md)

---

## The big idea

"An AI that knows our stuff" is the most common enterprise AI ask, and RAG is how you deliver it. **Most RAG quality problems are retrieval problems, not model problems.** If the right passage isn't in the top few results, no model can answer correctly; it will either refuse or, worse, make something up. So FDEs spend their effort on ingestion and retrieval, and they measure it.

---

## Learn

### The four-stage blueprint (from the roadmap)

```
 Documents ──► 1. Ingestion ──► 2. Indexing ──► 3. Retrieval ──► 4. Grounded generation
 (PDF, SharePoint,  parse, chunk,     vectors +       hybrid search,     answer ONLY from
  wikis, tickets)   attach metadata   keyword index   filter by ACL,     retrieved passages,
                    & permissions                     rerank             cite sources
```

**1. Ingestion: where most of the work is.** Enterprise documents are PDFs with tables, scanned forms, slide decks, and wikis with stale pages. Tools like **LlamaParse** extract structure (tables, headings) rather than flattening everything to text. Decisions you'll make here:
- **Chunking:** split by document structure (sections, headings) instead of a fixed character count when you can. Chunks that are too small lose context; chunks that are too large dilute relevance. Keep the section title with each chunk.
- **Metadata:** source, date, owner, document type, and above all **access permissions**. If retrieval ignores ACLs, the assistant will happily show someone a document they're not allowed to see, and that ends projects.
- **Freshness:** which version is authoritative? Index the system of record, not the copies (Module 2 again).

**2–3. Indexing & retrieval.**
- **Semantic (vector) search** matches *meaning*: "Can I keep customer files on my laptop?" finds the data-storage policy even though the words differ.
- **Keyword (BM25) search** matches *exact terms*: policy IDs, ticket numbers, product codes, acronyms, and internal jargon that embedding models have never seen.
- **Hybrid search** runs both and fuses the rankings (commonly with **Reciprocal Rank Fusion**). The roadmap's point: enterprises are full of "specific industry nomenclature," so you need both.
- **Reranking:** a second, more expensive model re-orders the top ~20 candidates. Often the cheapest large quality gain available.
- **Managed options:** Agent Search (formerly Vertex AI Search) as a managed RAG engine; Vector Search for high-scale custom indexing. Managed is usually the right first choice for an MVA, and you can switch to custom once you have measurements.

**4. Grounded generation.** The model is told to answer *only* from retrieved passages, cite them, and say "I don't know" when the passages don't contain the answer. That refusal behavior is a feature, and you'll test it in Module 6.

### Failure modes to recognize

| Symptom | Likely cause | First fix |
| :--- | :--- | :--- |
| Can't find docs by ID/code | Semantic-only retrieval | Add keyword/hybrid |
| Finds the right doc, wrong answer | Chunk split the key passage, or table flattened | Structure-aware parsing and chunking |
| Confident answer from an outdated doc | No freshness/authority metadata | Index system of record; filter or boost by date |
| Shows a user a doc they shouldn't see | ACLs not enforced at retrieval | Permission-filtered retrieval, never post-hoc |
| Hallucinates when docs don't cover it | No grounding instruction / no refusal path | Grounding prompt + eval for refusals |

---

## Lab — Keyword vs. semantic vs. hybrid, measured (90 min)

```bash
pip install rank_bm25 sentence-transformers
cd course/labs
python m4_hybrid_search.py
```

[`labs/m4_hybrid_search.py`](labs/m4_hybrid_search.py) builds a small fictional knowledge base (policies, runbooks, incidents, jargon, and **near-duplicate documents that differ mainly by ID**) and a 15-question golden set. It reports **hit@1** and **hit@3** for each retriever and a per-question breakdown.

What you should see, roughly:

```
keyword (BM25)   hit@1 12/15   hit@3 13/15
semantic         hit@1 12/15   hit@3 15/15
hybrid (RRF)     hit@1 12/15   hit@3 15/15
```

**Your tasks:**

1. Read the per-question table. Find a question where **keyword wins** and one where **semantic wins**, and explain *why* for each. (Look at the bare-ID query `POL-7713` and at the paraphrased "customer files on my laptop" question.)
2. Notice that hybrid doesn't win hit@1 but ties for best hit@3. Explain why hit@3 (recall) is often the number that matters when the top-k passages are passed to an LLM.
3. Add 5 questions of your own, including at least one with an acronym you use at work and one that **no document answers**. What do the retrievers return for the unanswerable one? (This sets up Module 6.)
4. Try changing `rrf_k` and weighting one retriever more heavily. Does the metric move? Don't trust a change your golden set doesn't show.
5. Stretch: add a cross-encoder reranker (`sentence_transformers.CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")`) over the hybrid top-10 and re-measure hit@1.

**The meta-lesson:** results on a 15-document toy can flip depending on which documents you add. That's the reason to **measure on your own golden set** instead of choosing an approach because of a blog post.

---

## Articulate

**Drill 4.1 — RAG for an exec (30 seconds):**
> *"We don't retrain a model on our data. We give it a librarian. For each question, the system finds the few most relevant passages from our approved documents, the model answers only from those, and it cites them. If the documents don't cover the question, it says so. The quality depends mostly on the librarian, so that's where we focus and what we measure."*

**Drill 4.2 — Hybrid search for an engineer (2 minutes).** Use the lab's per-question table as your evidence.

**Drill 4.3 — Push-back answers:**
- *"Why not fine-tune a model on all our documents?"* → Fine-tuning teaches style and format, not reliable facts. It can't cite, can't respect permissions, and goes stale the day after training. RAG updates when the documents update.
- *"The vendor says their search is 95% accurate."* → "On what data? Let's run it against our 50-question golden set and see."
- *"Can it just search everything?"* → Only if retrieval enforces each user's permissions. Otherwise you've built a data-leak tool.

---

## Drive it at work

- [ ] Inventory the document sources for your mission (or for the most-requested "AI over our docs" use case): where they live, their format, who owns them, how permissions work, and how stale they are.
- [ ] Collect **20 real questions** people actually ask, from tickets, chat channels, or by asking 3 users. For each, note which document *should* answer it. That's the start of your golden set for Module 6.
- [ ] Write a half-page **retrieval design note** in your field notebook: sources, parsing approach, chunking, metadata (including ACLs), and hybrid vs. semantic-only, with your reasoning.

---

## Check yourself

<details><summary>1. Why does pure semantic search fail on queries like "POL-7713"?</summary>
Embedding models represent meaning, and an ID carries almost none, so near-duplicate documents with different IDs look alike. Keyword search matches the exact token.
</details>

<details><summary>2. What is Reciprocal Rank Fusion, in one sentence?</summary>
Combine several rankings by giving each document a score of the sum of 1/(k + rank) across retrievers, so documents ranked well by any retriever rise without needing their raw scores to be comparable.
</details>

<details><summary>3. Where must document permissions be enforced, and why?</summary>
At retrieval time, as a filter, so unauthorized passages never reach the model or the user. Filtering the answer afterwards can still leak content.
</details>

<details><summary>4. Your RAG assistant gives a wrong answer. What's the first thing you check?</summary>
Whether the correct passage was retrieved. If not, it's a retrieval/ingestion problem; if it was, it's a generation/prompting problem.
</details>

---

## Go deeper

- [Pinecone: RAG Learning Center](https://www.pinecone.io/learn/series/rag/): best end-to-end RAG education (required)
- [LlamaParse](https://developers.llamaindex.ai/python/framework/llama_cloud/llama_parse/): structured parsing for complex PDFs
- [Agent Search on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/generative-ai-app-builder/docs): managed RAG
- [Vector Search](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/overview): custom high-scale indexing
- [OpenAI & Morgan Stanley](https://openai.com/customer-stories/morgan-stanley): RAG over 100k+ research documents under compliance constraints
- Roadmap: [The Enterprise RAG Blueprint](../README.md#-the-enterprise-rag-blueprint)

[Next: Module 5 — Agents & Orchestration →](05-agents-and-orchestration.md)
