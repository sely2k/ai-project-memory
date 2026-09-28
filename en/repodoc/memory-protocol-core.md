<!-- repodoc:version 1.9.0 -->

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
* `REQ-xxx-<title>`: requirements;
* `OPEN-xxx-<title>`: open questions;
* `ADR-xxx-<title>`: decisions;
* `SPEC-xxx-<title>`: specifications, including proposed work (one YAML file per spec, see [Specifications](#specifications));
* `specs-index`: the navigational index of every SPEC, grouped by lifecycle status;
* `research`: research;
* `knowledge`: stable, consolidated knowledge — not proposed or planned work, which belongs in `SPEC-xxx-<title>` files.

Create these documents only when needed. The concrete location of each type (file path, folder, or page) depends on the configured backend: see [Memory backend](#memory-backend).

## Linked knowledge base

Create focused, indexed documents connected to one another. Avoid oversized content, excessive fragmentation, and duplication; keep one primary source for each piece of information. The concrete linking mechanism depends on the configured backend.

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
type: feature            # feature | bug | task | chore
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
relations:
  parent: null            # SPEC-xxx, maps to a GitHub sub-issue parent
  children: []             # SPEC-xxx list, maps to GitHub sub-issues
  related: []               # SPEC-xxx or #issue, non-hierarchical cross-reference
github:
  issue: null              # owner/repo#123, set once the issue exists
  synced_at: null
updated: ...
```

Use statuses consistently:

* `draft`: the file is being authored and is not yet coherent enough for review;
* `proposed`: the work is a reviewable proposal but has not yet been approved as implementation-ready;
* `ready`: the proposal is approved and the scope, tasks, dependencies, and acceptance criteria are complete enough to implement;
* `submitted`: the spec has been published as a GitHub issue;
* `closed`: the work has been completed or otherwise closed;
* `rejected`: the proposal was considered and declined;
* `superseded`: another SPEC replaced this one; reference the replacement in `relations.related`.

Moving a SPEC to `ready` requires both sufficient detail and explicit approval in the user request or consolidated project documentation. Expanding a SPEC does not by itself imply approval; keep it `proposed` when it is detailed but still awaiting a decision.

Maintain one `specs-index` at the path defined by the configured backend. It is a navigational projection, not another source of specification content. Group every SPEC exactly once under:

* **Proposals**: `draft`, `proposed`;
* **Ready**: `ready`;
* **Published**: `submitted`;
* **Closed**: `closed`;
* **Archived**: `rejected`, `superseded`.

Each entry contains only the SPEC id linked to its canonical document, title, type, status, and updated date. Never copy summary, motivation, body, tasks, or acceptance criteria into the index. Create the index with the first SPEC and update it whenever a SPEC is created, renamed, changes status, or is removed. The general memory `index` links to `specs-index`; it does not enumerate individual SPECs.

Reference other specs in `relations` by their `id`, so links stay valid before any issue exists. Resolve them to real issue numbers only when publishing, by looking up each referenced spec's `github.issue`.

Publishing a spec as a GitHub issue (or updating one already published) is **never automatic**: do it only on explicit request, and only for specs with `status: ready`. When publishing:

1. resolve `relations.parent`, `relations.children`, and `relations.related` against the `github.issue` of the referenced specs; flag any still unresolved instead of guessing;
2. create or update the issue with `title`, `body`, `labels`, `assignees`, `milestone`;
3. set the parent/children relationship through GitHub's native sub-issues feature; render `related` as a cross-reference list inside the issue body, since GitHub has no native non-hierarchical link type;
4. write the resulting `github.issue` and `github.synced_at` back into the YAML file, move `status` to `submitted`, and move its entry to Published in `specs-index`;
5. verify the real outcome by rereading the issue through the connector or API, and report which issues were created or updated, with links.

This publishing step is a real, externally visible action — it is not covered by the automatic documentation updates in [Limits](#limits); treat it like any other action visible to others.

## Implementing specifications

Implementing code from SPECs is never automatic. Start only on explicit request and only from `ready` SPECs. Keep implementation separate from the persistent-memory review flow: the configured backend defines how code branches, pull requests, and merges are handled.

For a request covering multiple SPECs, use an orchestrator/worker model:

1. resolve the selected SPECs from `specs-index` and their canonical files;
2. validate that every selected SPEC is `ready`, all referenced prerequisites exist, and the execution order respects their dependencies;
3. process them sequentially unless the user explicitly requests parallel work and the repository can provide isolated worktrees and non-overlapping integration paths;
4. launch a fresh isolated implementation worker for each SPEC; the orchestrator coordinates but never writes implementation code itself;
5. give the worker only one SPEC, its relevant source context, the target branch, and the requested integration policy;
6. require the worker to implement, test, commit, and verify that SPEC without silently introducing decisions absent from the specification;
7. independently verify the worker's reported branch, commits, tests, and integration result before starting the next SPEC;
8. stop the train on the first unresolved decision, unrepairable verification failure, or incomplete integration, unless the user explicitly authorizes skipping that SPEC.

Every worker invocation must start with a fresh context. Never reuse one implementation worker across multiple SPECs and never fall back to inline implementation when isolated delegation is required but unavailable.

The default integration policy is `pull-request`: a dedicated branch plus pull request with no automatic merge. `direct-merge` into a shared target branch is allowed only when the current user request explicitly authorizes it. Never discard unrelated local changes, overwrite another worker's branch, or treat command success as proof: reread the resulting repository and hosting state.

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
