# CLI Tools & MCP Configuration

## Authenticated CLIs
The following tools are installed and authenticated:

- **`gh`** - GitHub CLI
- **`wrangler`** - Cloudflare CLI
- **`b2`** - Backblaze B2 object storage
- **`wasabi`** - Wasabi object storage
- **`op`** - 1Password CLI for secrets management
- **Netlify CLI** - Static site deployment (authenticated)

## Secrets Management
- **Primary method**: Use `.env` files for secret handling
- For private repositories, `.env` files may be committed to version control
- If committing `.env` to private repos, rename to similar values (e.g., `.env.local`, `.environment`) to work around gitignore rules that block `.env`

## MCP Configuration

### Configuration Location
- **MCP Config**: `/home/daniel/.codeium/windsurf/mcp_config.json`
- **Development Location**: Create MCP servers at `~/mcp`

### Tool Limit Management
- Windsurf has a limit of **100 active tools**
- Be proactive in supporting Daniel to prune unused MCPs
- Quality over quantity - activate tools judiciously

### Priority Hierarchy
When you could achieve a task through multiple methods:

1. **MCP** (preferred)
2. SSH into server
3. Direct CLI invocation

Always favor using MCPs when available.

### Clarification Protocol
- Ask Daniel to clarify the purpose of an MCP if you're unsure
- Don't assume functionality - verify before using

### Development Guidelines
When developing new MCP servers:
- Place them in `~/mcp/`
- Follow Daniel's existing patterns
- Document tool capabilities clearly
- Consider tool count impact on the 100-tool limit
