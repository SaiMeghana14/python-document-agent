from pathlib import Path

from document_agent.catalogue import CATALOGUE_PATH, load_catalogue, save_document
from document_agent.models import create_document
from document_agent.readers import NoExtractableTextError, read_document
from document_agent.storage import STORAGE_DIR, calculate_hash, copy_to_storage

SUPPORTED_EXTENSIONS = {".txt", ".md", ".csv", ".pdf"}


def import_folder(
    folder: str | Path,
    catalogue_path: Path | None = None,
    storage_dir: Path | None = None,
) -> dict[str, int]:
    """Import supported files from a folder. One bad file does not stop the batch."""
    input_folder = Path(folder).resolve()
    if not input_folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder}")
    if not input_folder.is_dir():
        raise NotADirectoryError(f"Not a folder: {folder}")

    active_catalogue = catalogue_path or CATALOGUE_PATH
    active_storage = storage_dir or STORAGE_DIR
    records = load_catalogue(active_catalogue)
    known_hashes = {record.get("sha256") for record in records}
    counts = {"imported": 0, "duplicates": 0, "unsupported": 0, "failed": 0}

    for candidate in sorted(input_folder.rglob("*")):
        if candidate.is_symlink():
            resolved_candidate = candidate.resolve()
            if not resolved_candidate.is_relative_to(input_folder):
                print(f"Skipped unsafe path: {candidate}")
                counts["failed"] += 1
                continue

        if not candidate.is_file():
            continue

        resolved_path = candidate.resolve()
        if not resolved_path.is_relative_to(input_folder):
            print(f"Skipped unsafe path: {candidate}")
            counts["failed"] += 1
            continue

        if candidate.suffix.lower() not in SUPPORTED_EXTENSIONS:
            message = "Image format not supported" if candidate.suffix.lower() in {".png", ".jpg", ".jpeg"} else "Unsupported file"
            print(f"{message}: {candidate.name}")
            counts["unsupported"] += 1
            continue

        try:
            read_result = read_document(resolved_path)
            file_hash = calculate_hash(resolved_path)
            if file_hash in known_hashes:
                print(f"Duplicate skipped: {candidate.name}")
                counts["duplicates"] += 1
                continue

            stored_path = copy_to_storage(resolved_path, file_hash, active_storage)
            document = create_document(
                name=candidate.name,
                file_type=candidate.suffix.lower().lstrip("."),
                file_hash=file_hash,
                size=resolved_path.stat().st_size,
                stored_path=str(stored_path),
                page_count=read_result.page_count,
            )
            save_document(document, active_catalogue)
            known_hashes.add(file_hash)
            counts["imported"] += 1
            print(f"Imported: {candidate.name}")
        except NoExtractableTextError as error:
            print(f"Skipped {candidate.name}: {error}")
            counts["unsupported"] += 1
        except Exception as error:  # noqa: BLE001
            # Continue importing even if one individual file fails.
            print(f"Failed to import {candidate.name}: {error}")
            counts["failed"] += 1

    print("\nImport summary")
    for label, count in counts.items():
        print(f"{label.capitalize()}: {count}")
    return counts
