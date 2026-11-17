# Combined project decision — November 17, 2026

**Status:** Megan requested this combined direction and publication. Megan instructed us to proceed assuming Daniel agrees to the design/task split. This is the basis of the working agreement, not a direct confirmation attributed to Daniel. This is a documented design decision, not real peer feedback or an implementation result.

## Contribution provenance

| Origin | Retained in combined project |
|---|---|
| Megan’s lecture concept and prior RAG notes | Authorized audio input; transcript correction; timestamped evidence; source-supported study materials; claim-level checking and missing-evidence handling |
| [Daniel’s original proposal](https://github.com/dan38-cmyk/Group-Content-System/blob/de003bb/RESEARCH.md) | Searchable reviewed library, learning cards, source/version filters, mobile citation usability, source-change review, PostgreSQL/pgvector candidate |

Both original preparations were AI-assisted. Reusing an idea credits the original planning work without claiming the author implemented it or personally verified every technical claim.

## Selected combination and scope boundary

Lecture → corrected transcript → cited study guide/cards → teacher approval → searchable class library. Begin with one short authorized lecture and one guide. Public SQL/pandas tutorial import is deferred; it may later support a lecture if teacher-approved and separately permitted. This avoids requiring two unrelated source pipelines in the first build.

## Approval clarification

Megan questioned whether self-approval prevention makes sense when the teacher supplies the lecture and is best placed to review its meaning. Decision: remove the blanket prohibition. A teacher can upload/correct/review/approve their own lecture materials. Students have read/search access; optional suggestions need teacher approval. Review of project changes by the other teammate remains required and is distinct from application roles.

Alternatives considered: (1) require a second approver, increasing independence but adding teacher staffing and review effort not established as necessary; (2) teacher-controlled approval, chosen for the initial workflow. Risk retained: the lecturer can overlook errors or repeat subject inaccuracies. Proposed mitigation: original audio/transcript references, version history, claim-level inspection and future student correction suggestions. Teacher approval does not prove factual correctness.

## Architecture discussion

Keep vector retrieval plus relational workflow/version records provisionally, with a keyword/full-transcript baseline. Graph retrieval remains the alternative if real cross-concept questions expose a need. Daniel’s PostgreSQL/pgvector is a candidate, not a tested deployment. Provider permissions, resource availability and effectiveness are unresolved.

## Actual revision / next

Updated shared problem/workflow, five stories, named proposed responsibilities, contribution attribution and both submission notes. Updated the synthetic example to match teacher-controlled approval. No audio exists; synthetic timing remains illustrative. Next: use the working assignments, both read/review, real peer feedback is recorded, and the teacher source contract is completed.
