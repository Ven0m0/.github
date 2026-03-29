import json
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]


def read_frontmatter(path: Path) -> str:
    """Return the YAML frontmatter block from an agent file."""
    match = re.match(r"^---\n(.*?)\n---\n", path.read_text(encoding="utf-8"), re.DOTALL)
    assert match is not None, f"missing frontmatter in {path}"
    return match.group(1)


def read_model(path: Path) -> str:
    """Return the configured primary model for an agent."""
    match = re.search(r'^model:\s*["\']?([^\n"\']+)["\']?$', read_frontmatter(path), re.MULTILINE)
    assert match is not None, f"missing model in {path}"
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
        "agents/coder.agent.md": ("github-mcp-server:", "fast-filesystem:", "octocode:", "eslint:", "ast-grep:"),
        "agents/reviewer.agent.md": ("github-mcp-server:", "fast-filesystem:", "octocode:", "eslint:", "ast-grep:"),
        "agents/codebase-maintainer.agent.md": (
            "github-mcp-server:",
            "fast-filesystem:",
            "octocode:",
            "eslint:",
            "ast-grep:",
        ),
        "agents/explorer.agent.md": ("github-mcp-server:", "fast-filesystem:", "octocode:", "ast-grep:"),
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


def test_all_agents_use_supported_primary_models():
    """Agents should use the repo-standard primary models only."""
    supported_models = {"GPT-5.4", "claude-sonnet-4.6"}
    expected_models = {
        "agents/orchestrator.agent.md": "claude-sonnet-4.6",
        "agents/explorer.agent.md": "GPT-5.4",
        "agents/planner.agent.md": "GPT-5.4",
        "agents/researcher.agent.md": "GPT-5.4",
        "agents/coder.agent.md": "claude-sonnet-4.6",
        "agents/reviewer.agent.md": "GPT-5.4",
        "agents/debug.agent.md": "claude-sonnet-4.6",
        "agents/workflow-engineer.agent.md": "claude-sonnet-4.6",
        "agents/frontend-specialist.agent.md": "claude-sonnet-4.6",
        "agents/git.agent.md": "claude-sonnet-4.6",
        "agents/codebase-maintainer.agent.md": "claude-sonnet-4.6",
        "agents/doc-writer.agent.md": "GPT-5.4",
        "agents/repo-architect.agent.md": "GPT-5.4",
        "agents/arch-linux-expert.agent.md": "claude-sonnet-4.6",
        "agents/janitor.agent.md": "claude-sonnet-4.6",
    }

    for path in (REPO_ROOT / "agents").glob("*.agent.md"):
        model = read_model(path)
        assert model in supported_models, f"unsupported model {model!r} in {path}"

    for relative_path, expected_model in expected_models.items():
        path = REPO_ROOT / relative_path
        model = read_model(path)
        assert model == expected_model


def test_primary_agents_drop_deprecated_mcp_servers():
    """Optimized agents should use the shared MCP stack instead of deprecated server choices."""
    deprecated_servers = ("context7:", "serena:", "gitmcp:", "grep-app:", "fetch:", "memory:", "morph-mcp:")

    for path in (REPO_ROOT / "agents").glob("*.agent.md"):
        frontmatter = read_frontmatter(path)
        for server_name in deprecated_servers:
            assert server_name not in frontmatter, f"unexpected {server_name} in {path}"
