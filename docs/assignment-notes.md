# Assignment Notes – Python Foundations and Document Tools

## 1. Assignment information

- **Project:** Python Document Agent
- **Assignment:** Python Foundations and Document Tools
- **Project folder:** `D:\python-document-agent`
- **Development environment:** Windows and PowerShell
- **Python version:** 3.13.3
- **Date of final verification:** 17 November 2026

## 2. Setup

### Tools used

| Tool | Purpose |
|---|---|
| Python 3.13.3 | Running the application and exercises |
| uv | Creating the virtual environment and managing dependencies |
| VS Code / text editor | Writing and editing Python files |
| PowerShell | Running commands |
| Git and GitHub | Version control and project hosting |

### Project setup

The project dependencies were installed using:

```powershell
uv sync
```

This command synchronises the project's virtual environment with the dependencies declared in the project configuration.

### Setup issues and solutions

**Issue 1: Running a pytest command directly through uv**

While running a test with:

```powershell
uv run pytest tests\test_logging.py -v
```

I encountered a Windows error:

```text
error: uv trampoline failed to canonicalize script path
```

I used the Python module form instead:

```powershell
uv run python -m pytest tests/test_logging.py -v
```

The test then completed successfully with 2 passed.

**Issue 2: Ruff detected a leftover debugger breakpoint**

Ruff reported:

```text
T100 Trace found: `breakpoint` used
```

The breakpoint was useful during the debugging exercise, but it should not remain in the final code. I removed the `breakpoint()` line after completing the exercise and ran Ruff again.

**Other setup details:**

- Python version: 3.13.3.
- uv version: [Add the output of `uv --version` if required.]
- Additional setup issue: [Mention any other issue you personally encountered, or write "No other major setup issues."]

## 3. Application design

### Why are the readers separate from the CLI?

The command-line interface and document readers have different responsibilities.

- The CLI accepts user commands such as `import`, `list` and `inspect`.
- The readers handle the extraction of content from supported file formats.
- Keeping these responsibilities separate makes the application easier to understand, test and maintain.

For example, PDF reading logic does not need to be written inside the CLI command itself.

### What is stored in the JSON catalogue?

The JSON catalogue stores information about imported documents so that the application can find them again after restarting.

The document records include information such as:

- Document ID.
- Original filename.
- File type.
- SHA-256 content hash.
- File size.
- Page count where applicable.
- Import status.
- Import timestamp.

The catalogue stores document metadata rather than the full extracted content.

### Where are accepted file copies stored?

Accepted documents are copied into the application's managed storage under:

```text
data/storage/
```

The original files inside `samples/input/` remain unchanged.

The catalogue is stored in:

```text
data/catalogue.json
```

### How does duplicate detection work?

The application calculates a SHA-256 hash from a document's contents.

It compares the calculated hash with hashes already stored in the catalogue.

- If the content has already been imported, the document is skipped as a duplicate.
- If the filename is the same but the content is different, the document is treated as a separate document.

This means duplicate detection is based on file content rather than filename alone.

### How does the application handle unsupported files?

The application checks the file type and uses the appropriate reader.

- TXT and Markdown files are read as text.
- CSV files are validated and read as tabular data.
- Text-based PDFs are processed using pypdf.
- PDFs without extractable text are skipped with a message explaining that OCR may be needed.
- PNG and JPEG images are reported as unsupported.

The importer continues processing other files instead of stopping the entire batch because of one unsupported file.

### How is input path safety handled?

The importer resolves file paths and checks that the files being imported remain inside the selected input folder.

This helps prevent files outside the permitted folder from being imported through unsafe paths or symbolic links.

## 4. Sample documents

The sample documents are stored in:

```text
samples/input/
```

The sample collection includes:

| File | Purpose |
|---|---|
| `company_policy.txt` | Tests importing a text file |
| `meeting_notes.md` | Tests importing a Markdown file |
| `expenses.csv` | Tests CSV reading and data handling |
| `employee_handbook.pdf` | Tests selectable-text PDF reading |
| `invoice_sample.pdf` | Tests another selectable-text PDF |
| `project_report.pdf` | Tests another selectable-text PDF |
| `simulated_scan.pdf` | Tests a PDF without extractable text |
| `boundary_test.png` | Tests unsupported image handling |

### Sample provenance

The sample manifest is stored in:

```text
samples/manifest.csv
```

It records:

- Filename.
- Source or method of creation.
- Acquisition date.
- SHA-256 hash.

The original text and CSV samples were created by me. The additional PDFs were created using Microsoft Word, including a simulated scanned PDF. The PNG test image was created using Microsoft Paint.

The manifest contains the hashes for the sample files. I verified the SHA-256 hash of `meeting_notes.md` against its manifest entry.

## 5. Application testing

The application was tested using the CLI and automated tests.

### Manual testing

The following scenarios were checked:

| Scenario | Observed result |
|---|---|
| Import TXT, Markdown and CSV files | Supported files were imported |
| Import the same files again | Duplicate content was skipped |
| Import a file with the same name but different content | It was treated as a separate document |
| List imported documents | Document records were displayed |
| Inspect an imported document | Document details and content preview were displayed |
| Import selectable-text PDFs | PDF text was extracted and imported |
| Import an image-only PDF | It was skipped with an OCR-needed message |
| Import a PNG image | It was reported as unsupported |
| Import an unsupported file | The importer reported the issue and continued |

Additional boundary and symbolic-link scenarios were investigated. The automated symbolic-link tests were skipped in the Windows environment.

### Automated tests

Command used:

```powershell
uv run python -m pytest -v
```

Final verified result:

```text
21 passed, 2 skipped
```

The skipped tests were related to symbolic-link testing in the Windows environment.

### Ruff

Command used:

```powershell
uv run python -m ruff check .
```

Result:

```text
All checks passed!
```

### mypy

Command used:

```powershell
uv run python -m mypy src
```

Result:

```text
Success: no issues found in 8 source files
```

These checks helped verify that the code passed the automated tests, linting rules and static type checks.

## 6. Python exercises and concepts learned

### Functions and programming fundamentals

I practised writing functions, using parameters and return values, and organising code into smaller reusable parts.
I also worked with lists, dictionaries, sets, mutable objects, shallow copies and deep copies.

### Modules and imports

I learned how to import code from other Python files and why the main guard is useful.
I also studied circular imports, import side effects and module shadowing.

### Classes and object-oriented programming

I practised classes, dataclasses, properties and instance, class and static methods.
These concepts help organise related data and behaviour.

### Exceptions and logging

I learned how to handle exceptions and how logging records application activity at different levels.
I practised INFO, WARNING and ERROR messages and inspected exception tracebacks.

### File handling and standard-library modules

I practised using:

- pathlib for file and directory paths.
- json for structured data.
- csv for reading CSV files.
- re for regular expressions.
- datetime for date and time values.
- Decimal for accurate decimal calculations.
- hashlib for content hashing.
- argparse for command-line arguments.
- logging for application logs.

### Generators and context managers

I learned how generators produce values one at a time.
I also practised context managers, which help manage resources such as open files safely.

### pandas and NumPy

I used pandas to clean and analyse CSV data.

The data exercise demonstrated:

- Removing duplicate rows.
- Preserving employee IDs with leading zeros.
- Identifying missing values.
- Grouping values and calculating totals.
- Using Decimal for monetary calculations.
- Validating joins to prevent unexpected row multiplication.

I also practised NumPy array shapes, data types and broadcasting.

### Lookup benchmark

I compared membership lookup using lists, sets and dictionaries with different collection sizes.
The observed results showed that set and dictionary lookups were generally much faster than list lookups for larger collections. The exact timings depend on the computer.

## 7. Debugger exercise

I created:

```text
exercises/debugger_practice.py
```

The exercise contains an intentional calculation mistake: addition was used instead of multiplication.

During the debugging exercise:

1. I placed a breakpoint in the function.
2. I ran the program using the Python debugger.
3. I inspected the program while execution was paused.
4. I initially tried to inspect `total` before that variable had been assigned.
5. The debugger returned a `NameError` because the assignment line had not executed yet.
6. I stepped to the next line and inspected `total`.
7. The value was `103`, which helped identify that addition had been used instead of multiplication.

The correct operation for calculating a total from price and quantity is multiplication.
After completing the exercise, I removed the breakpoint from the final file so that it would not trigger a Ruff warning.

## 8. Git and GitHub

The project is maintained in a GitHub repository:

https://github.com/SaiMeghana14/python-document-agent

The work was committed and pushed to the `main` branch.

A code and exercise commit was created with the message:

```text
Complete Python foundations and document agent exercises
```

Commit ID at that stage:

```text
59d8c7f
```

## 9. Help and resources used

I used the following resources while learning and completing the assignment:

- Official Python documentation: https://docs.python.org/3/
- uv documentation: https://docs.astral.sh/uv/
- pytest documentation: https://docs.pytest.org/
- pandas documentation: https://pandas.pydata.org/docs/
- NumPy documentation: https://numpy.org/doc/
- pypdf documentation: https://pypdf.readthedocs.io/

I referred to AI tools when I needed help understanding certain concepts and resolving errors during development. I checked the commands and results in my own project environment.

## 10. Final reflection

This assignment helped me understand how Python concepts are used in a practical application.

I learned how to organise a Python project into modules, read different file formats, handle errors, store metadata, detect duplicate content and build command-line functionality.

I also gained practical experience with testing, logging, debugging, data cleaning, Git and GitHub.

One important lesson was that a program should not only work for normal inputs; it should also handle duplicates, unsupported files, invalid data and unexpected errors carefully.
