import json
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]

RE_FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
RE_MODEL = re.compile(r'^model:\s*["\']?([^\n"\']+)["\']?$', re.MULTILINE)


def read_frontmatter(path: Path) -> str:
    """Return the YAML frontmatter block from an agent file."""
    match = RE_FRONTMATTER.match(path.read_text(encoding="utf-8"))
    assert match is not None, f"missing frontmatter in {path}"
    return match.group(1)


def read_model(path: Path) -> str:
    """Return the configured primary model for an agent."""
    match = RE_MODEL.search(read_frontmatter(path))
    assert match is not None, f"missing model in {path}"
    return match.group(1)


def test_workspace_mcp_config_includes_selected_servers():
    """Workspace MCP config should expose the newly selected high-value servers."""
    mcp_config = json.loads((REPO_ROOT / ".vscode" / "mcp.json").read_text(encoding="utf-8"))
    servers = mcp_config["mcpServers"]

    assert servers["github-mcp-server"]["url"] == "https://api.githubcopilot.com/mcp/insiders"
    assert servers["playwright"]["args"] == ["-y", "@playwright/mcp@latest", "--headless"]
    assert servers["vercel"]["url"] == "https://mcp.vercel.com"
    assert servers["exa"]["url"] == "https://mcp.exa.ai/mcp?tools=web_search_exa,web_search_advanced_exa,crawling_exa"
    assert servers["ref-tools"]["url"] == "https://api.ref.tools/mcp"
    assert servers["fast-filesystem"]["args"] == ["-y", "fast-filesystem-mcp@latest"]
    assert servers["octocode"]["args"] == ["-y", "octocode-mcp@latest"]


def test_code_agents_keep_only_specialized_structural_mcp_servers():
    """Coding-focused agents should keep only the specialized MCP servers they still need."""
    expected_servers = {
        "agents/coder.agent.md": ("eslint:", "ast-grep:", "repomix:", "semgrep:", "yggdrasil:"),
        "agents/reviewer.agent.md": ("eslint:", "ast-grep:", "repomix:", "semgrep:", "yggdrasil:"),
        "agents/codebase-maintainer.agent.md": ("eslint:", "ast-grep:", "repomix:", "yggdrasil:"),
        "agents/explorer.agent.md": ("ast-grep:", "repomix:"),
    }

    for relative_path, server_names in expected_servers.items():
        frontmatter = read_frontmatter(REPO_ROOT / relative_path)
        for server_name in server_names:
            assert server_name in frontmatter


def test_agents_include_specialized_mcp_servers_in_frontmatter():
    """Agents should expose the specialized MCP servers they need in frontmatter."""
    expected_servers = {
        "agents/researcher.agent.md": ("reddit:", "yggdrasil:", "mslearn:"),
        "agents/frontend-specialist.agent.md": ("chrome-devtools:", "vercel:"),
        "agents/debug.agent.md": ("chrome-devtools:", "semgrep:", "yggdrasil:"),
        "agents/workflow-engineer.agent.md": ("vercel:", "netlify:", "yggdrasil:", "mslearn:"),
        "agents/repo-architect.agent.md": ("vercel:", "netlify:", "yggdrasil:", "mslearn:"),
        "agents/orchestrator.agent.md": ("repomix:", "yggdrasil:"),
        "agents/planner.agent.md": ("repomix:", "yggdrasil:"),
        "agents/git.agent.md": ("yggdrasil:",),
        "agents/arch-linux-expert.agent.md": ("yggdrasil:",),
        "agents/janitor.agent.md": ("ast-grep:", "eslint:", "repomix:", "yggdrasil:"),
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


def test_all_agent_frontmatter_is_valid_yaml():
    """All agent frontmatter blocks must parse as valid YAML."""
    try:
        import yaml
    except ImportError:
        import pytest
        pytest.skip("PyYAML is not installed")

    for path in (REPO_ROOT / "agents").glob("*.agent.md"):
        frontmatter = read_frontmatter(path)
        try:
            yaml.safe_load(frontmatter)
        except yaml.YAMLError as exc:
            raise AssertionError(f"invalid YAML frontmatter in {path}: {exc}") from exc


def test_agents_replace_sequential_thinking_with_yggdrasil():
    """Agents should no longer reference the deprecated sequential-thinking server."""
    for path in (REPO_ROOT / "agents").glob("*.agent.md"):
        frontmatter = read_frontmatter(path)
        assert "sequential-thinking:" not in frontmatter, f"unexpected sequential-thinking in {path}"


def test_primary_agents_drop_deprecated_mcp_servers():
    """Optimized agents should avoid deprecated or now-default MCP server choices."""
    deprecated_servers = (
        "context7:",
        "serena:",
        "gitmcp:",
        "grep-app:",
        "fetch:",
        "memory:",
        "morph-mcp:",
        "github-mcp-server:",
        "fast-filesystem:",
        "octocode:",
        "exa:",
        "ref-tools:",
        "next-devtools:",
        "playwright:",
    )

    for path in (REPO_ROOT / "agents").glob("*.agent.md"):
        frontmatter = read_frontmatter(path)
        for server_name in deprecated_servers:
            assert server_name not in frontmatter, f"unexpected {server_name} in {path}"
