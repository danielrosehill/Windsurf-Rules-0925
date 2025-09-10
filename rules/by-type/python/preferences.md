# Python Development Preferences

## Virtual Environment Management
- **Primary**: Use `uv` to create virtual environments
- **Fallback**: Switch to regular `venv` if running into package difficulties

## Environment Activation
- **Always activate** the environment after creating it
- **Verify activation** before attempting to run scripts
- **First troubleshooting step**: Check if virtual environment is active when encountering package availability errors

## Best Practices
- Ensure environment is active before running any Python scripts
- If package errors occur, verify environment activation first
- Use uv unless specific compatibility issues arise

## Tool Priorities
1. **UV** (primary environment manager)
2. Regular `venv` (fallback for compatibility issues)

## GUI Framework Preferences
- **PySide6** - Preferred Qt binding for Python
- **Tauri** - For modern cross-platform applications
- **Qt** - Direct Qt usage when needed
- **Electron** - Fallback for web-based desktop apps

Do not use Tkinter unless there is no other option!

## Package Management
- Always create requirements.txt with specific versions
- Prefer pinned dependencies for reproducibility
- Use virtual environments for all projects
- Test in clean environments before deployment
