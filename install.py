# /// script
# requires-python = ">=3.11"
# dependencies = ["questionary>=2.1,<3"]
# ///

SOURCE_REPOSITORY = "https://github.com/sely2k/ai-project-memory"
SOURCE_BRANCH = "main"

from pathlib import Path
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import urlopen

import questionary
from questionary import Choice


TOOL_FILES = {
    "chatgpt-project": ("chatgpt/instruction.md", "repodoc/project-instructions/chatgpt.md"),
    "claude-project": ("claude/instruction.md", "repodoc/project-instructions/claude.md"),
    "claude-code": ("claude-code/CLAUDE.md", ".claude/CLAUDE.md"),
    "codex": ("codex/AGENTS.md", "AGENTS.md"),
    "copilot": ("copilot/copilot-instructions.md", ".github/copilot-instructions.md"),
}
PROTOCOL = ("repodoc/memory-protocol.md", "repodoc/memory-protocol.md")


def ask(prompt: str, default: str) -> str:
    if sys.stdin.isatty() and sys.stdout.isatty():
        value = questionary.text(prompt, default=default).ask()
        if value is None:
            raise KeyboardInterrupt
        return value.strip() or default
    value = input(f"{prompt} [{default}]: ").strip()
    return value or default


def choose_language() -> str:
    if sys.stdin.isatty() and sys.stdout.isatty():
        value = questionary.select(
            "Language / Lingua",
            choices=[
                Choice("English", value="en"),
                Choice("Italiano", value="it"),
            ],
            default="en",
            instruction="(↑/↓ move, Enter confirm)",
        ).ask()
        if value is None:
            raise KeyboardInterrupt
        return value

    while True:
        value = ask("Language / Lingua (en/it)", "en").lower()
        if value in {"en", "it"}:
            return value
        print("Choose 'en' or 'it'. / Scegli 'en' o 'it'.")


def choose_tools() -> list[str]:
    if sys.stdin.isatty() and sys.stdout.isatty():
        selected = questionary.checkbox(
            "Select tools / Seleziona gli strumenti",
            choices=[
                Choice("ChatGPT Project", value="chatgpt-project", checked=True),
                Choice("Claude Project", value="claude-project", checked=True),
                Choice("Claude Code", value="claude-code", checked=True),
                Choice("OpenAI Codex", value="codex", checked=True),
                Choice("GitHub Copilot", value="copilot", checked=True),
            ],
            validate=lambda values: bool(values) or "Select at least one tool / Seleziona almeno uno strumento",
            instruction="(↑/↓ move, Space toggle, Enter confirm)",
        ).ask()
        if selected is None:
            raise KeyboardInterrupt
        return selected

    aliases = {
        "1": "chatgpt-project",
        "2": "claude-project",
        "3": "claude-code",
        "4": "codex",
        "5": "copilot",
        "chatgpt": "chatgpt-project",
        "chatgpt-project": "chatgpt-project",
        "claude-project": "claude-project",
        "claude": "claude-code",
        "claude-code": "claude-code",
        "codex": "codex",
        "copilot": "copilot",
    }
    print("Tools: 1) ChatGPT Project  2) Claude Project  3) Claude Code  4) Codex  5) GitHub Copilot  6) All")
    while True:
        value = ask("Select tools (comma-separated)", "6").lower()
        if value in {"6", "all", "tutti"}:
            return list(TOOL_FILES)
        selected: list[str] = []
        valid = True
        for item in value.replace(" ", "").split(","):
            tool = aliases.get(item)
            if tool is None:
                valid = False
                break
            if tool not in selected:
                selected.append(tool)
        if valid and selected:
            return selected
        print("Choose 1, 2, 3, 4, 5, 6, or a comma-separated list.")


def raw_base_url() -> str:
    parsed = urlparse(SOURCE_REPOSITORY.rstrip("/"))
    parts = parsed.path.strip("/").removesuffix(".git").split("/")
    if parsed.netloc != "github.com" or len(parts) != 2 or "<" in SOURCE_REPOSITORY:
        raise ValueError("Set SOURCE_REPOSITORY to a GitHub URL such as https://github.com/owner/repo")
    return f"https://raw.githubusercontent.com/{parts[0]}/{parts[1]}/{SOURCE_BRANCH}"


def read_template(language: str, relative_path: str) -> str:
    local_path = Path(__file__).resolve().parent / language / relative_path
    if local_path.is_file():
        return local_path.read_text(encoding="utf-8")

    url = f"{raw_base_url()}/{language}/{relative_path}"
    try:
        with urlopen(url, timeout=30) as response:
            return response.read().decode("utf-8")
    except (HTTPError, URLError) as error:
        raise RuntimeError(f"Could not download {url}: {error}") from error


def confirm_overwrite(path: Path, language: str) -> bool:
    message = f"{path} exists. Overwrite?" if language == "en" else f"{path} esiste. Sovrascrivere?"
    if sys.stdin.isatty() and sys.stdout.isatty():
        answer = questionary.confirm(message, default=False).ask()
        if answer is None:
            raise KeyboardInterrupt
        return answer
    return input(f"{message} [y/N]: ").strip().lower() in {"y", "yes", "s", "si", "sì"}


def install_file(source: str, destination: str, language: str, repository: str, target: Path) -> bool:
    destination_path = target / destination
    if destination_path.exists() and not confirm_overwrite(destination_path, language):
        print(f"Skipped: {destination_path}")
        return False

    content = read_template(language, source).replace("<owner>/<repo>", repository)
    destination_path.parent.mkdir(parents=True, exist_ok=True)
    destination_path.write_text(content, encoding="utf-8", newline="\n")
    print(f"Installed: {destination_path}")
    return True


def main() -> int:
    language = choose_language()
    target = Path.cwd().resolve()
    repository = ask(
        "Target repository name (owner/name is preferred)" if language == "en" else "Nome della repository target (preferibilmente owner/nome)",
        target.name,
    )
    tools = choose_tools()

    print(f"\nTarget: {target}")
    print(f"Repository: {repository}")
    print(f"Language: {language}")
    print(f"Tools: {', '.join(tools)}\n")

    installed = 0
    protocol_source, protocol_destination = PROTOCOL
    installed += install_file(protocol_source, protocol_destination, language, repository, target)
    for tool in tools:
        source, destination = TOOL_FILES[tool]
        installed += install_file(source, destination, language, repository, target)

    print(f"\nDone. {installed} file(s) installed.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (EOFError, KeyboardInterrupt):
        print("\nCancelled.")
        raise SystemExit(130)
    except (RuntimeError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        raise SystemExit(1)
