import argparse
from pathlib import Path

from document_agent.catalogue import CATALOGUE_PATH, load_catalogue
from document_agent.importer import import_folder
from document_agent.readers import (
    NoExtractableTextError,
    UnsupportedFileError,
    read_document,
)
from document_agent.storage import STORAGE_DIR


def show_documents(records: list[dict]) -> None:
    if not records:
        print("No documents found. Import a folder first.")
        return

    print(f"{'ID':<36} {'NAME':<28} {'TYPE':<8} {'SIZE':>10}  STATUS")
    print("-" * 100)
    for record in records:
        print(
            f"{record['id']:<36} {record['original_name'][:27]:<28} "
            f"{record['file_type']:<8} {record['size_bytes']:>10}  {record['status']}"
        )

def inspect_document(document_id: str, records: list[dict]) -> None:
    document = next((item for item in records if item.get("id") == document_id), None)
    if document is None:
        print(f"Document not found: {document_id}")
        return

    print("Document details")
    print("-" * 40)
    for field in (
        "id", "original_name", "file_type", "sha256", "size_bytes",
        "page_count", "status", "imported_at", "stored_path",
    ):
        print(f"{field.replace('_', ' ').title()}: {document.get(field)}")

    stored_path = Path(document["stored_path"]).resolve()
    storage_root = STORAGE_DIR.resolve()
    if not stored_path.is_relative_to(storage_root) or not stored_path.is_file():
        print("\nStored document file not found or path is unsafe.")
        return

    print("\nContent preview")
    print("-" * 40)
    try:
        result = read_document(stored_path)
        if result.csv_headers:
            print("CSV headers:", ", ".join(result.csv_headers))
            print("CSV rows:")
        print(result.text[:1000] or "(No preview text)")
        if len(result.text) > 1000:
            print("\nPreview truncated.")
    except (OSError, ValueError, NoExtractableTextError, UnsupportedFileError) as error:
        print(f"Could not preview this document: {error}")

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Import, list and inspect local documents.")
    commands = parser.add_subparsers(dest="command", required=True)

    import_parser = commands.add_parser("import", help="Import documents from a folder")
    import_parser.add_argument("folder", help="Folder containing documents")

    commands.add_parser("list", help="List imported documents")

    inspect_parser = commands.add_parser("inspect", help="Inspect one imported document")
    inspect_parser.add_argument("document_id", help="ID shown by the list command")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    try:
        if args.command == "import":
            import_folder(args.folder)
        elif args.command == "list":
            show_documents(load_catalogue(CATALOGUE_PATH))
        elif args.command == "inspect":
            inspect_document(args.document_id, load_catalogue(CATALOGUE_PATH))
    except (FileNotFoundError, NotADirectoryError, ValueError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
