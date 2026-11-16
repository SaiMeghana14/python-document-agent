# Python Document Agent

A small Python command-line application for importing, listing and inspecting documents in a local folder. This project is being built as part of the Python Foundations and Document Tools internship assignment.

## What it does

- Imports TXT, Markdown, CSV and text-based PDF files.
- Copies imported files into `data/storage/`; it does not move or edit the originals.
- Stores document details in `data/catalogue.json` so records remain available after restarting the program.
- Uses SHA-256 to skip files whose contents have already been imported. Files with the same name but different contents are kept as separate records.
- Shows a short content preview when a document is inspected.
- Reports unsupported image files and continues importing the rest of the folder.
- Skips PDFs that contain no extractable text and explains that OCR may be needed.
- Checks that imported paths remain inside the selected input folder.

## Project layout

```text
document-agent/
├── data/
│   └── .gitkeep
├── exercises/
│   ├── calculator.py
│   ├── data_tools.py
│   ├── document_example.py
│   ├── file_tools.py
│   ├── import_example.py
│   ├── imports_and_context.py
│   ├── interpreter_info.py
│   ├── logging_demo.py
│   ├── lookup_benchmark.py
│   ├── main.py
│   ├── python_fundamentals.py
│   └── storage_example.py
├── samples/
│   └── input/
│       ├── company_policy.txt
│       ├── expenses.csv
│       └── meeting_notes.md
├── src/document_agent/
│   ├── __init__.py
│   ├── __main__.py
│   ├── catalogue.py
│   ├── cli.py
│   ├── importer.py
│   ├── models.py
│   └── readers.py
├── tests/
├── .gitignore
├── .python-version
├── pyproject.toml
└── README.md
```

## Setup on Windows (PowerShell)

Install Python 3.13 and `uv`, then open this folder in VS Code. Run:

```powershell
uv sync
```

This creates the virtual environment, installs the project and its dependencies, and creates `uv.lock`.

## Run the application

Import the sample documents:

```powershell
uv run docagent import samples/input
```

List imported documents:

```powershell
uv run docagent list
```

Inspect one document by copying its ID from the list:

```powershell
uv run docagent inspect YOUR_DOCUMENT_ID
```

The module form also works:

```powershell
uv run python -m document_agent --help
```

## Run checks

```powershell
uv run pytest -v
uv run ruff check .
uv run mypy
```

## Exercise scripts

```powershell
uv run python exercises/calculator.py
uv run python exercises/document_example.py
uv run python exercises/import_example.py
uv run python exercises/imports_and_context.py
uv run python exercises/data_tools.py
uv run python exercises/file_tools.py
uv run python exercises/python_fundamentals.py
uv run python exercises/logging_demo.py
uv run python exercises/lookup_benchmark.py
```

Run scripts from the project root so the sample file paths resolve.

## Notes and current limits

- Image OCR is not included. PNG/JPG/JPEG files are reported as unsupported.
- A PDF must contain selectable text for this version to import it.
- CSV files are validated for a header row and consistent column counts.
- If the JSON catalogue is malformed, the application reports the problem rather than silently replacing the existing data.
- `data/storage/` and the generated catalogue are local runtime data and are ignored by Git.

## Development checklist

- [x] Initial package and CLI structure
- [x] Document metadata model
- [x] TXT, Markdown, CSV and text-PDF readers
- [x] SHA-256 duplicate detection
- [x] Managed storage and JSON catalogue
- [x] List and inspect commands
- [x] Initial automated tests
- [ ] Add sample selectable-text PDFs and a scanned/image-only PDF for manual testing
- [x] Add a small logging example and a `caplog` test
- [ ] Compare a manual `python -m venv` + `pip` setup with the `uv` workflow and note the differences
- [ ] Capture a debugger breakpoint while stepping through `import_folder`
- [ ] Complete the assignment work log and add the final Git commit ID to the mentor update
