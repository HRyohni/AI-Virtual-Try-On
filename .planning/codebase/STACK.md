# Technology Stack

**Analysis Date:** 2026-03-16

## Languages

**Primary:**
- Python 3.7+ - All application logic in `main.py`

**Secondary:**
- None

## Runtime

**Environment:**
- Python 3.7+ (minimum required per README)

**Package Manager:**
- pip
- Lockfile: `requirements.txt` present (pinned versions)

## Frameworks

**Core:**
- None - single-script application, no web or application framework

**Testing:**
- Not detected

**Build/Dev:**
- IPython 8.37.0 - interactive shell support (dev utility)

## Key Dependencies

**Critical:**
- `google-genai==1.36.0` - Primary Google Generative AI SDK used in `main.py` for `genai.Client` and content generation
- `google-ai-generativeai` (via `google-generativeai==0.6.15`) - underlying Google AI language library
- `Pillow==11.3.0` - Image loading, saving, and display (`PIL.Image`) used in `main.py`

**Infrastructure:**
- `requests==2.32.5` - HTTP client (transitive dependency for API calls)
- `httpx==0.28.1` - Async HTTP client (used by Google SDK)
- `grpcio==1.74.0` - gRPC transport for Google API calls
- `protobuf==5.29.5` - Protocol buffers for Google API serialization
- `pydantic==2.11.9` - Data validation (used by Google SDK)
- `tqdm==4.67.1` - Progress bar utility
- `tenacity==9.1.2` - Retry logic for API calls
- `tiktoken==0.3.3` - Token counting (OpenAI tokenizer, present but `openai==0.27.10` is also installed)
- `openai==0.27.10` - OpenAI SDK (present in requirements but not used in `main.py`)
- `websockets==15.0.1` - WebSocket support (transitive)
- `beautifulsoup4==4.13.5` - HTML parsing (transitive)

**Data Handling:**
- `io.BytesIO` (stdlib) - In-memory binary stream for image decoding in `main.py`

## Configuration

**Environment:**
- API key is hardcoded as a placeholder string in `main.py` line 10: `api_key='your api key'`
- README recommends storing key in `.env` file as `GOOGLE_API_KEY` and loading via `os` module, but this is not implemented in the current script
- No `.env` file or environment loading library (e.g., `python-dotenv`) is present

**Build:**
- No build config files; project is a single executable script

## Platform Requirements

**Development:**
- Python 3.7+
- pip for dependency installation
- Input image files must be named `model.png` and `clothing_image3.png` (hardcoded in `main.py` lines 37-39)
- Output image saved as `model_with_transferred_outfit 3.png` (hardcoded in `main.py` line 67)

**Production:**
- Script-only; no deployment target. Runs locally via `python main.py`

---

*Stack analysis: 2026-03-16*
