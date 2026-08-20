## Backend: Google Docs

```text
GOOGLE_DRIVE_FOLDER: <GOOGLE_DRIVE_FOLDER>
```

> Replace the placeholder with the target project's Google Drive folder before use.

### Paths

Create one Google Doc per document type inside `GOOGLE_DRIVE_FOLDER`, titled `<Type> - <Title>` (e.g. "ADR-003 - Title").

### Links

Connect documents to one another with Google Docs' native links.

### Metadata

Since there is no native front matter, record metadata (`title`, `updated`, `related`, `status`) as the first lines of the document.

### Writing

If the active Google Drive/Docs connector cannot create or modify documents, do not pretend to write: state precisely which permission is missing and ask for it to be enabled.

The review flow (GitHub's persistent-PR equivalent) is not yet defined for this backend.
