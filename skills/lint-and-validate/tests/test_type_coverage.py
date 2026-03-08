import sys
from pathlib import Path

# Add scripts directory to path to import the module
scripts_dir = Path(__file__).parent.parent / "scripts"
sys.path.append(str(scripts_dir))

from type_coverage import check_typescript_coverage


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
