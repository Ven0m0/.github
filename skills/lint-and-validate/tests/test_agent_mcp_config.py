import json
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]


def read_frontmatter(path: Path) -> str:
    """Return the YAML frontmatter block from an agent file."""
    match = re.match(r"^---\n(.*?)\n---\n", path.read_text(encoding="utf-8"), re.DOTALL)
    assert match is not None, f"missing frontmatter in {path}"
    return match.group(1)


def test_workspace_mcp_config_includes_selected_servers():
    """Workspace MCP config should expose the newly selected high-value servers."""
    mcp_config = json.loads((REPO_ROOT / ".vscode" / "mcp.json").read_text(encoding="utf-8"))
    servers = mcp_config["mcpServers"]

    assert servers["eslint"]["args"] == ["-y", "@eslint/mcp@latest"]
    assert servers["chrome-devtools"]["args"] == ["-y", "chrome-devtools-mcp@latest", "--headless", "--no-usage-statistics"]
    assert servers["next-devtools"]["args"] == ["-y", "next-devtools-mcp@latest"]
    assert servers["vercel"]["url"] == "https://mcp.vercel.com"
    assert servers["ast-grep"]["args"] == ["-y", "@notprolands/ast-grep-mcp@latest"]


def test_code_agents_get_structural_and_linting_mcp_servers():
    """Coding-focused agents should expose ESLint and/or ast-grep where they add value."""
    expected_servers = {
        "agents/coder.agent.md": ("eslint:", "ast-grep:"),
        "agents/reviewer.agent.md": ("eslint:", "ast-grep:"),
        "agents/codebase-maintainer.agent.md": ("eslint:", "ast-grep:"),
        "agents/explorer.agent.md": ("ast-grep:",),
    }

    for relative_path, server_names in expected_servers.items():
        frontmatter = read_frontmatter(REPO_ROOT / relative_path)
        for server_name in server_names:
            assert server_name in frontmatter


def test_frontend_and_platform_agents_get_browser_and_vercel_servers():
    """Frontend/platform agents should expose the browser and hosting MCP servers they need."""
    expected_servers = {
        "agents/frontend-specialist.agent.md": ("chrome-devtools:", "next-devtools:", "vercel:"),
        "agents/debug.agent.md": ("chrome-devtools:", "next-devtools:"),
        "agents/workflow-engineer.agent.md": ("vercel:",),
        "agents/repo-architect.agent.md": ("vercel:",),
    }

    for relative_path, server_names in expected_servers.items():
        frontmatter = read_frontmatter(REPO_ROOT / relative_path)
        for server_name in server_names:
            assert server_name in frontmatter
