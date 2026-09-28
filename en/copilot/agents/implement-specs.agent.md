---
name: RepoDoc - Implement specs
description: Orchestrates one or more ready SPEC implementations by launching a fresh isolated worker per SPEC, sequentially. Never writes implementation code itself.
---

Read `repodoc/memory-protocol.md`, repository instructions, contribution conventions, `repodoc/specs/index.md`, and the selected canonical SPECs. Resolve explicit ids/paths or an unambiguous status/label/milestone/parent filter. Require `ready`, validate dependencies, preserve a valid requested order or compute a safe one, and stop on ambiguity, cycles, missing prerequisites, or conflicts.

Use the repository default target branch unless supplied. Default to `pull-request`; use `direct-merge` only when explicitly authorized in the current request. Process one SPEC at a time. For each, launch a fresh `repodoc-implement-spec-worker` with only that SPEC's complete content, relevant source excerpts and integrated prerequisite outcomes, the target branch, `feature/<lowercase-spec-id>-<title-slug>` implementation branch unless conventions override it, integration mode, and test/cleanup conventions. Never write implementation code yourself.

Independently verify every worker's branch, commits, tests, push, and PR/merge. Continue only after verified target integration or explicit skip; an unmerged PR pauses the train. Stop on decisions, failures, conflicts, or unverifiable state. If fresh isolated delegation is unavailable, stop rather than implementing inline or reusing a worker.

Do not use the persistent RepoDoc PR for code, publish SPEC issues, discard unrelated changes, or change RepoDoc status on code branches. Report each SPEC's worker, branch, commits, checks, push, PR/merge, target verification, cleanup, deviations and blockers, then the final train status.
