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
| `specs-catalog` | `repodoc/specs/features.md` |
| `research` | `repodoc/research/` |
| `knowledge` | `repodoc/knowledge/` |

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

### Persistent pull request

**Do not modify the main branch directly.**

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

### Commits

Create small, coherent commits grouped by concept, for example:

```text
docs: record authentication decision
```

### Publishing specs as issues

Only when explicitly requested, for a `SPEC-xxx-<title>` file with `status: ready`:

1. Check the write access of the active GitHub connector for issues (not just files/commits). If it cannot write, do not fake the publish: state precisely which permission is missing and ask for it to be enabled.
2. Resolve `relations.parent`, `relations.children`, and `relations.related` by looking up the `github.issue` of each referenced spec.
3. Create the issue (`gh issue create --title ... --body-file ... --label ... --assignee ... --milestone ...`), or update it with `gh issue edit` if `github.issue` is already set.
4. Set the parent/children relationship through GitHub's native sub-issues feature; render `relations.related` as a `Related: #...` list inside the issue body, since GitHub has no native non-hierarchical link type.
5. Write `github.issue` and `github.synced_at` back into the YAML file and set `status: submitted`.
6. Verify the real outcome by rereading the issue through the connector or API, and report the created/updated issue links.

### RepoDoc agents

For this backend, the installer can copy dedicated agents that run parts of this protocol autonomously, each in the native format of the selected tool (Claude Code, Codex, GitHub Copilot):

- **Consistency check** (`repodoc-consistency-check`): audits the entire memory backend for contradictions, broken links, duplication, and stale status fields.
- **Close open point** (`repodoc-close-openpoint`): reads an `OPEN-xxx-<title>` and tries to resolve it by gathering evidence.
- **Synthesize specs** (`repodoc-synthesize-specs`): once a situation closes, records future work as high-level entries in `repodoc/specs/features.md`.
- **Expand spec** (`repodoc-spec-expand` skill): turns a single catalog entry into a complete `SPEC-xxx-<title>.yaml` file, on the user's specific request.
- **Expand all specs** (`repodoc-expand-specs`): walks the `repodoc/specs/features.md` catalog entry by entry and formalizes each into a complete `SPEC-xxx-<title>.yaml` file. On Claude Code it delegates each single expansion to the `repodoc-expand-spec-worker` sub-agent (invoked via the Task tool, never in parallel, on the same persistent-PR branch); on Codex and Copilot, which offer no mechanism to invoke isolated sub-agents, it applies the same procedure inline, one entry at a time.

All of them follow the "Persistent pull request" flow described above, which is why they are only installed for the GitHub backend.
