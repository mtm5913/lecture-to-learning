# Lecture to Learning — shared project record

**Stage:** Plan, updated November 17, 2026. **Due:** November 17, 2026, 1 p.m. Eastern.

This is the team's working record for Deliverable 3, educational-content publishing. No application, recording, transcription run, retrieval experiment or publishing test exists yet. A synthetic written fixture and Plan artifact checks now exist; see the evidence index below. This record is AI-assisted and requires both members' review. Remaining human review and source-permission gaps are disclosed below.

**Team:** Megan and Daniel. **Repository URL:** https://github.com/mtm5913/lecture-to-learning. **Shared record URL:** https://github.com/mtm5913/lecture-to-learning/blob/main/README.md. **Demo:** none.

## Research-review index

- [Problem and reader](#problem-and-reader)
- [Sources and permissions](#sources-and-permissions)
- [Research and architecture decision](#research-and-architecture-decision)
- [Proposed workflow and source trace](#proposed-workflow-and-source-trace)
- [Stories and evaluation](#stories-and-evaluation)
- [Owners and contributions](#owners-and-contributions)
- [Peer feedback and decisions](#peer-feedback-and-decisions)
- [Actual checks and next steps](#actual-checks-and-next-steps)

## Problem and reader

**Course direction:** Educational-content publishing.

**Primary reader:** A student revisiting a teacher's lecture. **Editor/approver:** The teacher. **Proposed problem:** Students need concise learning materials that preserve the lecture's meaning and let them locate the supporting explanation. Teachers need a way to correct and approve these materials before students see them. These needs are hypotheses, not findings from interviews.

**Research question:** How can a teacher-authorized lecture be transformed into accurate, reviewable learning materials that students can search and verify against the lecture?

**Combined direction:** Teacher-authorized lecture → corrected transcript → cited study guide or learning cards → teacher review/approval → searchable class library. Megan contributes the lecture-to-learning workflow and her existing RAG research; Daniel contributes the learning-library proposal, learning cards, source/version filters, mobile citation usability, source-change review and PostgreSQL/pgvector as an architecture candidate. [Combined decision and contribution provenance](docs/combined-decision.md).

**Bounded first version:** One short recorded lecture, a corrected timestamped transcript, one cited study guide, teacher approval, and a searchable class-restricted library. Learning cards are an additional format after the first path works; briefings/question sets and simultaneous live capture remain later options. SQL/pandas tutorials from Daniel’s original proposal are optional future teacher-approved supporting sources, not a second required corpus.

**Approval rule:** The teacher may upload, correct and approve materials from their own lecture. Students view/search approved material; optional correction suggestions stay drafts until teacher approval. There is no requirement for a second teacher or blanket self-approval prohibition. Megan and Daniel must still review each other’s project work, as required by the assignment.

**Discovery still needed:** Ask a teacher what makes lecture summaries useful or misleading, what correction effort is acceptable, and whether recording/processing is permitted. Ask a student to locate support for a sample guide claim. Record actual responses here; no interviews have occurred.

## Sources and permissions

The lecture is the primary content source. A transcript is a derived representation, not independent confirmation that the lecture is factually correct. Technical research sources below inform the design and must not silently become course-content evidence.

| ID | Source | Permission/status | Intended use |
|---|---|---|---|
| L01 | Teacher lecture recording; teacher, topic, date and file reference TBD | Not collected; teacher authorization and course/institution requirements not verified | Original evidence for what was said |
| T01 | Timestamped transcript derived from L01 | Not created; inherits L01 access restrictions | Searchable passages and citations |
| C01 | Optional teacher-approved slides/readings | None selected; permission must be checked separately | Clarify terms or verify subject claims |
| F01 | [AI-authored synthetic written lecture](fixtures/lecture-script.md) | Created as project fixture; no teacher or recording; illustrative timestamp labels | Source trace and evaluation preparation, not classroom findings |

**Proposed source manifest fields:** source ID, title/topic, author/speaker, date, original location, permission evidence and permitted audience, processing permission, retention/deletion decision, content hash, transcript version, timestamp range, and access status. No recording is authorized merely by this plan.

**Proposed handling:** Ask for permission before recording or uploading a lecture to any transcription provider. Prefer a teacher-only sample; exclude student discussion from the first recording. Confirm storage, external processing and publication permissions. Keep recordings and unpublished drafts private; repository examples should contain only permitted or synthetic material. Select a retention period with the teacher rather than inventing one now.

## Research and architecture decision

### Initial original technical sources

These links were opened while drafting on November 15. The summaries reflect the retrieved abstract/documentation, not a complete literature review. Each member still needs to read and record their own interpretation and questions.

| Source | Supported concept | Implication and limit |
|---|---|---|
| [Lewis et al., RAG paper](https://arxiv.org/abs/2005.11401) | RAG combines generation with retrieval from an external non-parametric memory | Supports retrieving evidence before drafting. Its results do not establish accuracy for our lecture workflow. |
| [Sentence Transformers: semantic textual similarity](https://www.sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html) | Text embeddings can be compared using similarity measures | Supports a semantic passage-search candidate. Similarity does not prove a claim is supported. |
| [Neo4j: graph database concepts](https://neo4j.com/docs/getting-started/appendix/graphdb-concepts/) | A property graph represents entities and relationships | Supports explicitly modeling lecture concepts and connections. Extracted relationships still require verification. |

Course research to complete: [database/graph/RAG handout](https://kaw393939.github.io/is373-studio/handouts/database-rag-research.html). This course page could not be retrieved by the browsing tool during drafting; neither member's reading is claimed complete. [Project-record workshop prompts](https://kaw393939.github.io/is373-studio/templates/project-record.html#research-review-index) should also be checked manually.

### Two proposed approaches

| Consideration | A: Vector retrieval + RAG | B: Graph retrieval + RAG |
|---|---|---|
| Representation | Timestamped transcript chunks with embeddings | Concepts, definitions and relationships linked to transcript evidence |
| Retrieval | Find semantically related passages, scoped to the selected lecture/version | Traverse verified concept relationships to gather supporting passages |
| Likely fit | Topic-based study-guide sections and paraphrased requests | Questions about dependencies or connections among concepts |
| Main risk | Similar passages can omit qualifiers or essential context | Incorrect entity/relationship extraction can distort the lecture |
| Work required | Chunking, embedding, retrieval tuning and citation review | Schema design, extraction, relationship validation and retrieval logic |
| Evidence needed | Compare retrieved passages with human-labeled relevant passages | Compare a small manually verified concept map with expected relationships |

**Provisional decision:** Approach A, with ordinary relational records for permissions, versions and review state. The first question is finding lecture passages for guide sections, and a verified concept graph would add work before that path is useful. This is an engineering judgment, not a measured advantage. A vector index does not replace the review workflow or guarantee factuality. PostgreSQL with pgvector, proposed in Daniel’s research, is a candidate for storing vectors alongside relational source/version/review records. Adoption, extension availability, model/provider, hosting and costs remain unverified and subject to team review. No database has been implemented.

**Meaningful alternative experiment, planned:** For the same short lecture, manually map 5–10 concepts and evidence-backed relationships. Compare A and B on three topic questions and two relationship questions. Record relevant evidence found/missed, unsupported relationships, and preparation/review time. Revisit the architecture if relationship questions dominate or vector retrieval repeatedly misses required context. No experiment has run.

## Proposed workflow and source trace

1. Teacher authorizes capture and processing; create a manifest record.
2. Capture/upload the recording, validate type and size, and hash it. A repeat import should reuse the existing lecture record.
3. Transcribe with timestamps. Preserve the raw transcript; show uncertain terminology for human correction and version the corrected transcript.
4. Divide the approved transcript into passages while preserving speaker/timing context and identifiers. Do not remove qualifiers or merge distinct statements as duplicate text.
5. Store original recording privately; store transcript passages, source/version metadata, draft revisions and review events in a database. Index passage embeddings for retrieval.
6. For each proposed guide section, retrieve passages from that lecture/version, draft only supported claims, attach passage/timestamp references and mark insufficient evidence. A whole-guide coverage check must catch lecture topics omitted by section retrieval.
7. Teacher opens cited evidence, corrects/rejects unsupported material and approves a specific draft version. Transcript corrections invalidate affected citations and require review again.
8. Publish the approved version to a searchable library restricted to the permitted class audience. Search only approved material, filter by lecture/source and transcript version, and display mobile-usable citations. Preserve review history; edits or source corrections require renewed teacher approval. Unsupported requests receive an evidence-gap response.

**Prepared trace, not system execution:** [F01 synthetic script](fixtures/lecture-script.md) → passage `F01-v1-p03` (illustrative 00:50–01:15) → proposed passage storage/index → [sample guide](docs/sample-study-guide.md), version-specific approval claim → AI text review recorded in [Plan checks](evidence/plan-checks-2026-11-15.md). No audio exists, no storage/index was built, and no teacher approved the draft. The passage labels are not measured timestamps.

**Failure trace:** The seeded claim “editing preserves approval” cites a real fixture passage but contradicts p03. The evaluation requires rejection. Questions about provider choice and price must identify missing evidence. The prepared examples clarify expected behavior; they do not show that a model or reviewer actually catches errors.

This shared system adds persistent source/version tracking, assigned human review and approved publication beyond an individual chat.

## Stories and evaluation

All criteria below are proposed acceptance checks, with results **NOT RUN**. Named task assignments are the working split, proceeding on Megan’s stated assumption of Daniel’s agreement; they do not claim completed implementation. A different project reviewer is not an application approval restriction.

| Story | Planned check and pass criterion | Owner (working split) | Different project reviewer |
|---|---|---|---|
| As a teacher, I import an authorized lecture without duplicates. | Reimport the same file: one lecture/source record, retained permission evidence and stable source identity; unauthorized processing is blocked. | Daniel | Megan |
| As a teacher, I correct and version the transcript before materials are prepared. | Inspect names, numbers, negations and timing against audio; corrections create a version and flag affected materials for renewed review. | Daniel | Megan |
| As a teacher, I review and correct cited learning materials generated from my lecture. | Inspect every factual claim in one short guide against its cited passage/audio; reject seeded unsupported claims. The same teacher who uploaded the lecture can review and approve it. | Megan | Daniel |
| As a student, I search approved materials and inspect their evidence. | Predeclared paraphrased questions retrieve the relevant approved material in the first four results; lecture/version filters exclude other versions; citation text is readable and usable at 390px without horizontal overflow. | Daniel | Megan |
| As a teacher, I control publication and revisions so students receive reviewed, supported materials. | Draft/rejected versions stay unavailable to students; only the approved version appears. Source/guide changes require renewed approval. Two absent-topic questions receive insufficient-evidence responses without invented claims. | Megan | Daniel |

**Small evaluation set to create:** one permitted 3–5 minute recording; human-corrected transcript; three answerable topic questions; two relationship questions for the alternative comparison; two absent-topic questions; one duplicate import; one transcript correction; one rejected draft. Label expected supporting passages before running retrieval. Do not score similarity alone as correctness.

**Coverage and usability:** Teacher lists the fixture's main topics before seeing the generated guide. Check every listed topic appears or has an explicit gap. Observe a teacher finding evidence and approving/returning a draft; record confusion and correction effort. Ask what effort is acceptable before setting a time threshold. A diagram or example trace is not evidence these checks passed.

## Owners and contributions

| Work slice | Owner (working split) | Different reviewer | Actual contribution / status |
|---|---|---|---|
| Source permissions, intake, transcription/version design | Daniel | Megan | Adaptation to lectures proposed; implementation not run |
| Guide/card drafting, claim citations and missing-evidence evaluation | Megan | Daniel | Lecture workflow and prior research supplied; new artifacts AI-assisted |
| Searchable class library, source/version filters and mobile citations | Daniel | Megan | Ideas documented in Daniel’s original proposal; implementation not run |
| Teacher review, approval and source-change invalidation | Megan | Daniel | Combined design documented; Daniel’s source-change requirements credited |
| Architecture and integration | Both: Megan contributes prior RAG notes; Daniel contributes library/pgvector research | Cross-review | Provisional choice; no group database or retrieval test |

**Megan’s contribution:** Selected educational-content publishing, defined the lecture → transcript → learning-material workflow, supplied prior vector/graph/RAG notes, and directed the combined design and teacher-approval clarification. [Research provenance](docs/research-notes.md).

**Daniel’s contribution:** Prepared the AI-assisted [Data Learning Library proposal](https://github.com/dan38-cmyk/Group-Content-System/blob/de003bb/RESEARCH.md), including reviewed learning cards, searchable publication, source/version filters, mobile citation checks, renewed review after source changes and PostgreSQL/pgvector as a candidate. These ideas are retained here. [His contribution record](https://github.com/dan38-cmyk/Group-Content-System/blob/de003bb/LEARNING.md). This credits existing planning work; it does not claim he edited this repository, accepted task assignments or implemented the features.

**Working agreement:** On November 17, Megan instructed us to proceed assuming Daniel confirms the combined scope and named responsibilities. We are using that working agreement for planning; this records Megan’s instruction rather than a direct statement from Daniel. It is not peer feedback or evidence of implementation.

**Help received:** An AI assistant drafted this record and proposed architecture, stories and checks. Team members must verify the linked research, revise choices, and explain their own work. No simulated peer review is included.

## Peer feedback and decisions

**Status:** No peer has reviewed this plan yet.

Ask a real peer: “Follow the source trace from recording to published claim. Where could an unsupported claim slip through? Challenge one assumption, such as whether timestamps are enough for review or whether vector retrieval is justified for a short lecture.”

| Date / peer | Actual feedback | Team decision and reason | Changed section / commit | Follow-up check and result |
|---|---|---|---|---|
| Pending | Pending real feedback | Pending | Pending | Not run |

Do not fill this row with hypothetical feedback. Record a disagreement too if the team keeps its original choice with a reason.

## Actual checks and next steps

**Changed November 15:** Created the shared Plan and submission draft; added the independently preparable artifacts indexed below.

**Actually checked during drafting:** Workspace was empty before drafting. Opened the RAG paper abstract and the linked Sentence Transformers and Neo4j documentation; bounded technical summaries to those sources. Compared this draft's sections against the assignment text supplied in chat. These are document/source checks, not software tests or independent human review.

**Not checked:** Real reader needs; recording permissions; transcription accuracy; source trace execution; retrieval or generation quality; workflow usability; access control; deployment; peer feedback. No system behavior has run.

**Before Plan submission:**

- Proceed with the combined scope and named working split on Megan’s instruction; record any later team changes.
- Choose the lecture topic and teacher/contact; document source availability and permission status honestly.
- Both members read the course handout and original technical sources; add their own research notes and actual contribution links.
- Obtain a real peer's trace review, document the tradeoff challenged, and revise the record as warranted.
- Shared public repository and record now exist. Verify access again before submission; update links if moved.
- Cross-review the draft, update changed/checked/next, and finish each person's contribution note.

**After Plan:** Obtain an authorized sample, implement one complete path, execute and record the evaluation set, compare the alternative, and later host the system. Proposed course milestones from the supplied brief: Build November 24, 1 p.m.; Checked Release December 3, 1 p.m.; Improve December 10, 11:59 p.m., all Eastern. Verify schedule in the [course guide](https://njit.instructure.com/courses/70733/pages/is373-projects-and-weekly-work).


## Independent preparation evidence index

- [Megan’s existing research applied here](docs/research-notes.md): links to her prior notes; fresh AI cross-checks and limits.
- [Written synthetic lecture fixture](fixtures/lecture-script.md): no audio or machine transcription claimed.
- [Sample study guide and seeded bad claims](docs/sample-study-guide.md): editorial example, not application output.
- [Alternative architecture presentation](docs/alternative-comparison.md): paper comparison, not measured retrieval results.
- [Nine evaluation cases and expected evidence](fixtures/evaluation.json): actual test inputs prepared; model tests not run.
- [Executed Plan checks](evidence/plan-checks-2026-11-15.md) and [reproduction script](scripts/check_plan.py).
- [Teacher/student discovery and peer-review prompts](docs/discovery-and-review.md): prepared; conversations not conducted.

**Decision to discuss with the team:** A short lecture may fit a full-transcript or keyword baseline. Vector retrieval is provisional, not a requirement to justify after the fact. [Research amendment](docs/research-notes.md#architecture-amendment).

**Observations:** Megan’s prior notes exist; a synthetic script, draft output and evaluation records have now been created; fixture checks ran. **Assumptions:** teacher demand, student usefulness, permission availability and vector retrieval benefit remain unverified. **Pending human work:** personal research review, teacher source contract and real peer feedback. The independent preparation does not satisfy those requirements by itself.

- [Proposed build contract and failure states](docs/build-contract.md).
- [Plan requirement/readiness audit](evidence/plan-readiness.md).


## November 17 changed / checked / next

**Changed:** Combined the lecture workflow with Daniel’s learning-library design, replaced the five stories, added named proposed owners and different project reviewers, credited both contributions, and clarified that teachers can approve materials from their own lectures. [Decision record](docs/combined-decision.md).

**Checked:** AI reviewed the document for consistent teacher approval, named story coverage and contribution attribution; reran the fixture/local-link checks. [November 17 check record](evidence/combined-plan-checks-2026-11-17.md). No application tests or human peer review ran.

**Next:** Both members review the research; a real peer follows the trace and challenges a tradeoff; record the response and obtain a teacher-authorized source. Submit the same shared record with separate contribution notes. [Canvas text](SUBMISSION-NOTE.md).

## Team feedback and scope decision

Megan proposed combining her teacher-authorized lecture workflow with Daniel’s searchable learning library. Teachers review and approve study materials before publication. Students can search approved materials and follow citations to the supporting transcript passage and timestamp.

Daniel confirmed that the shared plan reflects the combined direction. Megan contributed the lecture-to-learning workflow. Daniel contributed the searchable library design, including source and version filters, mobile-friendly citations, and renewed review when a source changes.

The source-trace peer walkthrough is pending. Record the walkthrough feedback, the team’s response, and any resulting changes in the [peer feedback table](#peer-feedback-and-decisions).
