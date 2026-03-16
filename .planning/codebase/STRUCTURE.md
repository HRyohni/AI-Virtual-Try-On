# Codebase Structure

**Analysis Date:** 2026-03-16

## Directory Layout

```
AI-Virtual-Try-On/
├── main.py                                  # Sole application script
├── requirements.txt                         # Pinned Python dependencies
├── README.md                                # Project documentation
├── .gitattributes                           # Git line-ending config
├── model.png                                # Input: person to dress (runtime asset)
├── clothing_image2.png                      # Input: outfit source image (runtime asset)
├── model_with_transferred_outfit 2.png      # Output: generated result (runtime artifact)
└── examples/                                # Example input/output image pairs
    ├── clothing_image.png
    ├── clothing_image1.png
    ├── clothing_image3.png
    ├── model_with_transferred_outfit.png
    ├── model_with_transferred_outfit 1.png
    └── model_with_transferred_outfit 3.png
```

## Directory Purposes

**Root (`/`):**
- Purpose: Contains the entire application - there are no subdirectories for source code
- Contains: Single Python script, dependency manifest, documentation, and image assets
- Key files: `main.py`, `requirements.txt`, `README.md`

**`examples/`:**
- Purpose: Stores reference input/output image pairs demonstrating the tool's capability
- Contains: Clothing source images and their corresponding generated outfit-transfer results
- Key files: `clothing_image.png`, `clothing_image1.png`, `clothing_image3.png` (inputs); `model_with_transferred_outfit*.png` (outputs)
- Generated: Yes (outputs are AI-generated)
- Committed: Yes (used for README demonstration)

**`.planning/codebase/`:**
- Purpose: GSD codebase analysis documents for AI-assisted development
- Contains: Architecture and structure analysis markdown files
- Generated: Yes (by GSD map-codebase tooling)
- Committed: Yes

## Key File Locations

**Entry Points:**
- `main.py`: The sole executable; run directly with `python main.py`

**Configuration:**
- `requirements.txt`: Pinned dependency versions (note: file is UTF-16 encoded - has wide-character spacing)
- `.gitattributes`: LF normalization rule for all text files

**Core Logic:**
- `main.py`: All application logic - client init, image loading, API call, response handling

**Runtime Input Assets (required at run time, not tracked as code):**
- `model.png`: Person to be dressed - must be present in project root before running
- `clothing_image3.png`: Outfit source image - filename referenced directly in `main.py` line 39

**Runtime Output Artifacts:**
- `model_with_transferred_outfit 3.png`: Generated result written to project root

**Reference Examples:**
- `examples/`: Input images and expected-quality outputs for reference

## Naming Conventions

**Files:**
- Python script: lowercase with no separator (`main.py`)
- Input images: descriptive lowercase with underscore (`clothing_image2.png`, `model.png`)
- Output images: descriptive lowercase with spaces (`model_with_transferred_outfit 2.png`) - note spaces in filenames, not underscores for outputs
- Example outputs follow the same space-separated pattern with a numeric suffix

**Directories:**
- Lowercase, no separator (`examples`, `.planning`)

## Where to Add New Code

**New script or feature variant:**
- Place directly in project root alongside `main.py` (e.g., `batch_process.py`)
- No `src/` or package structure exists; the project uses flat layout

**New utility function:**
- Add to `main.py` directly, above the `# --- Main Logic ---` comment (line 33)
- No separate `utils.py` or module structure currently exists

**New example outputs:**
- Place in `examples/` using the naming pattern `clothing_imageN.png` (input) and `model_with_transferred_outfit N.png` (output)

**Configuration or environment loading:**
- No `.env` loader exists yet; the README recommends adding one using the `os` library
- If added, place `.env` in the project root and load it at the top of `main.py`

## Special Directories

**`examples/`:**
- Purpose: Human-readable demonstration of tool output quality
- Generated: Outputs are AI-generated; inputs are curated manually
- Committed: Yes - serves as README illustration assets

**`.planning/`:**
- Purpose: GSD AI development planning artifacts
- Generated: Yes
- Committed: Yes

---

*Structure analysis: 2026-03-16*
