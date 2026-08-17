# /// script
# requires-python = ">=3.11"
# dependencies = ["questionary>=2.1,<3"]
# ///

SOURCE_REPOSITORY = "https://github.com/sely2k/ai-project-memory"
SOURCE_BRANCH = "main"
DEFAULT_GITHUB_OWNER = "sely2k"

from pathlib import Path
import re
import subprocess
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
MANAGED_TOOLS = {"claude-code", "codex", "copilot"}
MANAGED_BLOCK_START = "<!-- repodoc:start -->"
MANAGED_BLOCK_END = "<!-- repodoc:end -->"


def ask(prompt: str, default: str) -> str:
    if sys.stdin.isatty() and sys.stdout.isatty():
        value = questionary.text(prompt, default=default).ask()
        if value is None:
            raise KeyboardInterrupt
        return value.strip() or default
    value = input(f"{prompt} [{default}]: ").strip()
    return value or default


def normalize_github_repository(value: str, default_owner: str = DEFAULT_GITHUB_OWNER) -> str | None:
    value = value.strip().rstrip("/").removesuffix(".git")
    patterns = (
        r"(?:https?://github\.com/|ssh://git@github\.com/|git@github\.com:)([^/]+/[^/]+)$",
        r"([^/\s]+/[^/\s]+)$",
    )
    for pattern in patterns:
        match = re.fullmatch(pattern, value)
        if match:
            return match.group(1)
    if re.fullmatch(r"[^/\s]+", value):
        return f"{default_owner}/{value}"
    return None


def detect_github_repository(target: Path) -> str:
    result = subprocess.run(
        ["git", "-C", str(target), "remote", "get-url", "origin"],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode == 0:
        repository = normalize_github_repository(result.stdout)
        if repository:
            return repository
    return f"{DEFAULT_GITHUB_OWNER}/{target.name}"


def ask_repository(target: Path, language: str) -> str:
    default = detect_github_repository(target)
    prompt = (
        f"GitHub repository (name or owner/name; default owner: {DEFAULT_GITHUB_OWNER})"
        if language == "en"
        else f"Repository GitHub (nome o proprietario/nome; proprietario predefinito: {DEFAULT_GITHUB_OWNER})"
    )
    error = (
        "Enter a repository name, owner/repository, or a complete GitHub URL."
        if language == "en"
        else "Inserisci il nome della repository, proprietario/repository oppure un URL GitHub completo."
    )
    while True:
        repository = normalize_github_repository(ask(prompt, default))
        if repository:
            return repository
        print(error)


def choose_language() -> str:
    if sys.stdin.isatty() and sys.stdout.isatty():
        value = questionary.select(
            "Language / Lingua",
            choices=[
                Choice("English", value="en"),
                Choice("Italiano", value="it"),
            ],
            default="en",
            instruction="(↑/↓ to choose • Enter to confirm)",
        ).ask()
        if value is None:
            raise KeyboardInterrupt
        return value

    while True:
        value = ask("Language / Lingua (en/it)", "en").lower()
        if value in {"en", "it"}:
            return value
        print("Choose 'en' or 'it'. / Scegli 'en' o 'it'.")


def choose_tools(language: str) -> list[str]:
    labels = {
        "en": {
            "prompt": "Which tools do you want to configure?",
            "instruction": "(↑/↓ move • Space select/deselect • Enter confirm)",
            "chatgpt-project": "ChatGPT Project  → instructions to paste into a Project",
            "claude-project": "Claude Project   → instructions to paste into a Project",
            "claude-code": "Claude Code      → .claude/CLAUDE.md",
            "codex": "OpenAI Codex     → AGENTS.md",
            "copilot": "GitHub Copilot   → .github/copilot-instructions.md",
        },
        "it": {
            "prompt": "Quali strumenti vuoi configurare?",
            "instruction": "(↑/↓ sposta • Spazio seleziona/deseleziona • Invio conferma)",
            "chatgpt-project": "ChatGPT Project  → istruzioni da incollare nel Project",
            "claude-project": "Claude Project   → istruzioni da incollare nel Project",
            "claude-code": "Claude Code      → .claude/CLAUDE.md",
            "codex": "OpenAI Codex     → AGENTS.md",
            "copilot": "GitHub Copilot   → .github/copilot-instructions.md",
        },
    }[language]
    if sys.stdin.isatty() and sys.stdout.isatty():
        selected = questionary.checkbox(
            labels["prompt"],
            choices=[
                Choice(labels[tool], value=tool, checked=True) for tool in TOOL_FILES
            ],
            validate=lambda values: bool(values) or "Select at least one tool / Seleziona almeno uno strumento",
            instruction=labels["instruction"],
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


def source_coordinates() -> tuple[str, str]:
    parsed = urlparse(SOURCE_REPOSITORY.rstrip("/"))
    parts = parsed.path.strip("/").removesuffix(".git").split("/")
    if parsed.netloc != "github.com" or len(parts) != 2 or "<" in SOURCE_REPOSITORY:
        raise ValueError("Set SOURCE_REPOSITORY to a GitHub URL such as https://github.com/owner/repo")
    return parts[0], parts[1]


def template_base_urls() -> tuple[str, ...]:
    owner, repository = source_coordinates()
    return (
        f"https://cdn.jsdelivr.net/gh/{owner}/{repository}@{SOURCE_BRANCH}",
        f"https://raw.githubusercontent.com/{owner}/{repository}/{SOURCE_BRANCH}",
    )


def read_template(language: str, relative_path: str) -> str:
    local_path = Path(__file__).resolve().parent / language / relative_path
    if local_path.is_file():
        return local_path.read_text(encoding="utf-8")

    errors = []
    for base_url in template_base_urls():
        url = f"{base_url}/{language}/{relative_path}"
        try:
            with urlopen(url, timeout=30) as response:
                return response.read().decode("utf-8")
        except (HTTPError, URLError) as error:
            errors.append(f"{url}: {error}")
    raise RuntimeError("Could not download template from any source:\n- " + "\n- ".join(errors))


def confirm_overwrite(path: Path, language: str) -> str:
    message = f"{path} exists. What do you want to do?" if language == "en" else f"{path} esiste. Cosa vuoi fare?"
    choices = (
        [Choice("No — skip this file", value="no"), Choice("Yes — overwrite this file", value="yes"), Choice("All — overwrite this and every following file", value="all")]
        if language == "en"
        else [Choice("No — salta questo file", value="no"), Choice("Sì — sovrascrivi questo file", value="yes"), Choice("Tutti — sovrascrivi questo e tutti i successivi", value="all")]
    )
    if sys.stdin.isatty() and sys.stdout.isatty():
        answer = questionary.select(message, choices=choices, default="no").ask()
        if answer is None:
            raise KeyboardInterrupt
        return answer
    answer = input(f"{message} [y/N/a]: ").strip().lower()
    if answer in {"a", "all", "t", "tutti"}:
        return "all"
    return "yes" if answer in {"y", "yes", "s", "si", "sì"} else "no"


def render_template(content: str, repository: str, language: str) -> str:
    content = content.replace("<owner>/<repo>", repository)
    placeholder_notes = {
        "en": "> Replace the placeholder with the target repository before pasting these instructions into the Project.\n\n",
        "it": "> Sostituire il placeholder con il repository del progetto target prima di incollare queste istruzioni nel Project.\n\n",
    }
    content = content.replace(placeholder_notes[language], "")
    return content.replace("`GITHUB_REPOSITORY`", f"`{repository}`")


def install_file(source: str, destination: str, language: str, repository: str, target: Path, overwrite_all: bool) -> tuple[bool, bool]:
    destination_path = target / destination
    if destination_path.exists() and not overwrite_all:
        overwrite = confirm_overwrite(destination_path, language)
        if overwrite == "no":
            print(f"Skipped: {destination_path}")
            return False, overwrite_all
        overwrite_all = overwrite == "all"

    content = render_template(read_template(language, source), repository, language)
    destination_path.parent.mkdir(parents=True, exist_ok=True)
    destination_path.write_text(content, encoding="utf-8", newline="\n")
    print(f"Installed: {destination_path}")
    return True, overwrite_all


def managed_block(content: str) -> str:
    return f"{MANAGED_BLOCK_START}\n{content.strip()}\n{MANAGED_BLOCK_END}\n"


def merge_managed_content(existing: str, content: str) -> tuple[str, str]:
    block = managed_block(content)
    start_count = existing.count(MANAGED_BLOCK_START)
    end_count = existing.count(MANAGED_BLOCK_END)
    if start_count != end_count or start_count > 1:
        raise RuntimeError("RepoDoc managed block markers are missing or duplicated")

    if start_count == 1:
        pattern = re.compile(
            rf"{re.escape(MANAGED_BLOCK_START)}.*?{re.escape(MANAGED_BLOCK_END)}(?:\r?\n)?",
            re.DOTALL,
        )
        return pattern.sub(block, existing, count=1), "Updated"

    separator = "" if not existing or existing.endswith(("\n\n", "\r\n\r\n")) else "\n"
    return f"{existing}{separator}{block}", "Added RepoDoc instructions to"


def install_managed_file(source: str, destination: str, language: str, repository: str, target: Path) -> bool:
    destination_path = target / destination
    content = render_template(read_template(language, source), repository, language)
    destination_path.parent.mkdir(parents=True, exist_ok=True)

    if destination_path.exists():
        existing = destination_path.read_text(encoding="utf-8")
        # Upgrade files created by older installer versions without duplicating them.
        if existing.strip() == content.strip():
            merged, action = managed_block(content), "Updated"
        else:
            try:
                merged, action = merge_managed_content(existing, content)
            except RuntimeError as error:
                raise RuntimeError(f"Cannot safely update {destination_path}: {error}") from error
    else:
        merged, action = managed_block(content), "Installed"

    destination_path.write_text(merged, encoding="utf-8", newline="\n")
    print(f"{action}: {destination_path}")
    return True


def main() -> int:
    language = choose_language()
    target = Path.cwd().resolve()
    repository = ask_repository(target, language)
    tools = choose_tools(language)

    print(f"\nTarget: {target}")
    print(f"Repository: {repository}")
    print(f"Language: {language}")
    print(f"Tools: {', '.join(tools)}\n")

    installed = 0
    overwrite_all = False
    protocol_source, protocol_destination = PROTOCOL
    was_installed, overwrite_all = install_file(protocol_source, protocol_destination, language, repository, target, overwrite_all)
    installed += was_installed
    for tool in tools:
        source, destination = TOOL_FILES[tool]
        if tool in MANAGED_TOOLS:
            was_installed = install_managed_file(source, destination, language, repository, target)
        else:
            was_installed, overwrite_all = install_file(source, destination, language, repository, target, overwrite_all)
        installed += was_installed

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
