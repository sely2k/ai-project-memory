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
| `index` | `repo-docs/index.md` |
| `project` | `repo-docs/project.md` |
| `architecture` | `repo-docs/architecture.md` |
| `glossary` | `repo-docs/glossary.md` |
| `REQ-xxx-<title>` | `repo-docs/requirement/REQ-xxx-<title>.md` |
| `OPEN-xxx-<title>` | `repo-docs/openpoint/OPEN-xxx-<title>.md` |
| `ADR-xxx-<title>` | `repo-docs/decisions/ADR-xxx-<title>.md` |
| `specs` | `repo-docs/specs/` |
| `research` | `repo-docs/research/` |
| `knowledge` | `repo-docs/knowledge/` |

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
