---
name: RepoDoc - Expand all specs
description: Expands all or selected draft/proposed repodoc/specs/SPEC-*.yaml files in place with detailed, evidence-backed implementation content.
---

Read the current `repodoc/memory-protocol.md`. Enumerate existing `repodoc/specs/SPEC-*.yaml` files with status `draft` or `proposed`, limited to a user-selected subset when given. Resolve the write mode once: Copilot CLI in the active working tree or chat through the persistent PR.

Process each SPEC sequentially as an isolated task. Re-read related project, architecture, ontology, REQ, ADR, OPEN, research, knowledge, and SPEC documents. Update the same YAML file with supported problem/context, proposal, scope and out of scope, ontology-backed platform, delivery group/order, boundaries, ordered activities, atomic subtasks, objective acceptance criteria, dependencies and relations, related documents, and readiness notes. Preserve its id and path; never create a catalog or replacement representation and never invent unresolved decisions. Update `repodoc/specs/index.md` in the same operation so every SPEC appears exactly once by scope, implementation group, and order, and ensure `repodoc/index.md` links to it. In CLI do not create branches, commits, pushes, or PRs; in chat follow the persistent PR.

Expanding is not approval: keep `draft` until reviewable; use `proposed` when reviewable or complete but awaiting approval; use `ready` only when complete and explicitly approved by the user or consolidated documentation. Never publish an issue and keep GitHub fields null.

Continue past incomplete specs, verify final files and the applicable persistence, and report statuses, missing information or approval, skips, changed files, and confirmation that no issue was published.
