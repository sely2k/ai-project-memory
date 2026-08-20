## Backend: Notion

```text
NOTION_PARENT_PAGE: <NOTION_PARENT_PAGE>
```

> Replace the placeholder with the target project's Notion parent page before use.

### Paths

Create one Notion page per document type under `NOTION_PARENT_PAGE`, titled `<Type> - <Title>` (e.g. "ADR-003 - Title").

### Links

Connect documents to one another with Notion's native links.

### Metadata

Use the page's properties (or a Notion database, if any) for `title`, `updated`, `related`, `status`, instead of YAML front matter.

### Writing

If the active Notion connector cannot create or modify pages, do not pretend to write: state precisely which permission is missing and ask for it to be enabled.

The review flow (GitHub's persistent-PR equivalent) is not yet defined for this backend.
