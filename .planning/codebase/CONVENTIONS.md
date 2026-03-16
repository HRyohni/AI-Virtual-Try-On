# Coding Conventions

**Analysis Date:** 2026-03-16

## Overview

This is a minimal single-file Python project. The entire application is contained in `main.py`. Convention patterns are inferred from that one source file.

## Naming Patterns

**Files:**
- Single entry-point file: `main.py`
- Output images use descriptive names with spaces allowed: `model_with_transferred_outfit 3.png`

**Functions:**
- snake_case: `export_image`
- Parameters use camelCase for booleans and mixed terms: `exportName`, `showImage`
- Note: parameter naming is inconsistent - `exportName` uses camelCase while `response` uses snake_case. No enforced convention.

**Variables:**
- snake_case for local variables: `model_image`, `outfit_image`, `image_parts`, `comprehensive_prompt`
- Module-level client instantiation uses snake_case: `client`

**Constants/Prompts:**
- Descriptive snake_case: `comprehensive_prompt`

## Code Style

**Formatting:**
- No formatter config detected (no `.prettierrc`, `pyproject.toml`, `setup.cfg`, or `.flake8`)
- Indentation: 4 spaces (standard Python)
- Line length: Not enforced by config; prompt string uses triple-quoted multiline strings

**Linting:**
- No linting config detected
- No `pyproject.toml`, `.flake8`, `.pylintrc`, or `tox.ini` present

## Import Organization

**Current order in `main.py`:**
1. Third-party SDK imports: `from google import genai`, `from google.genai import types`
2. Standard library imports (out of order): `from PIL import Image`, `import time`, `from io import BytesIO`
3. Additional third-party: `from traitlets.config.loader import ConfigLoader`

**Note:** Imports are not organized per PEP 8 (stdlib before third-party). `import time` and `from traitlets.config.loader import ConfigLoader` appear unused in the current code.

## Error Handling

**Patterns observed:**

Outer try/except for file loading at module level:
```python
try:
    model_image = Image.open('model.png')
    outfit_image = Image.open('clothing_image3.png')
except FileNotFoundError as e:
    print(f"Error: Make sure the image file '{e.filename}' exists.")
    exit()
```

Inner try/except in helper function, catching broad `Exception`:
```python
try:
    # ... image processing
except Exception as e:
    print(f"An error occurred: {e}")
    print("--- Full Response ---")
    print(response)
```

**Error handling style:**
- Use `print()` for all error output (no logging framework)
- Use `exit()` (not `sys.exit()`) for fatal errors
- Broad `except Exception` is used in the helper function - no re-raising
- No custom exception classes

## Logging

**Framework:** None - `print()` only

**Patterns:**
- Emoji prefixes used for status messages: `"✅ Successfully saved..."`, `"❌ No image data..."`, `"🚀Generating image..."`
- f-strings used for all string interpolation
- Debug info printed directly to stdout on error: `print(response)`

## Comments

**Usage observed:**
- Inline comments describe variable purpose: `# model is a person who you want to dress`
- Section separators use `# ---` style: `# --- Main Logic ---`
- Inline hints for customization: `# you can change your prompt`, `# name your output file`
- No docstrings on functions
- No type annotations

## Function Design

**Size:** `export_image` is small (~15 lines). Main logic runs at module level, not wrapped in a `main()` function or `if __name__ == "__main__":` guard.

**Parameters:**
- Mix of positional and keyword args: `export_image(response, exportName, showImage=False)`
- No type hints on parameters or return values

**Return Values:**
- `export_image` has no return value (implicitly returns `None`)

## Module Design

**Structure:**
- No package structure; single script `main.py`
- No `if __name__ == "__main__":` guard - module-level code runs on import
- Client instantiated at module level with hardcoded API key: `client = genai.Client(api_key='your api key')`
- No `.env` loading despite README recommending it

## Security Notes

- API key is hardcoded as a placeholder string in `main.py` (line 10). README documents the recommended fix (use environment variable), but the code does not implement it.
- File paths are hardcoded strings, not configurable.

---

*Convention analysis: 2026-03-16*
