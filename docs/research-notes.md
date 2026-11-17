# Megan's prior research applied to Lecture to Learning

**November 15, 2026 — AI-assisted adaptation of existing notes, not a new interview or claimed new reading by Megan.** The prior notebook explicitly identifies Megan-supplied notes and November 14 reflections; AI-authored clarifications there remain AI-authored here. Megan has authorized reuse, but has not yet confirmed this new adaptation.

## Existing contribution and provenance

- [Megan's source-specific reading notes](https://github.com/mtm5913/RAG-Research/blob/774018adfb272731203858fdb0bf464598f77933/docs/research.md#my-notes-vector-and-graph-rag): supplied by Megan from the Meilisearch comparison guide.
- [Megan's takeaways](https://github.com/mtm5913/RAG-Research/blob/774018adfb272731203858fdb0bf464598f77933/docs/research.md#my-takeaways-from-the-technical-research-and-checks): her explanations of vector retrieval, context preservation and citation limits.
- [Prior bounded comparisons](https://github.com/mtm5913/RAG-Research/blob/774018adfb272731203858fdb0bf464598f77933/docs/comparisons.md) and [failure/retest log](https://github.com/mtm5913/RAG-Research/blob/774018adfb272731203858fdb0bf464598f77933/docs/experiments.md): earlier individual photography project, with execution authorship documented there. These are background experience, not lecture-system tests or group implementation.

## Reused understanding and proposed application

| Megan's recorded understanding (paraphrased) | Proposed lecture-system consequence | How to check it later |
|---|---|---|
| Vector retrieval can find differently worded questions using meaning, rather than only exact terms. | Compare semantic search with a keyword baseline on paraphrased lecture questions. | Predeclare relevant passages; inspect recall and irrelevant results on the same corpus. |
| Graph retrieval becomes worth reconsidering when questions need connections that passage retrieval misses. | Model concept relationships only if actual lecture questions justify them. | Compare the relationship questions in the fixture against a small evidence-linked concept map. |
| Related information should stay together so retrieval preserves context. | Preserve qualifiers, definitions and timestamp context when chunking. | Reject a guide that turns “may” into “always” or loses a condition. |
| A citation can exist even when its claim is unsupported. | Teacher checks the meaning of each claim against the cited evidence, not just the citation ID. | Seed an incorrect claim with a valid passage ID; review must reject it. |

## Technical cross-checks opened by AI on November 15

- [Sentence Transformers semantic-search documentation](https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html), Background and Symmetric vs. Asymmetric Search: explains embedding queries/documents and task-dependent model selection. Supports similarity retrieval as a candidate; no model is selected or benchmarked here.
- [Neo4j original graph documentation](https://neo4j.com/docs/getting-started/graph-database/): nodes, relationships and properties support explicit concept modeling. Graph adjacency alone is not semantic similarity, and relationship extraction is a separate quality risk.
- [Lewis et al., original RAG paper](https://arxiv.org/abs/2005.11401): external retrieval can supply generation context. Its experiments do not establish our application's accuracy.
- [Meilisearch guide Megan read](https://www.meilisearch.com/blog/graph-rag-vs-vector-rag): reading provenance and a vendor-authored comparison. Broad accuracy, latency and complexity claims are hypotheses to test, not accepted benchmarks for this project.

Chunking splits text; embedding represents it numerically. Neither a valid citation nor a high similarity score verifies a generated claim. Transcript accuracy is an additional risk absent from an already-written document corpus. These are AI-assisted design conclusions cross-checked against the original technical concepts, not new personal reflections attributed to Megan.

## Architecture amendment

Propose vector passage retrieval plus relational review/version records. For one short lecture, reading the complete transcript or using keyword search may be sufficient; do not require a vector database just to use RAG. Compare a whole-transcript/keyword baseline before paying the complexity cost. Retain graph retrieval as the second architectural approach, with an evidence-linked manual presentation in [the alternative comparison](alternative-comparison.md).

**Limits:** Teacher discovery, model/provider selection and external-processing permission remain pending. Existing Qdrant/Groq deployment experience does not authorize sending lecture recordings to those services. No individual app or portfolio is copied into the group deliverable.
