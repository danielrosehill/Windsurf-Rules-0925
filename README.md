# Windsurf Rules - September 2025

Sep 9, 2025

A refactored version of my Windsurf rules to align with Windsurf IDE's (wisdomous) decision to abandon singular/monolithic Windsurf rules files in favor of individual rules "modules."

This approach accords nicely with emerging best practices in agentic code generation and has a number of benefits - including making it easier to create swap out sets of preferences.

Shared lest anyone want to follow a similar template or draws ideas from the constituent elements as I've created them. 

## Configuration Modules

| Category | Module | Description |
|----------|--------|-------------|
| **Environment** | [Environment & System](rules/environment/environment.md) | User profile, system specs, and basic configuration |
| | [Infrastructure](rules/environment/infrastructure.md) | Container deployment and infrastructure setup |
| | [Network Configuration](rules/environment/network.md) | LAN IP mapping and network context |
| **Development** | [Python Preferences](rules/python/preferences.md) | Virtual environment management and Python conventions |
| | [Documentation](rules/documentation.md) | Documentation standards and practices |
| **DevOps** | [Deployment Guidelines](rules/devops/deployment.md) | Containerization and deployment processes |
| **Tool Usage** | [CLI & MCP Tools](rules/tool-usage/cli-mcp.md) | Command-line tools and MCP server configurations |
| | [Tools & Conventions](rules/tool-usage/tools-conventions.md) | General tool usage patterns and conventions |
| **Workflow** | [Workflow Execution](rules/workflow/workflow-execution.md) | Task execution and workflow management |
| **Stack Selection** | [LLM & AI Services](stack-selection/llm-ai.md) | AI service preferences and configurations |
| | [Technology Stack](stack-selection/technology-stack.md) | Core technology preferences and choices |
| **Style** | [Style Boundaries](style/style-boundaries.md) | Code style and formatting guidelines |

I update my Windsurf Rules periodically so (depending on what my tooling looks like going forward) I may update this in the future.