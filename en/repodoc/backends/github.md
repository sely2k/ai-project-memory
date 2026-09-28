## Backend: GitHub

```text
GITHUB_REPOSITORY: <owner>/<repo>
```

> Replace the placeholder with the target project repository before use.

### Paths

| Type | Path |
|---|---|
| `README` | `README.md` |
| `AGENTS` | `AGENTS.md` |
| `index` | `repodoc/index.md` |
| `project` | `repodoc/project.md` |
| `architecture` | `repodoc/architecture.md` |
| `glossary` | `repodoc/glossary.md` |
| `REQ-xxx-<title>` | `repodoc/requirement/REQ-xxx-<title>.md` |
| `OPEN-xxx-<title>` | `repodoc/openpoint/OPEN-xxx-<title>.md` |
| `ADR-xxx-<title>` | `repodoc/decisions/ADR-xxx-<title>.md` |
| `SPEC-xxx-<title>` | `repodoc/specs/SPEC-xxx-<title>.yaml` |
| `specs-index` | `repodoc/specs/index.md` |
| `research` | `repodoc/research/` |
| `knowledge` | `repodoc/knowledge/` |

Proposed and fully detailed specifications use the same `repodoc/specs/SPEC-xxx-<title>.yaml` files. Do not create a separate feature catalog: use `status: proposed` for work awaiting approval and enrich the same file as it matures.

`repodoc/specs/index.md` groups links to all SPEC files by lifecycle status, using the sections defined by the core protocol. It contains only navigational metadata and must be updated atomically with every SPEC creation or lifecycle change. `repodoc/index.md` links to this specialized index rather than listing individual SPECs.

Use this shape, omitting table rows when a section is empty but keeping all section headings:

```markdown
# Specifications

## Proposals
| SPEC | Title | Type | Status | Updated |
|---|---|---|---|---|
| [SPEC-014](./SPEC-014-support-multi-backend-export.yaml) | Support multi-backend export | feature | proposed | 2026-09-28 |

## Ready
## Published
## Closed
## Archived
```

### Links

Connect documents to one another with relative links.

### Metadata

Metadata goes in a YAML front matter block at the top of the file:

```yaml
---
title: ...
updated: ...
related: [...]
status: ...
tag: [...]
---
```

`SPEC-xxx-<title>` files are plain YAML, not Markdown with front matter: see [Specifications](../memory-protocol-core.md#specifications) in the core protocol for their schema.

### Write modes

Determine the mode from the environment that originated the work, not from the name of any delegated agent:

- **Local CLI** (Claude Code, Codex CLI, Copilot CLI, or equivalent launched by the user in the repository): edit files in the existing working tree and active branch. Do not create or switch branches, create commits, push, or open or update PRs. Preserve all unrelated changes, verify the result by rereading files and the local diff, and leave staging, commits, and integration to the user.
- **Remote chat** (ChatGPT Project, Claude Project, or a task delegated by that chat): use the persistent RepoDoc pull request described below. Delegating from chat to Codex remains chat mode and does not become CLI mode.

### Persistent pull request for chat

In chat mode, **do not modify the main branch directly.**

Use the GitHub PR number without leading zeros. Valid title:

```regex
^repodoc/[1-9][0-9]*-ProjectMemory$
```

Before writing, follow these steps in order:

1. **Find an open PR matching the title above.**
   - If exactly one matching PR exists, use its branch.
   - If several exist, list them and ask the user which one to use.
   - If the only matching PR is closed or merged, treat it as nonexistent and move to step 2.
2. **If no open matching PR exists, create one:**
   - from the updated default branch, create `repodoc/project-memory-<YYYYMMDD-HHMMSS>`;
   - open the PR with the provisional title `repodoc/pending-ProjectMemory`;
   - immediately rename the title to `repodoc/<PR_NUMBER>-ProjectMemory`.
3. **Check the write access of the active GitHub connector** (creating/modifying files and commits).
   - If the connector can write, proceed normally with document changes, commits, push, and PR updates.
   - If the connector cannot write, do not stop after preparing a patch and do not ask the user to apply it manually: start or use an alternative environment or agent connected to the repository with write access (for example a Codex task or equivalent), and complete the RepoDoc update autonomously with that environment.
   - If no environment with write access is available, do not create empty branches or PRs and do not pretend to write: state precisely which permission or tool is missing and ask for it to be enabled; once available, resume the workflow autonomously from where it stopped.
4. **Verify the real outcome of every operation** by rereading the actual state (commit, push, PR) through the connector or API, instead of trusting only the call's "success" return value.

Keep and reuse the same PR for subsequent updates, as long as it stays open.

**Do not merge the PR autonomously.**

### Chat commits

In chat mode, create small, coherent commits grouped by concept, for example:

```text
docs: record authentication decision
```

### Publishing specs as issues

Only when explicitly requested, for a `SPEC-xxx-<title>` file with `status: ready`:

1. Check the write access of the active GitHub connector for issues (not just files/commits). If it cannot write, do not fake the publish: state precisely which permission is missing and ask for it to be enabled.
2. Resolve `relations.parent`, `relations.children`, and `relations.related` by looking up the `github.issue` of each referenced spec.
3. Create the issue (`gh issue create --title ... --body-file ... --label ... --assignee ... --milestone ...`), or update it with `gh issue edit` if `github.issue` is already set.
4. Set the parent/children relationship through GitHub's native sub-issues feature; render `relations.related` as a `Related: #...` list inside the issue body, since GitHub has no native non-hierarchical link type.
5. Write `github.issue` and `github.synced_at` back into the YAML file, set `status: submitted`, and move the SPEC entry to Published in `repodoc/specs/index.md` in the same operation. In chat mode include everything in one persistent-PR commit; in CLI mode leave the updates in the working tree without creating a commit.
6. Verify the real outcome by rereading the issue through the connector or API, and report the created/updated issue links.

### Implementing specs as code

Use the repository's documented contribution conventions when they exist. Otherwise:

- resolve the target branch from the user's request; if none is given, use the repository's default branch;
- create `feature/<lowercase-spec-id>-<title-slug>` for each SPEC, for example `feature/spec-005-short-title`;
- prefer an isolated git worktree so the user's current checkout and unrelated changes remain untouched;
- in `pull-request` mode, push the branch and open a PR against the target branch, but do not merge it;
- in `direct-merge` mode, proceed only when the current request explicitly authorizes direct merge, then merge and push the target branch according to repository conventions;
- delete local or remote branches only when repository conventions or the user explicitly require cleanup, and only after verifying successful integration.

The persistent RepoDoc PR is not the implementation PR and must never be used as a code branch.

### RepoDoc agents

For this backend, the installer can copy dedicated agents that run parts of this protocol autonomously, each in the native format of the selected tool (Claude Code, Codex, GitHub Copilot):

- **Bootstrap** (`repodoc-bootstrap`): reads the repository, gathers only missing essential project facts one at a time, and creates the minimal initial memory using the active write mode.
- **Doctor** (`repodoc-doctor`): diagnoses installation, wrappers, agents, placeholders, links, indexes, and SPEC structure read-only, without changes or update checks.
- **Consistency check** (`repodoc-consistency-check`): audits the entire memory backend for contradictions, broken links, duplication, and stale status fields.
- **Close open point** (`repodoc-close-openpoint`): reads an `OPEN-xxx-<title>` and tries to resolve it by gathering evidence.
- **Synthesize specs** (`repodoc-synthesize-specs`): once a situation closes, records future work directly as minimal `SPEC-xxx-<title>.yaml` files with `status: proposed`.
- **Expand spec** (`repodoc-spec-expand` skill): enriches one existing draft or proposed SPEC in place, on the user's specific request.
- **Expand all specs** (`repodoc-expand-specs`): walks draft and proposed `SPEC-xxx-<title>.yaml` files and enriches each in place. The Claude Code template delegates each expansion to `repodoc-expand-spec-worker`; the Codex and Copilot templates currently apply the same procedure inline, one file at a time.
- **Implement specs** (`repodoc-implement-specs`): orchestrates a sequential implementation train and launches a fresh `repodoc-implement-spec-worker` for each ready SPEC. It never writes implementation code itself.
- **Implement spec worker** (`repodoc-implement-spec-worker`): implements exactly one assigned SPEC on its dedicated code branch, runs its verification, and integrates it only according to the requested policy. It is an internal worker and should not be reused across SPECs.

Memory-changing agents and the expansion skill follow the CLI or chat mode defined above; `repodoc-doctor` always remains read-only. Implementation agents follow the separate dedicated code-branch flow.
