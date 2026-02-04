---
description: 'CMD/Batch scripting standards with best practices for Windows batch file development'
applyTo: '**/*.bat, **/*.cmd'
---

# CMD/Batch Scripting Standards

Standards for CMD/Batch scripting with focus on Windows automation, error handling, and maintainability.

## Shared Shell Principles

### Safety and Reliability

1. **Fail Fast**: Detect errors immediately and exit
   - Check errorlevel after commands
   - No silent failures or ignored errors
   - Explicit validation before operations

2. **Performance**: Minimize overhead
   - Batch operations together
   - Use built-in commands
   - Cache computed values

3. **Clarity**: Scripts should be readable and maintainable
   - Descriptive variable names
   - Comments explaining non-obvious logic
   - Consistent style and formatting

---

## CMD/Batch Standards

**File patterns**: `*.bat`, `*.cmd`

### Script Header

```batch
@echo off
setlocal enabledelayedexpansion
setlocal enableextensions
```

**Breakdown**:
- `@echo off`: Don't echo command being executed
- `setlocal enabledelayedexpansion`: Use `!var!` for delayed expansion
- `setlocal enableextensions`: Enable command extensions (safer, more features)

### Variables and Expansion

```batch
:: Immediate expansion (normal)
set "name=John"
echo %name%

:: Delayed expansion (in code blocks)
setlocal enabledelayedexpansion
if exist "file.txt" (
    set "count=1"
    echo Count: !count!     :: Use !var! not %var% in code blocks
)
```

### Control Flow

```batch
:: If statements
if exist "file.txt" (
    echo File exists
) else (
    echo File not found
)

:: If with conditions
if "%errorlevel%"=="0" (
    echo Success
) else (
    echo Failed with code %errorlevel%
)

:: For loops
for %%i in (1 2 3) do (
    echo Item: %%i
)

:: For directories
for /d %%i in (C:\*) do (
    echo Directory: %%i
)
```

### Functions/Subroutines

```batch
:: Call a subroutine with parameters
call :process_file "input.txt"

:: Function definition
:process_file
set "filename=%~1"
set "fullpath=%~f1"     :: Full path
set "drive=%~d1"        :: Drive letter
set "path=%~p1"         :: Directory path
set "filename=%~n1"     :: Filename without extension
set "extension=%~x1"    :: File extension

echo Processing: %fullpath%
exit /b 0               :: Return from function

:error_handler
echo Error: %errorlevel%
exit /b 1
```

### Error Handling

```batch
:: Check previous command's exit code
if errorlevel 1 (
    echo Error occurred
    goto :error_handler
)

:: Or use conditional execution
command && echo Success || echo Failure
```

### Forbidden Patterns

- ❌ Unquoted paths with spaces: always use `"%path%"`
- ❌ Using `%var%` inside code blocks with delayed expansion needed
- ❌ No error checking — always verify errorlevel
- ❌ Modifying environment variables without `setlocal`

---

## Exit Codes

```batch
exit /b 0      :: Success (from subroutine)
exit /b 1      :: General error
exit 0         :: Success (from script)
exit 1         :: General error
```

---

## Logging and Output

- Use `echo` for user messages
- Redirect errors to stderr: `echo Error >&2`
- Be specific in error messages with context

---

## Security Checklist

- [ ] No hardcoded credentials
- [ ] Input validation before use
- [ ] Error messages don't leak paths or sensitive data
- [ ] Proper quoting for variables with spaces
- [ ] Exit codes checked appropriately
- [ ] Temporary files created securely
- [ ] Use `setlocal` to avoid polluting environment
