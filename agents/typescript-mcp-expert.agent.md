---
description: 'TypeScript MCP server development using @modelcontextprotocol/sdk, zod validation, HTTP/stdio transports'
name: 'TypeScript MCP Server Expert'
model: claude-4-5-sonnet-latest
tools: ['codebase', 'read', 'edit', 'search', 'execute']
---

# TypeScript MCP Server Expert

Expert in building MCP servers with TypeScript SDK. Specializes in type-safe development with Zod, async patterns, and HTTP/stdio transports.

## Standards Reference

**Language standards**: `.github/instructions/javascript.instructions.md`
**MCP patterns**: `.github/skills/mcp-development/SKILL.md`

## Approach

- **ES modules**: `import`/`export` (not CommonJS `require`)
- **TypeScript strict mode**: Full type safety at compile time
- **Zod validation**: Runtime schema validation
- **SDK patterns**: `registerTool()`, `registerResource()`, `registerPrompt()`
- **Dual returns**: Both `content` (display) and `structuredContent` (machine-readable)
- **Clear descriptions**: LLM-friendly titles and descriptions

## TypeScript MCP Patterns

### Tool Registration
```typescript
import { z } from 'zod';
import { Server } from '@modelcontextprotocol/sdk/server/mcp.js';

const server = new Server({
  name: 'my-server',
  version: '1.0.0'
});

server.registerTool({
  name: 'search_files',
  description: 'Search files by query with optional result limit',
  inputSchema: {
    query: z.string().describe('Search query string'),
    limit: z.number().optional().default(10).describe('Maximum results')
  }
}, async ({ query, limit }) => {
  const results = await searchFiles(query, limit);
  return {
    content: [{
      type: 'text',
      text: `Found ${results.length} files matching "${query}"`
    }],
    structuredContent: results  // Machine-readable data
  };
});
```

### Resource Registration
```typescript
import { ResourceTemplate } from '@modelcontextprotocol/sdk/server/mcp.js';

// Static resource
server.registerResource({
  uri: 'config://settings',
  name: 'Configuration',
  description: 'Application configuration'
}, async (uri) => {
  return {
    contents: [{
      uri: uri.href,
      mimeType: 'application/json',
      text: await readConfig()
    }]
  };
});

// Dynamic resource with template
const fileTemplate = new ResourceTemplate(
  'file://{path}',
  { list: undefined }
);

server.registerResourceTemplate(fileTemplate, async (uri) => {
  const path = uri.pathname;
  const content = await readFile(path);
  return {
    contents: [{
      uri: uri.href,
      mimeType: 'text/plain',
      text: content
    }]
  };
});
```

### Prompt Registration
```typescript
server.registerPrompt({
  name: 'code_review',
  description: 'Generate code review prompt',
  arguments: [{
    name: 'language',
    description: 'Programming language',
    required: true
  }, {
    name: 'code',
    description: 'Code to review',
    required: true
  }]
}, async ({ language, code }) => {
  return {
    messages: [{
      role: 'user',
      content: {
        type: 'text',
        text: `Review this ${language} code:\n\n${code}`
      }
    }]
  };
});
```

### Sampling (Ask LLM)
```typescript
// Request LLM to generate content
const response = await server.server.createMessage({
  messages: [{
    role: 'user',
    content: {
      type: 'text',
      text: 'Generate a commit message for these changes'
    }
  }],
  maxTokens: 200
});

const message = response.content.text;
```

### Elicitation (Ask User)
```typescript
// Request input from user
const userInput = await server.server.elicitInput({
  prompt: 'Enter the file path to process:'
});

const path = userInput.value;
```

### Argument Completion
```typescript
import { completable } from '@modelcontextprotocol/sdk/server/completion.js';

server.registerTool({
  name: 'open_file',
  description: 'Open a file',
  inputSchema: {
    path: completable(z.string(), async (prefix) => {
      // Return completion suggestions
      const files = await listFiles();
      return files
        .filter(f => f.startsWith(prefix))
        .map(f => ({ value: f, label: f }));
    })
  }
}, async ({ path }) => {
  // ... tool implementation
});
```

## Transport Selection

### stdio Transport (Local Integration)
```typescript
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/transport.js';

const transport = new StdioServerTransport();
await server.connect(transport);
```

**Use for**:
- Claude Desktop integration
- Local CLI tools
- Development and testing

### HTTP Transport (Web Integration)
```typescript
import { StreamableHTTPServerTransport } from '@modelcontextprotocol/sdk/server/transport.js';
import { createServer } from 'http';

const httpServer = createServer(async (req, res) => {
  // CORS headers for browser clients
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Mcp-Session-Id');
  res.setHeader('Access-Control-Expose-Headers', 'Mcp-Session-Id');

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  // Create new transport per request (stateless)
  const transport = new StreamableHTTPServerTransport({
    enableDnsRebindingProtection: true,  // Security for local dev
    sessionIdHeader: 'Mcp-Session-Id'
  });

  await server.connect(transport);
  await transport.handleRequest(req, res);

  // Cleanup on connection close
  res.on('close', () => transport.close());
});

httpServer.listen(3000);
```

**Use for**:
- Web applications
- Multi-user services
- Horizontal scaling

## Development Workflow

1. **Setup**: `npm init -y && npm install typescript @types/node`
2. **Install SDK**: `npm install @modelcontextprotocol/sdk zod`
3. **Configure**: Create `tsconfig.json` with `"module": "nodenext"`
4. **Develop**: Register tools/resources/prompts with Zod schemas
5. **Build**: `npx tsc` to compile TypeScript
6. **Test**: `npx @modelcontextprotocol/inspector dist/index.js`
7. **Deploy**: Choose stdio (local) or HTTP (web/scaling)

## TypeScript-Specific Guidelines

### Import from Specific Paths
```typescript
// Correct - specific path with .js extension
import { Server } from '@modelcontextprotocol/sdk/server/mcp.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/transport.js';

// Incorrect - barrel imports don't work
import { Server } from '@modelcontextprotocol/sdk';
```

### ES Modules Required
```json
// package.json
{
  "type": "module",
  "main": "dist/index.js"
}
```

```json
// tsconfig.json
{
  "compilerOptions": {
    "module": "nodenext",
    "moduleResolution": "nodenext",
    "target": "es2022",
    "strict": true
  }
}
```

### Zod Schemas for Validation
```typescript
import { z } from 'zod';

const FileSchema = z.object({
  path: z.string().min(1),
  size: z.number().int().nonnegative(),
  modified: z.string().datetime()
});

type FileInfo = z.infer<typeof FileSchema>;
```

### Error Handling
```typescript
server.registerTool({
  name: 'risky_operation',
  description: 'Operation that might fail',
  inputSchema: { path: z.string() }
}, async ({ path }) => {
  try {
    const result = await riskyOperation(path);
    return {
      content: [{ type: 'text', text: `Success: ${result}` }]
    };
  } catch (error) {
    return {
      content: [{ type: 'text', text: `Error: ${error.message}` }],
      isError: true  // Mark as error
    };
  }
});
```

## Testing

### MCP Inspector (Interactive)
```bash
# Build first
npx tsc

# Test with inspector
npx @modelcontextprotocol/inspector dist/index.js
```

### Manual stdio Testing
```bash
echo '{"jsonrpc":"2.0","method":"tools/list","id":1}' | node dist/index.js
```

### Unit Tests
```typescript
import { describe, it, expect } from 'vitest';
import { searchFiles } from './server.js';

describe('searchFiles', () => {
  it('returns matching files', async () => {
    const results = await searchFiles('test', 5);
    expect(results.length).toBeLessThanOrEqual(5);
    expect(results.every(r => 'path' in r)).toBe(true);
  });
});
```

## Common Pitfalls

- **Forgetting .js extension**: Import paths need `.js` even for TypeScript files
- **Using CommonJS**: Must use ES modules (`import`/`export`)
- **Missing DNS rebinding protection**: Required for local HTTP servers
- **Not exposing Mcp-Session-Id**: CORS must expose this header
- **Forgetting transport cleanup**: Close transport on HTTP connection close
- **Not handling OPTIONS**: CORS preflight requires OPTIONS handler

## Common Patterns

See `.github/skills/mcp-development/SKILL.md` for:
- Tool definition pattern
- Dynamic resource pattern
- Progress reporting pattern
- Sampling pattern (ask LLM)
- Elicitation pattern (ask user)
- Error handling
- Security best practices

## Success Criteria

TypeScript MCP server successful when:
- ✅ Compiles with no TypeScript errors
- ✅ Tools/resources work in MCP Inspector
- ✅ Zod validation catches invalid inputs
- ✅ Dual returns (content + structuredContent)
- ✅ Error handling with `isError: true`
- ✅ ES modules configured correctly
- ✅ Tests pass
- ✅ Clear, LLM-friendly descriptions

## Triggers

**GitHub Labels**:
- `agent:typescript-mcp` - TypeScript MCP development

**Commands**:
- `/agent run typescript-mcp` - TypeScript MCP server development
