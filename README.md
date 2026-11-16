# Lecture to Learning — shared project record

**Stage:** Plan draft, November 15, 2026. **Due:** November 17, 2026, 1 p.m. Eastern.

This is the team's working record for Deliverable 3, educational-content publishing. No application, recording, transcription run, retrieval experiment or publishing test exists yet. This record is AI-assisted and requires both members' review. It is not ready to submit until the outstanding items below are resolved.

**Team:** [your name], [partner name]. **Repository URL:** https://github.com/mtm5913/lecture-to-learning. **Shared record URL:** https://github.com/mtm5913/lecture-to-learning/blob/main/README.md. **Demo:** none.

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

**Research question:** How can a teacher-authorized lecture be transformed into a useful study guide with verifiable transcript references and teacher approval before publication?

**Bounded first version:** Capture one short lecture, transcribe it with timestamps, prepare one study guide, and let the teacher review and publish it. Briefings and question sets are later output options. Start with a short recording rather than simultaneous live transcription; live capture is a later extension. This is a proposed scope choice for the team to confirm.

**Discovery still needed:** Ask a teacher what makes lecture summaries useful or misleading, what correction effort is acceptable, and whether recording/processing is permitted. Ask a student to locate support for a sample guide claim. Record actual responses here; no interviews have occurred.

## Sources and permissions

The lecture is the primary content source. A transcript is a derived representation, not independent confirmation that the lecture is factually correct. Technical research sources below inform the design and must not silently become course-content evidence.

| ID | Source | Permission/status | Intended use |
|---|---|---|---|
| L01 | Teacher lecture recording; teacher, topic, date and file reference TBD | Not collected; teacher authorization and course/institution requirements not verified | Original evidence for what was said |
| T01 | Timestamped transcript derived from L01 | Not created; inherits L01 access restrictions | Searchable passages and citations |
| C01 | Optional teacher-approved slides/readings | None selected; permission must be checked separately | Clarify terms or verify subject claims |
| F01 | Team-authored short sample lecture | Not written or recorded; label synthetic when created | Early workflow fixture, not evidence of real classroom usefulness |

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

**Provisional decision:** Approach A, with ordinary relational records for permissions, versions and review state. The first question is finding lecture passages for guide sections, and a verified concept graph would add work before that path is useful. This is an engineering judgment, not a measured advantage. A vector index does not replace the review workflow or guarantee factuality. Provider/model, hosting and costs remain undecided pending permission and a small experiment.

**Meaningful alternative experiment, planned:** For the same short lecture, manually map 5–10 concepts and evidence-backed relationships. Compare A and B on three topic questions and two relationship questions. Record relevant evidence found/missed, unsupported relationships, and preparation/review time. Revisit the architecture if relationship questions dominate or vector retrieval repeatedly misses required context. No experiment has run.

## Proposed workflow and source trace

1. Teacher authorizes capture and processing; create a manifest record.
2. Capture/upload the recording, validate type and size, and hash it. A repeat import should reuse the existing lecture record.
3. Transcribe with timestamps. Preserve the raw transcript; show uncertain terminology for human correction and version the corrected transcript.
4. Divide the approved transcript into passages while preserving speaker/timing context and identifiers. Do not remove qualifiers or merge distinct statements as duplicate text.
5. Store original recording privately; store transcript passages, source/version metadata, draft revisions and review events in a database. Index passage embeddings for retrieval.
6. For each proposed guide section, retrieve passages from that lecture/version, draft only supported claims, attach passage/timestamp references and mark insufficient evidence. A whole-guide coverage check must catch lecture topics omitted by section retrieval.
7. Teacher opens cited evidence, corrects/rejects unsupported material and approves a specific draft version. Transcript corrections invalidate affected citations and require review again.
8. Publish the approved version to the permitted student audience. Preserve a review history; edits return the document to draft.

**Illustrative trace only — not an executed test:** Suppose synthetic recording F01 says at 00:20–00:35, “An extract, transform, load pipeline extracts source data, transforms it, and loads the result into a destination.” Derived passage `F01-v1-p02` retains those timestamps and text. Retrieval for “What are the ETL stages?” should return that passage. Draft claim “ETL has extract, transform and load stages [F01-v1-p02, 00:20–00:35]” goes into the review queue. The reviewer compares it with the recording before approving it. These IDs, timestamps and words are a designed fixture; no audio or transcript file exists.

**Failure trace:** A request for “Which database does this teacher recommend?” has no support in that passage. The output should say evidence is insufficient, rather than inventing a recommendation. A timestamp pointing to the wrong segment, or a claim changing the source meaning, fails review even if a citation is present.

This shared system adds persistent source/version tracking, assigned human review and approved publication beyond an individual chat.

## Stories and evaluation

All criteria below are proposed acceptance checks, with results **NOT RUN**. Member A/B are placeholders to replace with real names.

| Story | Planned check and pass criterion | Owner | Different reviewer |
|---|---|---|---|
| As a teacher, I import an authorized lecture once and can locate its source record. | Import the same file twice: one lecture, traceable permission record; an unauthorized fixture cannot proceed. | A | B |
| As a teacher, I correct transcription before guide creation. | Compare a short recording with transcript: inspect names, numbers, negation and timestamps; corrections create a version and affected drafts require review. | A | B |
| As a student, I inspect evidence behind a study-guide claim. | For every factual claim in one short guide, reviewer opens the cited passage/audio and finds supporting meaning at the stated location; zero unsupported claims accepted. | B | A |
| As a student, I receive an honest gap when the lecture lacks evidence. | Two intentionally absent-topic questions produce an insufficient-evidence response, without invented answers or citations. | B | A |
| As a teacher, I control what students receive. | Draft/rejected material is unavailable to the student view; approval exposes only the approved version. Teacher completes review without developer help and feedback is recorded. | B | A |

**Small evaluation set to create:** one permitted 3–5 minute recording; human-corrected transcript; three answerable topic questions; two relationship questions for the alternative comparison; two absent-topic questions; one duplicate import; one transcript correction; one rejected draft. Label expected supporting passages before running retrieval. Do not score similarity alone as correctness.

**Coverage and usability:** Teacher lists the fixture's main topics before seeing the generated guide. Check every listed topic appears or has an explicit gap. Observe a teacher finding evidence and approving/returning a draft; record confusion and correction effort. Ask what effort is acceptable before setting a time threshold. A diagram or example trace is not evidence these checks passed.

## Owners and contributions

| Work slice | Proposed owner | Reviewer | Actual evidence |
|---|---|---|---|
| Teacher discovery, source contract, recording/transcript/version design | Member A — name TBD | Member B — name TBD | None yet |
| Guide generation, citation review and publishing-state design | Member B — name TBD | Member A — name TBD | None yet |
| Vector/graph/RAG research and architecture comparison | Both, individual notes required | Cross-review | Initial AI-assisted source summaries above; member review pending |
| Integration, evaluation and real peer workshop | Both, specify tasks when assigned | Cross-review plus real peer | None yet |

**Known contribution:** The requesting student selected educational-content publishing and defined the lecture → transcript → source-supported learning-material workflow. Add their name and a durable record/commit link. Do not claim implementation, research reading or testing that has not occurred.

**Help received:** An AI assistant drafted this record and proposed architecture, stories and checks. Team members must verify the linked research, revise choices, and explain their own work. No simulated peer review is included.

## Peer feedback and decisions

**Status:** No peer has reviewed this plan yet.

Ask a real peer: “Follow the source trace from recording to published claim. Where could an unsupported claim slip through? Challenge one assumption, such as whether timestamps are enough for review or whether vector retrieval is justified for a short lecture.”

| Date / peer | Actual feedback | Team decision and reason | Changed section / commit | Follow-up check and result |
|---|---|---|---|---|
| Pending | Pending real feedback | Pending | Pending | Not run |

Do not fill this row with hypothetical feedback. Record a disagreement too if the team keeps its original choice with a reason.

## Actual checks and next steps

**Changed November 15:** Created an initial shared Plan draft and individual submission-note draft.

**Actually checked during drafting:** Workspace was empty before drafting. Opened the RAG paper abstract and the linked Sentence Transformers and Neo4j documentation; bounded technical summaries to those sources. Compared this draft's sections against the assignment text supplied in chat. These are document/source checks, not software tests or independent human review.

**Not checked:** Real reader needs; recording permissions; transcription accuracy; source trace execution; retrieval or generation quality; workflow usability; access control; deployment; peer feedback. No system behavior has run.

**Before Plan submission:**

- Confirm partner and replace member placeholders; agree scope and task split.
- Choose the lecture topic and teacher/contact; document source availability and permission status honestly.
- Both members read the course handout and original technical sources; add their own research notes and actual contribution links.
- Obtain a real peer's trace review, document the tradeoff challenged, and revise the record as warranted.
- Create/use the shared remote repository and verify the record is accessible to the reviewer. Add actual URLs; this local file is not a submission link.
- Cross-review the draft, update changed/checked/next, and finish each person's contribution note.

**After Plan:** Obtain an authorized sample, implement one complete path, execute and record the evaluation set, compare the alternative, and later host the system. Proposed course milestones from the supplied brief: Build November 24, 1 p.m.; Checked Release December 3, 1 p.m.; Improve December 10, 11:59 p.m., all Eastern. Verify schedule in the [course guide](https://njit.instructure.com/courses/70733/pages/is373-projects-and-weekly-work).
