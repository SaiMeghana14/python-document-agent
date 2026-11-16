import hashlib
import shutil
from pathlib import Path

from document_agent.catalogue import PROJECT_ROOT

STORAGE_DIR = PROJECT_ROOT / "data" / "storage"


def calculate_hash(file_path: Path) -> str:
    """Return the SHA-256 hash of a file, reading it in small chunks."""
    digest = hashlib.sha256()
    with file_path.open("rb") as file:
        for chunk in iter(lambda: file.read(8192), b""):
            digest.update(chunk)
    return digest.hexdigest()


def copy_to_storage(file_path: Path, file_hash: str, storage_dir: Path | None = None) -> Path:
    """Copy a file into managed storage using its hash in the destination name."""
    destination_dir = storage_dir or STORAGE_DIR
    if destination_dir.is_symlink():
        raise ValueError("Managed storage directory must not be a symlink.")

    destination_dir.mkdir(parents=True, exist_ok=True)
    destination_root = destination_dir.resolve()
    destination = destination_dir / f"{file_hash}_{file_path.name}"

    if not destination.resolve(strict=False).is_relative_to(destination_root):
        raise ValueError("Storage destination is outside the managed storage directory.")

    shutil.copy2(file_path, destination)
    return destination.resolve()
