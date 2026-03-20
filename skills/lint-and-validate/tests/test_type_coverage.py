import sys
from pathlib import Path

# Add scripts directory to path to import the module
scripts_dir = Path(__file__).parent.parent / "scripts"
sys.path.append(str(scripts_dir))

from type_coverage import check_typescript_coverage, check_python_coverage


def test_check_typescript_coverage_no_files(tmp_path):
    """Test when no TypeScript files are present."""
    result = check_typescript_coverage(tmp_path)
    assert result["files"] == 0
    assert "[!] No TypeScript files found" in result["issues"]
    assert result["stats"]["any_count"] == 0


def test_check_typescript_coverage_any_detection(tmp_path):
    """Test detection of ': any' with various formats."""
    ts_file = tmp_path / "test.ts"
    ts_file.write_text(
        """
        let a: any;
        const b:any = 1;
        function foo(x:  any): any { return x; }
        let c:any;
        // False positives to avoid (no colon)
        let company = "any";
        let many = true;

        // Note: Current regex-based detection is simple and might match
        // these if they have a colon, even in comments/strings.
        // This test documents the current behavior.
    """,
        encoding="utf-8",
    )

    result = check_typescript_coverage(tmp_path)

    # Expected matches for ': any':
    # 1. let a: any; -> ': any'
    # 2. const b:any = 1; -> ':any'
    # 3. function foo(x:  any) -> ':  any'
    # 4. ): any { -> ': any'
    # 5. let c:any; -> ':any'

    assert result["stats"]["any_count"] == 5
    assert result["files"] == 1


def test_check_typescript_coverage_function_stats(tmp_path):
    """Test detection of typed and untyped functions."""
    ts_file = tmp_path / "test.ts"
    ts_file.write_text(
        """
        function typedFunc(a: number): number { return a; }
        function untypedFunc(a: number) { return a; }
        const untypedArrow = (x) => x;
    """,
        encoding="utf-8",
    )

    result = check_typescript_coverage(tmp_path)

    # typedFunc -> matches typed (1)
    # untypedFunc -> matches untyped (1)
    # untypedArrow -> matches untyped (2)

    assert result["stats"]["untyped_functions"] == 2
    assert result["stats"]["total_functions"] == 3


def test_check_typescript_coverage_multiple_files(tmp_path):
    """Test handling of multiple files."""
    (tmp_path / "file1.ts").write_text("let a: any;")
    (tmp_path / "file2.tsx").write_text("let b: any;")
    (tmp_path / "not_ts.js").write_text("let c: any;")

    result = check_typescript_coverage(tmp_path)
    assert result["files"] == 2
    assert result["stats"]["any_count"] == 2


def test_check_python_coverage_no_files(tmp_path):
    """Test when no Python files are present."""
    result = check_python_coverage(tmp_path)
    assert result["files"] == 0
    assert "[!] No Python files found" in result["issues"]
    assert result["stats"]["any_count"] == 0


def test_check_python_coverage_any_detection(tmp_path):
    """Test detection of 'Any' with various formats."""
    py_file = tmp_path / "test.py"
    py_file.write_text(
        """
        from typing import Any
        def foo(x: Any) -> Any:
            return x
        a: Any = 1
        # False positives
        def anybody(): pass
        any_var = True
    """,
        encoding="utf-8",
    )

    result = check_python_coverage(tmp_path)

    # Expected matches for Any usage:
    # 1. Parameter annotation: x: Any
    # 2. Return annotation: -> Any
    # 3. Variable annotation: a: Any

    assert result["stats"]["any_count"] == 3
    assert result["files"] == 1


def test_check_python_coverage_function_stats(tmp_path):
    """Test detection of typed and untyped functions."""
    py_file = tmp_path / "test.py"
    py_file.write_text(
        """
        def untyped_func(x):
            pass

        def params_typed(x: int):
            pass

        def return_typed(x) -> int:
            return 1

        def fully_typed(x: int) -> int:
            return x
    """,
        encoding="utf-8",
    )

    result = check_python_coverage(tmp_path)

    # untyped_func: matches ALL (1), matches PARAMS (0), matches RETURN (0)
    # params_typed: matches ALL (2), matches PARAMS (1), matches RETURN (0)
    # return_typed: matches ALL (3), matches PARAMS (0), matches RETURN (1)
    # fully_typed: matches ALL (4), matches PARAMS (2), matches RETURN (2)

    # Current implementation:
    # typed_funcs = RE_PY_TYPED_FUNC_PARAMS.findall(content) -> 2 matches
    # typed_funcs += RE_PY_TYPED_FUNC_RETURN.findall(content) -> 2 matches
    # stats["typed_functions"] = 4
    # stats["untyped_functions"] = 4 - 4 = 0

    # This is obviously wrong. fully_typed is double-counted as typed.
    # And untyped_func is NOT counted as untyped because total_typed (4) == total_all (4).

    assert result["stats"]["typed_functions"] == 3
    assert result["stats"]["untyped_functions"] == 1


def test_check_python_coverage_multiple_files(tmp_path):
    """Test handling of multiple files."""
    (tmp_path / "file1.py").write_text("def foo(x: int): pass")
    (tmp_path / "file2.py").write_text("def bar(x: int): pass")
    (tmp_path / "not_py.txt").write_text("def baz(x: int): pass")

    result = check_python_coverage(tmp_path)
    assert result["files"] == 2
    assert result["stats"]["typed_functions"] == 2
