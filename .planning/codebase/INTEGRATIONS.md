# External Integrations

**Analysis Date:** 2026-03-16

## APIs & External Services

**AI / Generative Image:**
- Google Gemini API - Multimodal image generation used for virtual outfit transfer
  - SDK/Client: `google-genai==1.36.0` (`from google import genai`)
  - Client instantiation: `genai.Client(api_key='your api key')` in `main.py` line 10
  - Model used: `gemini-2.5-flash-image-preview`
  - Call site: `main.py` lines 61-64 via `client.models.generate_content()`
  - Auth: API key hardcoded in `main.py`; README recommends env var `GOOGLE_API_KEY`

**OpenAI (present but unused):**
- `openai==0.27.10` is listed in `requirements.txt` but not imported or called in `main.py`
  - Auth: Not configured
  - Status: Dependency present, integration not implemented

## Data Storage

**Databases:**
- None

**File Storage:**
- Local filesystem only
  - Input images read from project root: `model.png`, `clothing_image3.png`
  - Output image written to project root: `model_with_transferred_outfit 3.png`
  - All filenames are hardcoded in `main.py` lines 37-39, 67

**Caching:**
- None

## Authentication & Identity

**Auth Provider:**
- Google AI API Key (string)
  - Implementation: Passed directly to `genai.Client(api_key=...)` in `main.py` line 10
  - Current state: Placeholder string `'your api key'` - must be replaced before use
  - Recommended state (per README): Load from `.env` file using `os` module; `.env` file not present

## Monitoring & Observability

**Error Tracking:**
- None - basic `try/except` blocks with `print()` statements in `main.py`

**Logs:**
- `print()` to stdout only; no structured logging

## CI/CD & Deployment

**Hosting:**
- Local script execution only; no deployment platform

**CI Pipeline:**
- None detected

## Environment Configuration

**Required env vars:**
- `GOOGLE_API_KEY` - Google Gemini API key (recommended by README, not yet implemented in code)

**Secrets location:**
- Currently: hardcoded in `main.py` line 10 (insecure; should be replaced)
- Recommended: `.env` file in project root (not present)

## Webhooks & Callbacks

**Incoming:**
- None

**Outgoing:**
- None - all communication is synchronous request/response via `client.models.generate_content()`

---

*Integration audit: 2026-03-16*
