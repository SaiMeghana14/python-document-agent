from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from uuid import uuid4


@dataclass
class Document:
    id: str
    original_name: str
    file_type: str
    sha256: str
    size_bytes: int
    stored_path: str
    status: str
    imported_at: str
    page_count: int | None = None


def create_document(
    name: str,
    file_type: str,
    file_hash: str,
    size: int,
    stored_path: str,
    page_count: int | None = None,
) -> Document:
    """Create a document record with a new ID and import timestamp."""
    return Document(
        id=str(uuid4()),
        original_name=name,
        file_type=file_type,
        sha256=file_hash,
        size_bytes=size,
        stored_path=stored_path,
        status="imported",
        imported_at=datetime.now(UTC).isoformat(),
        page_count=page_count,
    )


def document_to_dict(document: Document) -> dict:
    return asdict(document)
