---
name: repodoc-spec-expand
description: Expands one existing draft or proposed repodoc/specs/SPEC-xxx-<title>.yaml file in place. Use when the user asks to detail, refine, or formalize a specific SPEC.
---

# RepoDoc — Expand one SPEC

## Required input

Identify one existing SPEC from the user's id, title, or path. Search `repodoc/specs/SPEC-*.yaml` to resolve a partial reference. Ask only if it remains ambiguous. Do not create a new SPEC through this skill; proposal creation belongs to `repodoc-synthesize-specs`.

## Instructions

Read the current `repodoc/memory-protocol.md` and the selected SPEC. Confirm its status is `draft` or `proposed`, then consult `project.md`, `architecture.md`, and all related REQs, ADRs, OPENs, research notes, SPECs, and knowledge documents.

Enrich the same YAML file with evidence-backed problem/context, proposal, scope and out of scope, boundaries, ordered activities, atomic subtasks, objective acceptance criteria, dependencies and relations, related documentation, and readiness notes. Preserve its id and path. Do not create a feature catalog, replacement document, or unsupported technical decision.

Update `repodoc/specs/index.md` in the same change so the SPEC appears exactly once in the lifecycle section matching its resulting status. Ensure `repodoc/index.md` links to this specialized index.

Apply status rules exactly:

- keep `draft` while the SPEC is not coherent enough for review;
- set `proposed` when it is reviewable, even if fully detailed but still awaiting approval;
- set `ready` only when every required detail is present and the user or consolidated documentation explicitly approves it;
- never publish an issue; leave `github.issue` and `github.synced_at` null.

Work in the existing working tree and active branch. Do not create or switch branches, create commits, push, or open or update PRs. Preserve unrelated changes and verify files, the local diff, and absence of a GitHub issue.

Report the modified file, resulting status and reason, activity/subtask counts, missing information or approval, and local verification outcome.
