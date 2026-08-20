<!-- repodoc:version 1.1.0 -->

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
* `specs`: specifications;
* `research`: research;
* `knowledge`: stable knowledge.

Create these documents only when needed. The concrete location of each type (file path, folder, or page) depends on the configured backend: see [Memory backend](#memory-backend).

## Linked knowledge base

Create focused, indexed documents connected to one another. Avoid oversized content, excessive fragmentation, and duplication; keep one primary source for each piece of information. The concrete linking mechanism depends on the configured backend.

## Metadata

When useful, `knowledge`, `decision`, `research`, and `specs` documents may carry metadata with:
- `title`
- `updated`
- `related`
- `status` (`draft`, `active`, `deprecated`, or `superseded`).
- `tag`

`openpoint` documents use the same metadata, but with `status` (`open` or `resolved`).

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
6. save the update following the configured backend's rules;
7. briefly report what was recorded.

Do not repeatedly interrupt the conversation to ask whether each item should be saved. Distinguish temporary brainstorming from established knowledge autonomously.

## Limits

You may automatically modify only **project documentation and memory**. Code, infrastructure, pipelines, dependencies, databases, operational configuration, scripts, and other executable artifacts require an explicit request.

This autonomy applies exclusively to automatic project-memory and documentation updates managed by RepoDoc. It does not extend to every kind of project change and does not authorize autonomous changes to code, infrastructure, pipelines, dependencies, databases, configuration, scripts, or other executable artifacts, regardless of the configured backend.

## Goal

Maintain reliable, concise, current, versioned, linked memory. **Chat is for thinking; the configured backend is for remembering; history stays preserved; the backend's review flow keeps memory evolving.**
