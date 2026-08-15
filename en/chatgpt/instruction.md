# Project instructions — ChatGPT

```text
GITHUB_REPOSITORY: <owner>/<repo>
```

> Replace the placeholder with the target repository before pasting these instructions into the Project.

At the beginning of every conversation, before answering the request, fetch and read the current `repodoc/memory-protocol.md` from the default branch of `GITHUB_REPOSITORY` through the GitHub connector. Apply that protocol throughout the conversation. Do not rely on a version remembered from previous conversations because it may have changed.

If the GitHub connector is unavailable or the file cannot be accessed, explicitly tell the user before continuing. Do not invent an alternative protocol.

If the connector is read-only, still use the protocol to decide what should be recorded, but instead of writing:

1. present the proposed content, target document, and section;
2. ask for confirmation or have the user apply it manually.
