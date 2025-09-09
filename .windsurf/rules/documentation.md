---
trigger: always_on
---

# Documentation Guidelines

## Core Principle
**Less is more** - Only contribute to existing docs or add new docs if they would be helpful. Don't create documentation just for the sake of it.

## Repository Context
Unless otherwise instructed, assume these are **private repositories and projects**. Don't create general purpose README docs unless Daniel explicitly wants that.

## Documentation Types

### 1. Session Logs
Provide notes about what was achieved during a lengthy editing session:
- Date and summary
- What's blocking progress
- What was accomplished
- Next steps

### 2. Reference Documentation
Daniel may import this into a wiki for future reference:
- Use descriptive subfolders like 'instructions'
- Focus on how to use and maintain what you created
- Make it searchable and organized

### 3. Architecture & Design Reference
When it took significant effort to figure out an approach:
- High-level overview of the solution
- Key decisions and rationale
- Implementation patterns used

## Structure Guidelines
- Nest docs at `/docs` relative to repo root
- Use clear subfolder organization
- Make documentation self-contained and useful for future reference

## AI Workspace Structure
Within every project, you may wish to configure and use a folder structure to receive instructions from Daniel and write them back to him. If this is partially set up, finish it and use it.

Paths are relative to the repo base:

| Path                        | Purpose                               |
| --------------------------- | ------------------------------------- |
| `/ai-workspace/for-ai/`     | Assistant input (logs, prompts, etc.) |
| `/ai-workspace/for-daniel/` | Assistant output, notes, logs, docs   |

## Usage Guidelines
- Use `/for-daniel/` for procedures, logs, and internal docs
- Complete partially set up workspace structures
- Follow the established pattern when it exists