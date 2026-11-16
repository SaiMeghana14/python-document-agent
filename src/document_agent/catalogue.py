import json
import os
import tempfile
from pathlib import Path

from document_agent.models import Document, document_to_dict

PROJECT_ROOT = Path(__file__).resolve().parents[2]
CATALOGUE_PATH = PROJECT_ROOT / "data" / "catalogue.json"


class CatalogueError(Exception):
    """Raised when the catalogue cannot be read or written safely."""


def load_catalogue(path: Path | None = None) -> list[dict]:
    catalogue_path = path or CATALOGUE_PATH
    if not catalogue_path.exists():
        return []

    try:
        with catalogue_path.open("r", encoding="utf-8") as file:
            records = json.load(file)
    except (json.JSONDecodeError, OSError) as error:
        raise CatalogueError(f"Could not read catalogue '{catalogue_path}': {error}") from error

    if not isinstance(records, list):
        raise CatalogueError("Catalogue must contain a JSON list of document records.")
    return records


def save_document(document: Document, path: Path | None = None) -> None:
    catalogue_path = path or CATALOGUE_PATH
    records = load_catalogue(catalogue_path)
    records.append(document_to_dict(document))
    save_records(records, catalogue_path)


def save_records(records: list[dict], path: Path | None = None) -> None:
    """Write the catalogue atomically so an interrupted write does not corrupt it."""
    catalogue_path = path or CATALOGUE_PATH
    catalogue_path.parent.mkdir(parents=True, exist_ok=True)
    temporary_name = None

    try:
        with tempfile.NamedTemporaryFile(
            "w", encoding="utf-8", dir=catalogue_path.parent, delete=False
        ) as temporary_file:
            temporary_name = temporary_file.name
            json.dump(records, temporary_file, indent=4)
            temporary_file.write("\n")
        os.replace(temporary_name, catalogue_path)
    except OSError as error:
        if temporary_name and os.path.exists(temporary_name):
            os.unlink(temporary_name)
        raise CatalogueError(f"Could not save catalogue '{catalogue_path}': {error}") from error
