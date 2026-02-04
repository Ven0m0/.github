---
description: 'PowerShell scripting standards with best practices for cmdlet development, pipeline operations, and error handling'
applyTo: '**/*.ps1, **/*.psm1, **/*.psd1'
---

# PowerShell Scripting Standards

Standards for PowerShell scripting with focus on cmdlet design, object-oriented pipeline operations, and robust error handling.

## Shared Shell Principles

### Safety and Reliability

1. **Fail Fast**: Detect errors immediately and exit
   - Use strict mode and stop on errors
   - No silent failures or ignored errors
   - Explicit validation before operations

2. **Performance**: Minimize overhead and optimize pipeline usage
   - Batch operations together
   - Use built-in cmdlets over external tools
   - Cache computed values

3. **Clarity**: Scripts should be readable and maintainable
   - Descriptive cmdlet and parameter names
   - Comments explaining non-obvious logic
   - Consistent style and formatting

### Tooling Preferences

Modern tools prioritized with legacy fallbacks:

| Task | Preferred | Fallback |
|------|-----------|----------|
| Search files | `rg` (ripgrep) | `Select-String` |
| Find files | `fd` | `Get-ChildItem` |
| Streaming | `jq` | `ConvertFrom-Json` |
| View files | `bat` | `Get-Content` |

---

## PowerShell Standards

**File patterns**: `*.ps1`, `*.psm1` (module), `*.psd1` (manifest)

### Script Metadata

```powershell
<#
.SYNOPSIS
    Brief description of what the script does

.DESCRIPTION
    Detailed description with more context

.PARAMETER Path
    Path to the resource to process

.EXAMPLE
    .\script.ps1 -Path "C:\data"

.NOTES
    Author: John Doe
    Last Modified: 2024-02-01
#>

param(
    [Parameter(Mandatory=$true)]
    [string]$Path,

    [Parameter(Mandatory=$false)]
    [int]$Timeout = 30
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"
```

### Cmdlet Naming and Style

```powershell
# GOOD: Verb-Noun naming (PowerShell approved verbs)
function Get-UserById {
    param(
        [Parameter(Mandatory=$true)]
        [string]$UserId
    )

    # Implementation
}

# Use approved verbs: Get, Set, New, Remove, Test, Start, Stop, Invoke, Confirm, etc.
# Full list: Get-Verb
```

### Error Handling

```powershell
# Try-catch-finally pattern
try {
    $result = Get-Item $Path -ErrorAction Stop
    Write-Host "Found: $result"
}
catch [ItemNotFoundException] {
    Write-Error "Item not found: $Path"
    exit 1
}
catch {
    Write-Error "Unexpected error: $_"
    exit 2
}
finally {
    # Cleanup
}
```

### Pipeline and Objects

```powershell
# GOOD: Working with objects through the pipeline
Get-Process |
    Where-Object {$_.WorkingSet -gt 100MB} |
    ForEach-Object {
        [PSCustomObject]@{
            Name = $_.Name
            Memory = "$([math]::Round($_.WorkingSet/1MB)) MB"
        }
    }

# Avoid string manipulation; use objects
$obj = [PSCustomObject]@{
    Name = "John"
    Age = 30
    Email = "john@example.com"
}
$obj | Export-Csv "users.csv"
```

### Modules and Functions

```powershell
# Export public functions in module manifest
Export-ModuleMember -Function Get-User, New-User

# Use filters for pipeline
filter Where-Large {
    if ($_.Size -gt 10MB) {
        $_
    }
}

Get-ChildItem | Where-Large
```

### Linting and Analysis

```powershell
# PowerShell Script Analyzer
Invoke-ScriptAnalyzer -Path script.ps1
```

### Testing

```powershell
# PowerShell Pester
Invoke-Pester -Path tests/
```

### Forbidden Patterns

- ❌ Hardcoded credentials — use SecureString or credential objects
- ❌ `Invoke-Expression` with untrusted input — code injection risk
- ❌ `ConvertFrom-Json` with `-Depth 1` — insufficient for complex objects
- ❌ Unquoted paths with spaces — always quote
- ❌ Ignoring errors with `$ErrorActionPreference = "SilentlyContinue"`

---

## Exit Codes

```powershell
exit 0      # Success
exit 1      # General error
exit 127    # Command not found
```

---

## Logging and Output

- Use `Write-Host` for user messages
- Use `Write-Error` for error messages
- Use `Write-Verbose` for detailed logging (enabled with `-Verbose`)
- Use `Write-Debug` for debugging output (enabled with `-Debug`)
- Be specific in error messages with context

---

## Security Checklist

- [ ] No hardcoded credentials
- [ ] Input validation before use
- [ ] Error messages don't leak paths or sensitive data
- [ ] No dynamic code execution from untrusted sources
- [ ] Use SecureString for passwords
- [ ] Exit codes checked appropriately
- [ ] Temporary files created securely
