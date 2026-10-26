<!-- repodoc:version 1.12.0 -->

# Persistent memory protocol

This is the protocol's single source of truth. Do not duplicate it elsewhere: the other files in this language package must only reference it.

This project uses an external backend as the **persistent memory and source of truth** for consolidated information. The configured backend's operating rules (where to write, how to organize, how to review) are described in [Memory backend](#memory-backend).

Chat is temporary working memory; the configured backend is persistent, structured, versioned memory.

## What to remember

Use chat freely for brainstorming, hypotheses, comparisons, and temporary reasoning.

When information becomes important and sufficiently established, record it in the configured backend. This includes:

* goals, requirements, and constraints;
* design and architecture decisions;
* technology choices and conventions;
* important domain knowledge;
* relevant configuration and procedures;
* useful research results;
* problems and their solutions;
* rejected alternatives when their rationale is worth retaining;
* open questions and future work;
* anything needed to resume the project correctly later.

Do not archive conversations automatically. **Extract the knowledge**, summarize it, and integrate it into existing documentation.

As a rule of thumb, information that may be useful in a few weeks to understand the project or make a decision should probably be recorded.

## Specification gathering

When the `project` document does not exist or is still a stub, before recording anything else gather the minimum project context by asking the missing questions, one at a time rather than as a single questionnaire:

1. problem or motivation: why the project exists;
2. goal: what it must do, broadly;
3. users and main use cases;
4. what is explicitly out of scope;
5. known constraints (technical, timeline, budget, compliance).

Record the answers in the `project` document as they emerge. Only after this framing is established does it make sense to break down individual requirements into REQs.

When a new requirement emerges during the conversation without acceptance criteria, ask how it will be verified as satisfied before creating the REQ. Do not request the entire template: ask only for the missing information needed to make the requirement verifiable.

This active gathering does not override the general rule against repeatedly interrupting the conversation (see [Automatic behavior](#automatic-behavior)): it applies only when the minimum project context or the acceptance criteria of a new requirement are missing.

## Document types

Adapt document types to what already exists. Do not create unnecessary documents or equivalent types.

* `README`: project overview;
* `AGENTS`: operational instructions only, without duplicating project knowledge;
* `index`: memory index;
* `project`: project context;
* `architecture`: architecture;
* `glossary`: terminology;
* `ontology`: project ontology, including the platform-to-naming-suffix map;
* `REQ-xxx-<title>`: requirements;
* `OPEN-xxx-<title>`: open questions;
* `ADR-xxx-<title>`: decisions;
* `SPEC-xxx-<title>`: specifications, including proposed work (one YAML file per spec, see [Specifications](#specifications));
* `specs-index`: the navigational index of every SPEC, grouped by ordered implementation group and then by scope, with lifecycle status visible on every entry;
* `research`: research;
* `knowledge`: stable, consolidated knowledge — not proposed or planned work, which belongs in `SPEC-xxx-<title>` files.

Create these documents only when needed. The concrete location of each type (file path, folder, or page) depends on the configured backend: see [Memory backend](#memory-backend).

## Linked knowledge base

Create focused, indexed documents connected to one another. Avoid oversized content, excessive fragmentation, and duplication; keep one primary source for each piece of information. The concrete linking mechanism depends on the configured backend.

## Ontology and multi-platform naming

When a project includes artifacts for one or more specific platforms, maintain a canonical map in the `ontology` document between every platform identifier and its naming suffix; it is mandatory for multi-platform projects. Every platform-specific project, module, or artifact must end with the registered suffix, using `<base-name>-<platform-suffix>` unless the repository already has an established convention. Do not invent local suffix variants or reuse one suffix for different platforms.

The ontology must distinguish at least the canonical identifier, display name, suffix, and any accepted legacy aliases or prefixes. If the repository calls a code a “prefix” even though it appears as a suffix in names, record that correspondence explicitly. SPECs identify their platform through the ontology's canonical identifier; shared artifacts use an explicit identifier such as `shared`, also mapped there.

## Metadata

When useful, `knowledge`, `decision`, and `research` documents may carry metadata with:
- `title`
- `updated`
- `related`
- `status` (`draft`, `active`, `deprecated`, or `superseded`).
- `tag`

`openpoint` documents use the same metadata, but with `status` (`open` or `resolved`). `SPEC-xxx-<title>` documents do not use this generic metadata: they follow the dedicated schema in [Specifications](#specifications).

Do not add unnecessary metadata. The concrete metadata syntax depends on the configured backend.

## Updating knowledge

Documentation should primarily describe the **current state**.

When a decision changes:

1. identify the affected documents;
2. update the current documentation;
3. create or update an ADR when needed;
4. update links and indexes.

Do not retain obsolete information in current documents merely to preserve history: **the configured backend keeps the history; documentation describes the current state.**

## ADRs

Create ADRs only for significant decisions. Heading: `# ADR-XXX - Title`. Minimum sections: `Status`, `Context`, `Decision`, `Rationale`, `Alternatives`, `Consequences`, `Related`.

If possible, link an ADR to one or more requirements.

## Requirements

Create a REQ for every requirement exposed. Heading: `# REQ-XXX - Title`.
Minimum sections:
* `Status`
* `Priority`
* `Context`
* `Related`
* `Description`
* `Acceptance Criteria`: a bullet list of verifiable conditions; use Given/When/Then only for complex behavior
* `Example` (if available)

If the requirement emerges without acceptance criteria, ask for them before creating the REQ (see [Specification gathering](#specification-gathering)).

## Open questions

Create an OPEN for questions not yet resolved. Heading: `# OPEN-XXX - Title`.
Minimum sections:
* `Status` (`open` or `resolved`)
* `Context`
* `Description`
* `Related`

When a question is resolved, update `Status` to `resolved`. If the resolution is a significant decision, create or update the corresponding ADR instead of leaving the knowledge only in the OPEN.

## Specifications

Create a `SPEC-xxx-<title>` YAML file as soon as proposed work is worth tracking. Do not keep preliminary specs in a separate feature list or catalog: the same file evolves from proposal to implementation-ready specification, preserving one identifier and one source of truth throughout its lifecycle.

A newly identified idea may start with only a summary, motivation, source documents, and `status: proposed`. Expand that same file in place as scope, tasks, and acceptance criteria become known. Never create a second document merely because the specification becomes more detailed.

When upgrading a repository that still has a legacy feature catalog, migrate every unique entry to a proposed SPEC file, preserve its original source links, and remove the catalog after verifying that no proposal was lost.

Unlike other document types, a spec is plain YAML, not Markdown with front matter. Minimum fields:

```yaml
id: SPEC-014
title: Support multi-backend export
status: proposed        # draft | proposed | ready | submitted | closed | rejected | superseded
approval: pending       # pending | approved
publication: unpublished # unpublished | published
type: feature            # feature | bug | task | chore
scope: catalog            # canonical functional or technical scope
platform: web             # identifier defined in the project ontology
delivery:
  group: 1                # fully completed before the next group starts
  order: 2                # SPEC order within the group
labels: [backend, export]
assignees: []
milestone: null
summary: |
  High-level description of the proposed work.
motivation: |
  Why the work is worth considering and which source documents led to it.
sources:
  - ../decisions/ADR-003-multi-backend.md
body: null               # may be null for draft/proposed; required and complete for ready+
depends_on: []           # mandatory prerequisite SPEC ids; not informational links
relations:
  parent: null            # SPEC-xxx, maps to a GitHub sub-issue parent
  children: []             # SPEC-xxx list, maps to GitHub sub-issues
  related: []               # SPEC-xxx or #issue, non-hierarchical cross-reference
github:
  issue: null              # owner/repo#123, set once the issue exists
  synced_at: null
implementation:
  state: not_started     # not_started | partial | verified | completed | blocked
  branch: null
  checkpoint_commit: null
  spec_revision: null    # immutable blob/hash or commit identifying reviewed SPEC content
  checks: []             # command, commit, result, and optional evidence reference
  review: null           # reviewer, head_commit, verdict, cycle, findings reference
  blocker: null
  integration:
    target: null
    pull_request: null
    merge_commit: null
    tag: null
closure:
  reason: null           # completed | cancelled | duplicate | obsolete | other
  note: null
updated: ...
```

Use statuses consistently:

* `draft`: the file is being authored and is not yet coherent enough for review;
* `proposed`: the work is a reviewable proposal but has not yet been approved as implementation-ready;
* `ready`: the proposal is approved and the scope, tasks, dependencies, and acceptance criteria are complete enough to implement;
* `submitted`: compatibility status for an approved spec published as a GitHub issue; it remains executable;
* `closed`: the work is no longer active; `closure.reason` distinguishes completed work from cancellation, duplication, obsolescence, or another reason;
* `rejected`: the proposal was considered and declined;
* `superseded`: another SPEC replaced this one; reference the replacement in `relations.related`.

Moving a SPEC to `ready` requires both sufficient detail and explicit approval in the user request or consolidated project documentation. Expanding a SPEC does not by itself imply approval; keep it `proposed` when it is detailed but still awaiting a decision.

Approval, publication, execution, and closure are separate dimensions. New or migrated files record `approval` and `publication` explicitly while retaining the legacy `status` field for compatibility: `ready` means approved/unpublished and `submitted` means approved/published. Both are eligible for implementation. Publishing changes only `publication`, GitHub metadata, and the compatible status projection; it never revokes approval. `implementation.state` tracks delivery progress, and `closed` requires `closure.reason`; only `closure.reason: completed` proves successful completion. When migrating older files, infer only deterministic values (`ready` -> approved/unpublished, `submitted` -> approved/published); leave ambiguous closure reasons for review rather than guessing.

`depends_on` contains only mandatory prerequisite SPEC ids. `relations.related` remains an informational cross-reference and must never be promoted automatically. Dependencies must resolve, contain no self-reference or cycle, and agree with `delivery.group` and `delivery.order`: a prerequisite cannot be scheduled after its dependent. A contradiction blocks readiness or implementation.

Maintain one `specs-index` at the path defined by the configured backend. It is a navigation and sequencing projection, not another source of specification content. Organize every SPEC exactly once using this hierarchy:

1. **implementation group** (`delivery.group`), in ascending numeric order;
2. **scope** (`scope`), using a stable canonical identifier;
3. **order within the group** (`delivery.order`), ascending even across different scopes.

The group is a global execution barrier: all selected ready SPECs in group 1, regardless of scope, must be implemented and integrated before code is generated for group 2, and so on. SPECs in the same group remain sequential unless parallel work is explicitly requested and dependency-compatible. `delivery.group` and `delivery.order` must be positive integers and the pair must be unique across the whole index; declared dependencies and delivery order must not conflict. SPECs that cannot yet be planned may use `null` values and belong in a final **Unplanned** section grouped by scope; they cannot become `ready` until scope, platform, group, and order are defined.

Each entry contains only the SPEC id linked to its canonical document, title, platform, type, compatible status, approval, publication, implementation state, group, order, and updated date. These fields remain visible but do not determine the index's primary grouping. Never copy summary, motivation, body, tasks, acceptance criteria, or checkpoint evidence into the index. Create the index with the first SPEC and update it whenever a projected field changes. The general memory `index` links to `specs-index`; it does not enumerate individual SPECs.

Reference other specs in `relations` by their `id`, so links stay valid before any issue exists. Resolve them to real issue numbers only when publishing, by looking up each referenced spec's `github.issue`.

Publishing a spec as a GitHub issue (or updating one already published) is **never automatic**: do it only on explicit request, and only for specs with `status: ready`. When publishing:

1. resolve `relations.parent`, `relations.children`, and `relations.related` against the `github.issue` of the referenced specs; flag any still unresolved instead of guessing;
2. create or update the issue with `title`, `body`, `labels`, `assignees`, `milestone`;
3. set the parent/children relationship through GitHub's native sub-issues feature; render `related` as a cross-reference list inside the issue body, since GitHub has no native non-hierarchical link type;
4. write `github.issue` and `github.synced_at`, set `publication: published`, preserve `approval: approved`, project the compatible `status: submitted`, and update the index;
5. verify the real outcome by rereading the issue through the connector or API, and report which issues were created or updated, with links.

This publishing step is a real, externally visible action — it is not covered by the automatic documentation updates in [Limits](#limits); treat it like any other action visible to others.

## Implementing specifications

Implementing code from SPECs is never automatic. Start only on explicit request and only when `approval: approved`; compatible `ready` and `submitted` files both qualify. Keep each repository in an independent session.

### Batches, plans, and branches

Group the SPECs selected for one implementation run into a **batch**, identified by `BATCH_ID` in `<YYYYMMDD>-<HHmm>` format (the run's own start date and time, e.g. `20261026-1430`). A batch may cover one SPEC or several; it is a unit of planning and review, not a new approval state, and it never encodes the included SPEC ids or ranges — the plan document does.

Before any code changes, a scouting pass produces exactly one reviewable low-level plan for the whole batch at `repodoc/plans/<BATCH_ID>.md`, committed to a dedicated `feature/batch-<BATCH_ID>` branch. Validate `depends_on`, `relations.related`, `delivery.group`/`delivery.order`, and ontology-backed platform suffixes once for the entire batch here, not once per SPEC. For every SPEC in the batch, the plan also reconciles existing state (checkpoint, local/remote branch, PR/merge/tag) into the `absent`/`partial`/`satisfied`/`ambiguous` classification, and lists the concrete files and changes anticipated. Do not start implementation until the plan branch exists and has been reviewed; publishing it is a real action visible to others, like any other.

Each SPEC keeps its own dedicated implementation branch, `feature/<lowercase-spec-id>-<title-slug>`. Once every SPEC in the batch has a pushed implementation, review happens on a dedicated `review/batch-<BATCH_ID>` branch against the batch's aggregated diff. A fix cycle for one SPEC's findings stays scoped to that SPEC's branch and triggers a re-review of only that changed diff, never a re-review of the whole batch.

### Keeping SPECs small

Keep each SPEC small enough for one fresh worker to implement in a single pass: a handful of files, one coherent change. When implementing reveals that the real scope is substantially larger than planned — a distinct component, or an infrastructure piece that a pipeline depends on and makes sense to build together with it — stop and report it as a new SPEC to create by hand, linked through `relations.parent`/`relations.children`, rather than silently expanding the current SPEC or the batch plan. Decomposing proposed work into such parent/child SPECs is always a human decision; no agent creates one unprompted.

Within that scope, favor minimal, single-responsibility changes: touch only what the SPEC requires, keep functions and classes small and focused, and avoid unrelated refactors. The reviewer checks for this alongside correctness.

Tasks and subtasks in the SPEC are the canonical functional plan. Do not duplicate them elsewhere. The `implementation` block is only a resumability checkpoint, owned by the orchestrator and updated in the active RepoDoc write mode after every meaningful step, not by the implementation worker on its code branch. It records at least branch, checkpoint commit, SPEC revision, checks and results tied to a commit, independent review, blocker, and PR/merge/tag references. Checkboxes alone are not evidence. `partial` means unfinished work, `verified` means implementation and review passed but target integration is not verified, and `completed` requires verified target integration.

Before changing code, compare the SPEC with existing implementation and tests; the batch plan already carries this classification, so reuse it instead of recomputing it per SPEC. Implement only gaps. Already-satisfied work receives evidence and required checks without artificial changes or commits. On resume, reconcile the SPEC revision, checkpoint, code, local and remote Git/PR/tag state; reuse matching evidence and repeat checks invalidated by later changes. This makes interruption between merge, tag, and memory update idempotent.

For multiple SPECs, resolve and order them by mandatory `depends_on`, then `delivery.group` and `delivery.order`; stop on missing dependencies, cycles, contradictions, or ambiguity. Process one at a time from the updated target and stop at the first blocker. Use a dedicated branch and a fresh isolated implementation worker for each SPEC. Once the batch's SPECs are implemented, launch a fresh `repodoc-review-spec-worker` for the batch's exact reviewed commits on `review/batch-<BATCH_ID>`. The reviewer is read-only and checks acceptance coverage, correctness/regressions, architecture/dependency boundaries, tests, SPEC-size and single-responsibility drift, and unrelated changes, returning blocking findings, observations, and verifiable references per SPEC.

Blocking findings return to the implementer of the affected SPEC; affected checks run again and the changed commit receives a new independent review scoped to that SPEC. The review-cycle limit is configurable and defaults to 3 per SPEC. At the limit preserve the branch and checkpoint and report the blocker.

The default integration policy is `pull-request` (pull request): open/update a dedicated PR and do not merge. `direct-merge` is allowed only when the request explicitly authorizes it; selection-wide authorization applies to every selected SPEC without repeated prompts. Do not globally change the default target: use `develop` only when requested or conventional. Before pushing a target that triggers deployment, obtain any additional authorization required by repository policy.

After a passing review, preserve the SPEC boundary in history, preferring a merge commit unless conventions differ. Verify required checks on the integrated target, push and verify the remote merge, then create and push an annotated completion tag on the resulting commit. Use repository naming, otherwise `spec/<lowercase-spec-id>/completed`. Never overwrite, move, force, or reuse an existing tag; verify it remotely. A completion tag identifies SPEC completion, not a release or deployment. Only then set `implementation.state: completed`, record merge/tag, set `closure.reason: completed` and compatible `status: closed`, and update the index. Never discard unrelated work or claim an end-to-end proof from static template checks.

## Consultation order

For questions about project state, consult the configured memory backend first. Reliability order:

1. consolidated documentation in the backend;
2. the current conversation;
3. memory of previous conversations.

If the current conversation conflicts with the documentation, verify that it represents a new decision before updating the backend.

## Memory backend

This project uses **a single backend** as persistent memory. The configured backend's specific operating rules follow from here.

## Automatic behavior

The user does not need to request a memory update each time.

When clearly established and relevant knowledge emerges:

1. consult the existing documentation;
2. determine where to record it;
3. prefer updating an existing document;
4. create a new document only when necessary;
5. update relevant indexes and links;
6. check that the content you are about to write is consistent with the existing documentation; if you find an inconsistency (conflicting data, contradictory decisions, different terminology), flag it explicitly and ask how to resolve it before saving;
7. save the update following the configured backend's rules;
8. briefly report what was recorded.

Do not repeatedly interrupt the conversation to ask whether each item should be saved. Distinguish temporary brainstorming from established knowledge autonomously.

## Limits

You may automatically modify only **project documentation and memory**. Code, infrastructure, pipelines, dependencies, databases, operational configuration, scripts, and other executable artifacts require an explicit request.

This autonomy applies exclusively to automatic project-memory and documentation updates managed by RepoDoc. It does not extend to every kind of project change and does not authorize autonomous changes to code, infrastructure, pipelines, dependencies, databases, configuration, scripts, or other executable artifacts, regardless of the configured backend.

## Goal

Maintain reliable, concise, current, versioned, linked memory. **Chat is for thinking; the configured backend is for remembering; history stays preserved; the backend's review flow keeps memory evolving.**
