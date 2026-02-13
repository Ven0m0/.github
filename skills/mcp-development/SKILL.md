---
name: mcp-development
description: Common patterns and best practices for Model Context Protocol (MCP) server development. Use when creating MCP tools/resources/prompts, choosing stdio vs HTTP transport, or debugging MCP server behavior.
version: 1.0.0
allowed-tools: [Read, Glob, Grep]
---

# MCP Development Skill

Common patterns, principles, and best practices for building Model Context Protocol (MCP) servers across Python and TypeScript.

## Core MCP Concepts

### Tools
Functions the LLM can call with validated inputs:
- Define input schema for validation
- Return structured output
- Include clear descriptions for LLM

### Resources
Data sources the LLM can read:
- **Static**: Fixed URI, pre-defined content
- **Dynamic**: URI templates with parameters
- Include metadata (MIME type, description)

### Prompts
Reusable prompt templates with arguments:
- Parameterized prompts for common tasks
- Clear descriptions of parameters
- Return formatted prompt text

### Context
Shared state and operations:
- Logging (stderr, not stdout)
- Progress reporting
- Sampling (ask LLM for content)
- Elicitation (ask user for input)

### Transports
Communication channels:
- **stdio**: Standard input/output, local integration
- **HTTP**: Web-based, scaling, stateless servers

## Universal Principles

### Type Safety First
- Schema-first development
- Runtime validation at boundaries
- Type hints/annotations drive schema generation
- Clear error messages for validation failures

### LLM-Friendly Descriptions
- Clear, concise tool descriptions
- Explain what the tool does and when to use it
- Document all parameters
- Provide examples in descriptions

### Structured Output
- Return both human-readable and machine-readable formats
- Use consistent data structures
- Include metadata when helpful

### Error Handling
- Catch and handle errors gracefully
- Return error objects with clear messages
- Don't crash the server on tool errors
- Log errors for debugging

### Async for I/O
- All I/O operations should be async
- Don't block event loop
- Use connection pooling for databases
- Handle timeouts appropriately

### Logging Best Practices
- Log to stderr (stdout interferes with stdio transport)
- Include context (tool name, parameters)
- Different log levels (debug, info, error)
- Structured logging for production

## Transport Decision Matrix

| Use Case | Transport | Reason |
|----------|-----------|--------|
| Claude Desktop integration | stdio | Native support, simple setup |
| Web application | HTTP | Browser-compatible, REST-like |
| High-scale deployment | HTTP (stateless) | Load balancing, horizontal scaling |
| Local CLI tool | stdio | Pipes, process communication |
| Multi-user service | HTTP | Session management, CORS |
| Development/testing | stdio | Easier debugging, inspector tools |

### stdio Transport

**Characteristics**:
- Single process, single user
- Stateful connection
- Simple deployment
- Native Claude Desktop support

**Best for**:
- Local development tools
- Personal automation
- CLI integration
- Quick prototypes

**Considerations**:
- Don't log to stdout (use stderr)
- Process lifecycle = session lifecycle
- No CORS or HTTP concerns

### HTTP Transport

**Characteristics**:
- Multi-process, multi-user
- Can be stateless or stateful
- Web integration
- Requires CORS configuration

**Best for**:
- Production deployments
- Scaling horizontally
- Browser-based clients
- Multi-user services

**Considerations**:
- Session management required
- DNS rebinding protection for local servers
- CORS headers for browser clients
- Transport cleanup on connection close

## Common Patterns

### Tool Definition Pattern

**Schema-first approach**:
1. Define input schema with validation
2. Document what the tool does
3. Implement tool logic
4. Return structured output
5. Handle errors gracefully

**Best practices**:
- Validate all inputs
- Use descriptive parameter names
- Include parameter descriptions
- Return consistent output format
- Don't leak internal errors to LLM

### Dynamic Resource Pattern

**Template-based resources**:
1. Define URI template with parameters
2. Parse URI to extract parameters
3. Fetch/compute resource content
4. Return with appropriate MIME type
5. Handle missing/invalid resources

**Best practices**:
- Validate URI parameters
- Cache expensive resources
- Include metadata
- Handle 404/errors gracefully

### Progress Reporting Pattern

For long-running operations:
1. Report initial progress (0%)
2. Update progress periodically
3. Include status messages
4. Report completion (100%)
5. Handle cancellation

### Sampling Pattern

When you need LLM to generate content:
1. Prepare messages for LLM
2. Request sampling with parameters
3. Extract generated content
4. Validate/process response
5. Use in tool execution

### Elicitation Pattern

When you need user input:
1. Prepare prompt for user
2. Request elicitation
3. Receive user response
4. Validate input
5. Continue execution

## Testing Strategies

### Local Testing
- Manual stdio testing with echo/pipes
- MCP Inspector for interactive testing
- Unit tests for tool/resource logic
- Integration tests for full workflows

### Test Cases
- Happy path: Normal inputs, expected outputs
- Edge cases: Boundary values, empty inputs
- Error cases: Invalid inputs, failures
- Performance: Large inputs, timeouts

### Inspector Usage
- Test all tools interactively
- Verify schemas correct
- Check error handling
- Validate output format

## Security Considerations

### Input Validation
- Validate all tool inputs
- Sanitize file paths (prevent directory traversal)
- Limit resource access
- Rate limiting for expensive operations

### Authentication/Authorization
- Don't trust all requests
- Implement auth for production
- Scope permissions appropriately
- Audit access logs

### Secret Management
- Never hardcode secrets
- Use environment variables
- Rotate credentials
- Don't expose secrets in errors

### Safe File Operations
- Validate paths before access
- Restrict to allowed directories
- Check file sizes before reading
- Handle symlinks carefully

## Performance Optimization

### Caching
- Cache expensive computations
- Cache external API calls
- Use TTL for cache invalidation
- Share cache across tools

### Connection Pooling
- Reuse database connections
- Pool HTTP client connections
- Limit concurrent connections
- Handle connection failures

### Batching
- Batch database queries
- Group API calls
- Reduce round trips
- Parallelize independent operations

### Resource Cleanup
- Close connections properly
- Release resources on errors
- Use context managers/cleanup handlers
- Handle shutdown gracefully

## Common Pitfalls

### General
- Forgetting async for I/O operations
- Blocking the event loop
- Not handling errors in tools
- Poor error messages
- Missing input validation

### stdio Transport
- Logging to stdout (interferes with protocol)
- Not closing connections properly
- Synchronous I/O blocking server

### HTTP Transport
- Forgetting DNS rebinding protection
- Missing CORS headers
- Not cleaning up transport on disconnect
- Shared state across requests in stateless mode

## Debugging Tips

### Common Issues
- **Schema validation fails**: Check type mismatches, required fields
- **Transport errors**: Verify JSON-RPC format, check logs
- **Tools not appearing**: Check registration, schema correctness
- **Async errors**: Ensure all I/O is async, check event loop

### Debugging Tools
- MCP Inspector for interactive testing
- Structured logging for production
- Unit tests for tool logic
- Network debugging for HTTP transport

### Log Analysis
- Check stderr for server logs
- Verify JSON-RPC messages
- Inspect tool input/output
- Track error patterns

## Development Workflow

1. **Design**: Plan tools/resources/prompts
2. **Schema**: Define input/output schemas
3. **Implement**: Write tool logic with tests
4. **Test locally**: Use inspector/manual tests
5. **Deploy**: Choose transport and deploy
6. **Monitor**: Track usage and errors
7. **Iterate**: Improve based on feedback

## Language-Specific Implementations

Each language has specific SDK patterns:

### Python
- FastMCP for high-level API (decorators)
- Low-level Server for fine control
- Pydantic for schemas
- See: Python MCP agent for details

### TypeScript
- @modelcontextprotocol/sdk
- Zod for runtime validation
- ES modules required
- See: TypeScript MCP agent for details

## Success Criteria

MCP server is successful when:
- ✅ All tools/resources work correctly
- ✅ Schema validation prevents bad inputs
- ✅ Error handling graceful
- ✅ Tests pass (unit + integration)
- ✅ LLM can discover and use features
- ✅ Performance acceptable
- ✅ Logging sufficient for debugging

## References

- Language-specific MCP agents for implementation details
- Python/TypeScript instruction files for language standards
- MCP specification for protocol details
