---
description: 'Instructions for building MCP servers using the Python SDK'
applyTo: '**/*.{py,pyi},**/pyproject.toml'
---

# Python MCP Server Development

<Goals>

- Use `uv` for project management, `mcp[cli]` SDK
- Type hints mandatory (drive schema generation and validation)
- FastMCP for rapid development, low-level Server for max control

</Goals>

<Standards>

**Setup**: `uv init mcp-server-demo && uv add "mcp[cli]"`
**Registration**: `@mcp.tool()`, `@mcp.resource()`, `@mcp.prompt()` decorators
**Types**: Pydantic models, TypedDicts, or dataclasses for structured output
**Transport**: `mcp.run()` (stdio default), `mcp.run(transport="streamable-http")` for HTTP
**Context**: `ctx: Context` parameter for logging, progress, user input, LLM sampling
**Testing**: `uv run mcp dev server.py` (Inspector) | `uv run mcp install server.py` (Claude Desktop)

</Standards>

## Core Patterns

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My Server")

@mcp.tool()
def calculate(a: int, b: int, op: str) -> int:
    """Perform calculation."""
    return a + b if op == "add" else a - b

if __name__ == "__main__":
    mcp.run()
```

### Structured Output
```python
from pydantic import BaseModel, Field

class WeatherData(BaseModel):
    temperature: float = Field(description="Temperature in Celsius")
    condition: str

@mcp.tool()
def get_weather(city: str) -> WeatherData:
    """Get weather for a city."""
    return WeatherData(temperature=22.5, condition="sunny")
```

### Context and Logging
```python
from mcp.server.fastmcp import Context

@mcp.tool()
async def process_data(data: str, ctx: Context) -> str:
    """Process data with logging."""
    await ctx.info(f"Processing: {data}")
    await ctx.report_progress(0.5, 1.0, "Halfway")
    return f"Processed: {data}"
```

### Lifespan Management
```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def app_lifespan(server: FastMCP):
    db = await Database.connect()
    try:
        yield AppContext(db=db)
    finally:
        await db.disconnect()

mcp = FastMCP("My App", lifespan=app_lifespan)
```

<WhatToAdd>

- Clear docstrings (become tool descriptions)
- Descriptive parameter names with type hints
- Pydantic Field descriptions for input validation
- Async functions for I/O-bound operations
- Error handling with try-except
- Environment variables for configuration

</WhatToAdd>

<Limitations>

- No hardcoded credentials
- No blocking operations in async handlers
- Log to stderr to avoid interfering with stdio transport
- Clean up resources in lifespan context managers
- Test tools independently before LLM integration

</Limitations>
