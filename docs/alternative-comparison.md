# Alternative architecture presentation

**AI-prepared paper exercise, November 15. No vector or graph engine ran.** Uses [F01](../fixtures/lecture-script.md); describes expected evidence, not measured rankings, speed or quality.

## Approach A: passage retrieval

Store six passages with source/version IDs and timestamp labels. Embed the approved passage text and retrieve passages for a guide section, scoped to F01-v1. Retain a full-transcript/keyword baseline: this small fixture may not require a vector database.

## Approach B: evidence-linked concept graph

| Subject | Relationship | Object | Evidence |
|---|---|---|---|
| Editor | prepares | Draft | p01 |
| Teacher | reviews | Draft | p02 |
| Claim | requires | Supporting passage | p02 |
| Approval | applies to | Specific version | p03 |
| Changed version | returns to | Draft | p03 |
| Teacher | approves | Publication | p04 |
| Publication | limited to | Permitted class audience | p04 |
| Timestamp | helps locate | Audio | p05 |

Here p01 means F01-v1-p01, etc. Relationships are manually selected from the synthetic source by AI, not automatically extracted or human-verified. Avoid inventing an edge “timestamp guarantees accuracy.” Review-state relationships may also belong in ordinary relational tables; their existence does not require a graph database.

## Same questions, expected evidence

| Question | Required evidence | A: expected passage approach | B: expected graph approach |
|---|---|---|---|
| What are the stages? | p01 | Direct passage | Workflow/stage edges would need adding; this graph is incomplete. |
| Why do references need inspection? | p02 | Preserve explanation text | Claim/support edge alone loses the explanation; fetch original passage. |
| What changes after editing an approved guide? | p03 | Preserve version condition | Follow version/returns-to relationships; validate the condition in p03. |
| Who approves and who can view publication? | p04 | One passage contains both facts | Teacher → publication → audience plus source evidence. |
| Which provider is recommended? | p06, no recommendation | Must decline recommendation | Missing provider edge cannot prove absence; inspect source/completeness. |

**Observed in this paper exercise:** The drafted graph omits the workflow stages and compresses explanatory/negative statements. This is a limitation of this manually prepared representation, not proof all graph systems fail. The passages already contain the expected answers; semantic retrieval success has not been measured.

**Provisional choice:** A, subject to baseline evaluation; working scope follows Megan’s instruction to assume agreement. The useful group feature is source/version/review/publication control. The graph adds extraction/maintenance work without a demonstrated unmet question. Reconsider if real users need connections across lectures that passage retrieval misses.

**Still planned:** Build both retrieval representations if warranted, use the same predeclared questions, record returned evidence and preparation time, inspect omissions, and compare a stronger lexical baseline. No numerical performance advantage is claimed.
