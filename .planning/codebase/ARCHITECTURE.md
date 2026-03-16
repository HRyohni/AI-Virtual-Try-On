# Architecture

**Analysis Date:** 2026-03-16

## Pattern Overview

**Overall:** Single-script procedural pipeline

**Key Characteristics:**
- No application layers, modules, or classes - all logic is in one flat script
- Linear execution: load inputs → call external API → process response → save output
- Stateless: no persistence, sessions, or in-memory state between runs
- Entirely dependent on the Google Gemini generative AI API for the core transformation

## Layers

**Input Layer:**
- Purpose: Load source images from the local filesystem
- Location: `main.py` (lines 36–42)
- Contains: `Image.open()` calls for model and outfit images
- Depends on: Pillow (`PIL.Image`), local image files (`model.png`, `clothing_image3.png`)
- Used by: API call layer

**Prompt Layer:**
- Purpose: Define the natural language instruction sent alongside images to the AI model
- Location: `main.py` (lines 47–57)
- Contains: Hardcoded multi-line string (`comprehensive_prompt`)
- Depends on: Nothing (static string)
- Used by: API call layer

**API Call Layer:**
- Purpose: Send images and prompt to Google Gemini, receive generated image response
- Location: `main.py` (lines 61–64)
- Contains: `client.models.generate_content()` invocation
- Depends on: `google-genai` SDK, hardcoded API key (`genai.Client(api_key=...)` at line 10)
- Used by: Output layer

**Output Layer:**
- Purpose: Parse the API response, extract image bytes, save to disk, optionally display
- Location: `main.py` (lines 13–31, function `export_image`)
- Contains: `export_image()` function - the only named abstraction in the codebase
- Depends on: Pillow (`PIL.Image`, `io.BytesIO`), writable local filesystem
- Used by: Top-level script execution

## Data Flow

**Primary Flow - Outfit Transfer:**

1. Script starts; `genai.Client` is instantiated with a hardcoded API key
2. `model.png` and `clothing_image3.png` are opened as `PIL.Image` objects
3. Both images plus `comprehensive_prompt` are passed to `client.models.generate_content()`
4. Google Gemini `gemini-2.5-flash-image-preview` processes the multimodal request
5. Response object is passed to `export_image()`
6. `export_image()` iterates `response.candidates[0].content.parts` for `inline_data` parts
7. First image binary is decoded via `BytesIO`, opened as `PIL.Image`, and saved to disk
8. If `showImage=True`, the OS default image viewer opens the result

**Error Handling Flow:**
- `FileNotFoundError` on image load: prints message and calls `exit()` (lines 40–42)
- All other errors in `export_image`: caught by bare `except Exception as e`, prints error and raw response

**State Management:**
- No state. Each script run is fully independent. No database, cache, or session.

## Key Abstractions

**`export_image` function:**
- Purpose: Decode and persist a generated image from the Gemini API response
- Location: `main.py` (lines 13–31)
- Pattern: Simple utility function; accepts `(response, exportName, showImage=False)`
- Note: This is the only reusable abstraction in the codebase

**`comprehensive_prompt` string:**
- Purpose: Encodes the domain logic for how the outfit transfer should be performed
- Location: `main.py` (lines 47–57)
- Pattern: Hardcoded multiline string; all transfer behavior is controlled entirely through prompt engineering

## Entry Points

**`main.py`:**
- Location: `main.py`
- Triggers: Direct Python execution (`python main.py`)
- Responsibilities: All - client init, image loading, prompt construction, API call, output saving

## Error Handling

**Strategy:** Minimal, inline try/except

**Patterns:**
- `FileNotFoundError` at image load exits immediately with a user-friendly message
- `export_image` wraps its body in `try/except Exception` and prints the full raw response on failure
- No retries, no logging framework, no structured error types

## Cross-Cutting Concerns

**Logging:** `print()` statements only; no logging framework
**Validation:** None - no input validation on image format, size, or API key validity
**Authentication:** API key hardcoded as a string literal in `main.py` line 10; no environment variable loading

---

*Architecture analysis: 2026-03-16*
