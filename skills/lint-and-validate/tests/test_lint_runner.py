import json
from pathlib import Path
from scripts.lint_runner import (
    detect_node_project,
    detect_python_project,
    detect_project_type,
)


def test_detect_node_project_with_lint_script(tmp_path: Path):
    result = {"type": "unknown", "linters": []}
    package_json = tmp_path / "package.json"
    package_json.write_text(
        json.dumps(
            {"scripts": {"lint": "eslint ."}, "dependencies": {"typescript": "^4.0.0"}}
        )
    )

    detect_node_project(tmp_path, result)

    assert result["type"] == "node"
    assert len(result["linters"]) == 2
    assert result["linters"][0]["name"] == "npm lint"
    assert result["linters"][1]["name"] == "tsc"


def test_detect_node_project_with_eslint_dep(tmp_path: Path):
    result = {"type": "unknown", "linters": []}
    package_json = tmp_path / "package.json"
    package_json.write_text(json.dumps({"devDependencies": {"eslint": "^8.0.0"}}))

    detect_node_project(tmp_path, result)

    assert result["type"] == "node"
    assert len(result["linters"]) == 1
    assert result["linters"][0]["name"] == "eslint"


def test_detect_node_project_with_tsconfig(tmp_path: Path):
    result = {"type": "unknown", "linters": []}
    package_json = tmp_path / "package.json"
    package_json.write_text(json.dumps({}))
    (tmp_path / "tsconfig.json").touch()

    detect_node_project(tmp_path, result)

    assert result["type"] == "node"
    assert len(result["linters"]) == 1
    assert result["linters"][0]["name"] == "tsc"


def test_detect_python_project_pyproject(tmp_path: Path):
    result = {"type": "unknown", "linters": []}
    (tmp_path / "pyproject.toml").touch()

    detect_python_project(tmp_path, result)

    assert result["type"] == "python"
    assert len(result["linters"]) == 2
    assert result["linters"][0]["name"] == "ruff"
    assert result["linters"][1]["name"] == "mypy"


def test_detect_python_project_requirements(tmp_path: Path):
    result = {"type": "unknown", "linters": []}
    (tmp_path / "requirements.txt").touch()

    detect_python_project(tmp_path, result)

    assert result["type"] == "python"
    assert len(result["linters"]) == 1
    assert result["linters"][0]["name"] == "ruff"


def test_detect_project_type_node(tmp_path: Path):
    package_json = tmp_path / "package.json"
    package_json.write_text(
        json.dumps(
            {"scripts": {"lint": "eslint ."}, "dependencies": {"typescript": "^4.0.0"}}
        )
    )

    result = detect_project_type(tmp_path)

    assert result["type"] == "node"
    assert len(result["linters"]) == 2


def test_detect_project_type_python(tmp_path: Path):
    (tmp_path / "pyproject.toml").touch()

    result = detect_project_type(tmp_path)

    assert result["type"] == "python"
    assert len(result["linters"]) == 2


def test_detect_project_type_unknown(tmp_path: Path):
    result = detect_project_type(tmp_path)

    assert result["type"] == "unknown"
    assert len(result["linters"]) == 0
