# Proposed build contract

**Plan specification, not implemented. Working scope proceeds on Megan’s instruction to assume agreement.** This narrows the first useful path without choosing providers before permission review.

## Initial path and component choices

Use a browser interface to accept one teacher-authorized recorded lecture; retain live listening/capture as the intended later input option. After transcription, expose a correction screen, a cited guide draft, a teacher review queue and a class-restricted publication view. Begin with a study guide; add briefing/question-set formats after this path works. The text-only fixture supports Plan discussion but does not satisfy the eventual audio-input feature.

**Proposed choices:** a server-side transcription adapter; relational records for sources, versions, permissions and review events; private file storage for recordings; replaceable retrieval adapter supporting a keyword baseline and optional vector index; server-side generation restricted to retrieved evidence. Model, database product, authentication system, hosting and cost are undecided. No keys or recordings belong in the public repository.

For a single short transcript, a full-transcript draft is a legitimate baseline. Compare it with section-level retrieval on coverage and support before committing to additional indexing. Longer lectures need chunking that retains speaker, timing and context. Do not equate fewer components with measured better output.

## Proposed records

| Record | Minimum fields / invariant |
|---|---|
| Source | ID, teacher, topic, original file reference, hash, permission reference, allowed audience, processing restrictions, deletion policy; permission must be present before processing. |
| Transcript version | Source ID, version, raw/corrected status, correction history; raw transcription preserved until retention policy requires deletion. |
| Passage | ID, source/version, text, start/end time, review status; timestamps must refer to actual audio once available. |
| Draft version | Transcript version, guide sections, claims, supporting passage IDs, unresolved gaps, author and revision. |
| Review event | Reviewer identity, role, draft version, decision, reason and time; approval cannot silently transfer to another version. |
| Publication | Approved version, teacher approval reference, allowed audience and publication time. |

## Proposed states and failure handling

Source: pending permission → authorized → imported → transcript needs review → transcript approved. If permission is denied, stop processing. If transcription fails, retain an error status and retry without creating duplicate sources. If time alignment is unavailable, label references unverified; do not invent timestamps.

Guide: draft → in review → returned or approved → published. An edit creates a new draft version. Student requests must check audience and approved publication on the server, not just hide buttons. Reject unknown/old passage references. A transcript correction marks affected drafts stale; publication of a stale version must be blocked or withdrawn pending re-review.

If retrieval lacks evidence, record the gap. If generation fails, show a retryable draft error, never a fabricated guide. If external processing is prohibited, select a permitted local path or keep the source out of the system. These are requirements, not verified protections.

## Future integration checks

Run authorized synthetic audio through the whole path. Compare recording against transcript before checking generation. Inspect at least one missing-evidence answer, duplicate import, stale citation, denied student access, rejected draft and revised approval. Record actual inputs, versions, expected/observed results, reviewer, failure evidence and retest links. Use a real teacher/peer for usability; AI demonstrations alone are insufficient.


## November 17 combined design amendment

Approved guides/cards enter a searchable class library with lecture/source and transcript-version filters. Search only teacher-approved current material. At 390px, citation controls and transcript evidence must remain usable without horizontal document overflow. The teacher may approve their own uploaded lecture; there is no self-approval prohibition. Students cannot directly publish or alter approved records. Cross-review by Megan/Daniel applies to project development.

PostgreSQL/pgvector is a candidate credited to Daniel’s proposal, not an adopted or tested deployment. Named proposed owners and reviewers are in the README. Use the working split on the basis recorded in the combined decision. Source corrections require renewed teacher review before affected revised material is published.
