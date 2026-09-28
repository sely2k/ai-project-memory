---
name: RepoDoc - Synthesize specs
description: Identifies future work from consolidated project knowledge and records it directly as minimal SPEC YAML proposals with status proposed.
---

Read the current `repodoc/memory-protocol.md`. Starting from the OPEN, ADR, REQs, or other consolidated source named by the user, identify concrete future work. If none is named, infer the source from current changes in the active mode or ask.

Search every existing `repodoc/specs/SPEC-*.yaml`, regardless of status, and skip semantic duplicates. Assign the next sequential SPEC id. Create one minimal YAML file per proposal with `status: proposed`, a concise summary, motivation, source-document references, null GitHub fields, and only evidence-backed detail. Do not invent tasks, scope, or acceptance criteria, and do not create a feature catalog. Create or update `repodoc/specs/index.md`, placing every SPEC exactly once in its lifecycle section, and ensure `repodoc/index.md` links to that specialized index.

Follow the protocol's write mode: in Copilot CLI use the existing working tree and branch without creating branches, commits, pushes, or PRs; when invoked from chat, use the persistent PR. Verify the actual result. Do not publish issues or modify non-documentation artifacts. Report the trigger, proposals, duplicates, files, and persistence result.
