---
name: repodoc-spec-expand
description: Transforms a single high-level entry of the repodoc/specs/features.md catalog into a complete SPEC-xxx-<title>.yaml file conforming to the RepoDoc protocol. Use this skill when the user asks to detail, expand, or formalize a spec from the catalog.
---

# RepoDoc — Expand a high-level spec

## When to use it

When the user asks to turn a catalog entry from `repodoc/specs/features.md` (typically produced by the `repodoc-synthesize-specs` agent) into a complete YAML spec, ready to eventually become a GitHub issue.

## Required parameters

- `SPEC_NUMBER`: the spec's identifier as it appears in the catalog (e.g. `SPEC-003`).
- `SPEC_TITLE`: the spec's short title as it appears in the catalog.

If the user does not provide both values, ask for them before proceeding. If they provide only one (or an ambiguous reference), read `repodoc/specs/features.md` to infer the other; if the entry is not unambiguous, ask for confirmation instead of guessing.

## Operating instructions

Execute the following task, substituting `SPEC_NUMBER` and `SPEC_TITLE` with the values gathered:

---

In the `GITHUB_REPOSITORY` repository, apply the current version of `repodoc/memory-protocol.md`.

Transform `SPEC_NUMBER` (`SPEC_TITLE`), currently synthesized in `repodoc/specs/features.md`, into a precise, complete YAML spec conforming to the protocol.

Before writing:

- consult `repodoc/project.md`, `repodoc/architecture.md`, and every requirement, ADR, open point, research note, and document related to the SPEC;
- check the current state of the repository and of the persistent RepoDoc PR;
- respect naming, responsibilities, and dependency boundaries already established;
- preserve any naming or intentionally consolidated wording found in authoritative documents;
- do not arbitrarily introduce technical decisions that are still open.

The YAML spec must include at least:

- problem and context;
- proposal;
- scope and out of scope;
- relevant rules, responsibilities, and dependency boundaries;
- detailed, ordered implementation activities;
- specific, atomic, verifiable subtasks;
- objective acceptance criteria, ideally tied to commands, exit codes, tests, or observable checks;
- dependencies and relations to other SPECs;
- related documentation;
- readiness notes precisely stating any decisions still missing.

Manage the SPEC's status based on the documentary evidence:

- keep it `draft` if decisions, prerequisites, or essential details remain unresolved;
- set it to `ready` only if every criterion required by the protocol is clearly satisfied;
- do not publish it as a GitHub issue;
- leave `github.issue: null` and `github.synced_at: null`.

Update `repodoc/specs/features.md` so the old synthesized entry is replaced with a link to the new canonical YAML file, removing the duplication without altering the other SPECs.

Manage the update through the persistent RepoDoc PR required by the protocol:

1. search for every open PR whose title exactly matches the expected format;
2. if exactly one exists, reuse its branch;
3. if none exists, create the branch and PR following the protocol;
4. if more than one exists, stop and ask which one to use;
5. create small, coherent commits;
6. update the PR description to include the new SPEC;
7. do not merge.

Actually verify, by rereading GitHub after the changes:

- the content and SHA of the new YAML file;
- the `draft` or `ready` status;
- the presence of activities, subtasks, and acceptance criteria;
- the absence of the old duplication in `features.md`;
- the presence of the new link in the catalog;
- the commits present on the branch;
- the state, title, branch, and content of the persistent PR;
- the absence of a GitHub issue for the SPEC.

At the end, report concisely:

- files created or modified;
- the status assigned to the SPEC and why;
- the number of activities and subtasks;
- commits created;
- link to the persistent PR;
- the outcome of the verifications;
- confirmation that no issue was created.

---

## Notes

- This skill never publishes GitHub issues: that remains an explicit, separate step, defined in the protocol's "Specifications" section, only for SPECs with `status: ready` and only on explicit request.
- If the configured backend is not GitHub, the persistent-PR flow described above does not apply: follow the configured backend's writing flow described in `repodoc/memory-protocol.md` instead.
