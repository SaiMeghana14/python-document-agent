import csv
from dataclasses import dataclass
from pathlib import Path

from pypdf import PdfReader


class UnsupportedFileError(Exception):
    pass


class NoExtractableTextError(Exception):
    pass


@dataclass
class ReadResult:
    text: str
    page_count: int | None = None
    csv_headers: list[str] | None = None
    csv_rows: list[list[str]] | None = None


def read_text_file(path: Path) -> ReadResult:
    return ReadResult(text=path.read_text(encoding="utf-8-sig"))


def read_csv_file(path: Path) -> ReadResult:
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if not rows or not rows[0] or all(not cell.strip() for cell in rows[0]):
        raise ValueError("CSV file is empty or has no header row.")

    headers = rows[0]
    for line_number, row in enumerate(rows[1:], start=2):
        if len(row) != len(headers):
            raise ValueError(
                f"Malformed CSV at row {line_number}: expected {len(headers)} columns, "
                f"found {len(row)}."
            )

    preview_rows = rows[1:6]
    preview = "\n".join([", ".join(headers)] + [", ".join(row) for row in preview_rows])
    return ReadResult(text=preview, csv_headers=headers, csv_rows=preview_rows)


def read_pdf_file(path: Path) -> ReadResult:
    reader = PdfReader(str(path))
    page_text = [page.extract_text() or "" for page in reader.pages]
    text = "\n\n".join(value.strip() for value in page_text if value.strip())
    if not text.strip():
        raise NoExtractableTextError("No extractable text; OCR may be needed")
    return ReadResult(text=text, page_count=len(reader.pages))


def read_document(path: Path) -> ReadResult:
    extension = path.suffix.lower()
    if extension in {".txt", ".md"}:
        return read_text_file(path)
    if extension == ".csv":
        return read_csv_file(path)
    if extension == ".pdf":
        return read_pdf_file(path)
    if extension in {".png", ".jpg", ".jpeg"}:
        raise UnsupportedFileError("Image files are not supported; OCR is outside this version.")
    raise UnsupportedFileError(f"Unsupported file type: {extension or '(no extension)'}")
