# Persistent memory protocol

This is the protocol's single source of truth. Do not duplicate it elsewhere: the other files in this language package must only reference it.

This project uses a GitHub repository as the **persistent memory and source of truth** for consolidated information.

```text
GITHUB_REPOSITORY: <owner>/<repo>
```

> Replace the placeholder with the target project repository before use.

Chat is temporary working memory; GitHub is persistent, structured, versioned memory.

## What to remember

Use chat freely for brainstorming, hypotheses, comparisons, and temporary reasoning.

When information becomes important and sufficiently established, record it in the repository. This includes:

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

## Structure

Adapt to the existing structure. Do not create unnecessary files, directories, or equivalent documents.

* `README.md`: overview; `AGENTS.md`: operational instructions only.
* `repo-docs/index.md`: index; `project.md`: context and requirements; `architecture.md`: architecture; `glossary.md`: terminology; `backlog.md`: open items.
* `repo-docs/decisions/ADR-xxx-<title>.md`: ADRs; `specs/`: specifications; `research/`: research; `knowledge/`: stable knowledge.

Create these files only when needed.

## Linked knowledge base

In `repo-docs/`, create focused, indexed documents connected by relative links. Avoid oversized files, excessive fragmentation, and duplication; keep one primary source for each piece of information.

## Metadata

When useful, files under `knowledge`, `research`, and `specs` may use front matter with `title`, `updated`, `related`, and `status` (`draft`, `active`, `deprecated`, or `superseded`). Do not add unnecessary metadata.

## Updating knowledge

Documentation should primarily describe the **current state**.

When a decision changes:

1. identify the affected documents;
2. update the current documentation;
3. create or update an ADR when needed;
4. update links and indexes.

Do not retain obsolete information in current documents merely to preserve history: **Git keeps the history; documentation describes the current state.**

## ADRs

Create ADRs only for significant decisions. Heading: `# ADR-XXX - Title`. Minimum sections: `Status`, `Context`, `Decision`, `Rationale`, `Alternatives`, `Consequences`, `Related`.

## Consultation order

For questions about project state, consult the repository first. Reliability order:

1. consolidated repository documentation;
2. the current conversation;
3. memory of previous conversations.

If the current conversation conflicts with the documentation, verify that it represents a new decision before updating the repository.

## Persistent pull request

**Do not modify the main branch directly.**

Use the GitHub PR number without leading zeros. Valid title:

```regex
^repodoc/[1-9][0-9]*-ProjectMemory$
```

Before writing, find an open matching PR and use its branch.

If none exists, create `repodoc/project-memory-<YYYYMMDD-HHMMSS>` from the updated default branch, open the PR as `repodoc/pending-ProjectMemory`, then immediately rename it to `repodoc/<PR_NUMBER>-ProjectMemory`.

Keep and reuse this PR. If several matching PRs exist, list them and ask which one to use. If it is closed or merged, create a new one.

**Do not merge the PR autonomously.**

If the current tool cannot write to the repository, do not pretend the operation succeeded: propose the content to record and ask the user to apply it manually.

## Commits

Create small, coherent commits grouped by concept, for example:

```text
docs: record authentication decision
```

## Automatic behavior

The user does not need to request a memory update each time.

When clearly established and relevant knowledge emerges:

1. consult the existing documentation;
2. determine where to record it;
3. prefer updating an existing document;
4. create a new document only when necessary;
5. update relevant indexes and links;
6. commit to the branch associated with `repodoc/<PR_NUMBER>-ProjectMemory`;
7. briefly report what was recorded.

Do not repeatedly interrupt the conversation to ask whether each item should be saved. Distinguish temporary brainstorming from established knowledge autonomously.

## Limits

You may automatically modify only **project documentation and memory**. Code, infrastructure, pipelines, dependencies, databases, operational configuration, scripts, and other executable artifacts require an explicit request.

## Goal

Maintain reliable, concise, current, versioned, linked memory. **Chat is for thinking; the repository is for remembering; Git preserves history; `repodoc/<PR_NUMBER>-ProjectMemory` keeps memory evolving.**
