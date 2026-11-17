# Python Document Agent

A Python command-line application for importing, storing, listing and inspecting documents. This project was developed as part of the **Python Foundations and Document Tools internship assignment**.

The project also contains Python practice exercises covering programming fundamentals, file handling, data processing, logging, testing and debugging.

## 1. Features

The application supports:

- Importing `.txt`, `.md`, `.csv` and text-based `.pdf` files.
- Copying accepted documents into managed storage without changing the original files.
- Saving document information in a JSON catalogue.
- Generating a SHA-256 hash for each document to identify duplicate content.
- Skipping documents whose content has already been imported.
- Keeping files with the same name but different content as separate documents.
- Listing imported documents.
- Inspecting a document and viewing a content preview.
- Reporting unsupported image files.
- Detecting PDFs without extractable text and explaining that OCR may be required.
- Checking input paths to help prevent files outside the selected folder from being imported.

**Important:** Image OCR is not implemented. PNG, JPG and JPEG files are unsupported. A PDF must contain extractable text to be imported.

## 2. Project structure

```text
python-document-agent/
│
├── data/
│   └── .gitkeep
│
├── docs/
│   └── assignment-notes.md
│
├── exercises/
│   ├── calculator.py
│   ├── create_pdf_samples.py
│   ├── data_tools.py
│   ├── debugger_practice.py
│   ├── file_tools.py
│   ├── import_example.py
│   ├── imports_and_context.py
│   ├── interpreter_info.py
│   ├── logging_demo.py
│   ├── lookup_benchmark.py
│   ├── python_fundamentals.py
│   ├── storage_example.py
│   └── README.md
│
├── samples/
│   ├── input/
│   └── manifest.csv
│
├── src/
│   └── document_agent/
│       ├── __init__.py
│       ├── __main__.py
│       ├── catalogue.py
│       ├── cli.py
│       ├── importer.py
│       ├── models.py
│       └── readers.py
│
├── tests/
│   ├── conftest.py
│   ├── test_catalogue.py
│   ├── test_importer.py
│   ├── test_logging.py
│   └── test_readers.py
│
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
└── README.md
```

The application creates its runtime files under `data/`, including the JSON catalogue and managed document storage. These generated files are local application data and are not intended to be committed to Git.

## 3. Technologies used

| Technology | Purpose |
|---|---|
| Python 3.13 | Main programming language |
| uv | Project and dependency management |
| pypdf | Reading text from PDF files |
| pandas | CSV cleaning and data analysis |
| NumPy | Array operations and broadcasting |
| pytest | Automated testing |
| Ruff | Code style and lint checks |
| mypy | Static type checking |
| hashlib | SHA-256 content hashing |
| pathlib | File and directory handling |
| argparse | Command-line argument handling |
| logging | Application log messages |

## 4. Setup on Windows

Install Python 3.13 and uv.

Open PowerShell in the project folder:

```powershell
cd D:\python-document-agent
```

Install the project dependencies:

```powershell
uv sync
```

This creates or updates the project's virtual environment and installs the dependencies specified in `pyproject.toml` and `uv.lock`.

## 5. Running the application

Run these commands from the project root.

### Display available commands

```powershell
uv run docagent --help
```

The application provides three main commands: `import`, `list` and `inspect`.

### Import documents

```powershell
uv run docagent import samples/input
```

This reads supported files from the input folder, checks their contents and imports accepted documents into managed storage.

### List imported documents

```powershell
uv run docagent list
```

This displays the documents saved in the catalogue, including their IDs and other available details.

### Inspect a document

Copy a document ID from the list command and use it here:

```powershell
uv run docagent inspect YOUR_DOCUMENT_ID
```

Replace `YOUR_DOCUMENT_ID` with an actual document ID.

The inspect command displays document details and a preview of its extracted content.

### Display module help

```powershell
uv run python -m document_agent --help
```

## 6. Running the tests and code checks

Run the automated tests:

```powershell
uv run python -m pytest -v
```

Check code quality using Ruff:

```powershell
uv run python -m ruff check .
```

Check type annotations using mypy:

```powershell
uv run python -m mypy src
```

### Verified results

The final checks completed successfully:

- **pytest:** 21 passed, 2 skipped.
- **Ruff:** All checks passed.
- **mypy:** No issues found in 8 source files.

The two skipped tests were related to symbolic-link testing in the Windows environment.

## 7. Python exercises

The `exercises/` folder contains separate practice programs for the Python concepts covered in the assignment.

For the exercise list and commands, see [`exercises/README.md`](exercises/README.md).

Run an exercise from the project root, for example:

```powershell
uv run python exercises/python_fundamentals.py
```

## 8. Sample documents

The `samples/input/` folder contains documents used to test the application.

The samples include:

- Text and Markdown files.
- A CSV file containing duplicate data and missing values.
- Selectable-text PDF files.
- An image-only PDF.
- A PNG image used to test unsupported file handling.

The `samples/manifest.csv` file records each sample's filename, source, acquisition date and SHA-256 hash.

## 9. Known limitations

- OCR is not implemented.
- Image files such as PNG, JPG and JPEG are unsupported.
- PDFs without extractable text cannot be imported.
- The application is designed as a local command-line document library; it is not a web application.

## 10. Assignment documentation

The assignment work log is maintained in [`docs/assignment-notes.md`](docs/assignment-notes.md).

It records the development environment, application design, testing results, exercise observations, debugging experience and lessons learned.
