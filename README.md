# Python Document Agent

A beginner-friendly command-line document library built for the Python Foundations and Document Tools assignment.

## Features

- Import TXT, Markdown, CSV and PDFs that contain extractable text.
- Copy accepted files into managed storage without changing the originals.
- Save document details in a JSON catalogue so they remain available after restarting.
- Detect duplicate content using SHA-256. Different files with the same name are kept when their contents differ.
- List documents and inspect their metadata and content preview.
- Report unsupported images and PDFs with no extractable text without stopping the import batch.

## Project structure

```text
python-document-agent/
├── data/
│   └── .gitkeep
├── docs/
│   └── assignment-notes.md
├── exercises/
│   ├── README.md
│   ├── calculator.py
│   ├── create_pdf_samples.py
│   ├── data_tools.py
│   ├── file_tools.py
│   ├── import_example.py
│   ├── imports_and_context.py
│   ├── interpreter_info.py
│   ├── logging_demo.py
│   ├── lookup_benchmark.py
│   ├── python_fundamentals.py
│   └── storage_example.py
├── samples/input/
├── src/document_agent/
├── tests/
├── .gitignore
├── .python-version
├── README.md
├── pyproject.toml
└── uv.lock
```

## Setup (Windows PowerShell)

Install Python 3.13 and uv. Open the project folder in VS Code and run:

```powershell
uv sync --locked
```

## Run the document application

```powershell
uv run docagent import samples/input
uv run docagent list
uv run docagent inspect YOUR_DOCUMENT_ID
```

Copy a real ID from the `list` output before running `inspect`.

The catalogue and accepted copies are created locally in `data/catalogue.json` and `data/storage/`. They are intentionally excluded from Git.

## Run the exercises

See [exercises/README.md](exercises/README.md) for the topic-to-file guide. For example:

```powershell
uv run python exercises/python_fundamentals.py
uv run python exercises/imports_and_context.py
uv run python exercises/data_tools.py
```

The data exercise reads the existing `samples/input/expenses.csv` and writes a cleaned copy to `data/expenses_cleaned.csv`. It does not edit the source CSV.

Optional PDF boundary samples can be created with:

```powershell
uv run python exercises/create_pdf_samples.py
```

This creates additional files in `samples/input/`. Only run it if you want to generate the test samples; it does not alter the three original sample documents.

## Checks

```powershell
uv run python -m pytest -v
uv run python -m ruff check .
uv run python -m mypy src
```

Record the actual output from your machine in `docs/assignment-notes.md`. Do not claim checks passed until you have run them.

## Design notes

- `readers.py` contains format-specific reading code.
- `importer.py` coordinates validation, duplicate detection and copying.
- `models.py` defines the document record.
- `catalogue.py` reads and writes JSON metadata.
- `storage.py` calculates hashes and copies accepted files.
- `cli.py` handles command-line arguments and displays results.

The JSON catalogue is kept separate from readers and command handling. In a later version, the persistence functions in `catalogue.py` could be replaced with database operations without rewriting the file readers.

## Current limits

- OCR is not implemented. Image files are unsupported, and a PDF with no extractable text is skipped with an OCR-needed message.
- The tool reads CSV data but does not automatically clean or modify imported source files.
- The sample files are small learning examples, not real company documents.
