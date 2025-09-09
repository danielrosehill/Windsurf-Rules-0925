---
trigger: always_on
---

# General Tools & Conventions

## Tool Prioritization

### Scrape before using headless browsers
If Daniel prompts something like: "this URL has the API context that we need" then you should scrape that content (for example using Firecrawl MCP or similar). Only if that approach proves unfruitful should you move to using headless browsers to attempt to extract the documentation.

## General Development Conventions
- Focus on creating replicable, maintainable solutions
- Prefer existing tools and established patterns
- Document decisions when they involve significant complexity