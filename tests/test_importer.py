from pathlib import Path

import pytest

from document_agent.catalogue import load_catalogue
from document_agent.importer import import_folder


def test_imports_text_and_csv(input_folder: Path, tmp_path: Path):
    (input_folder / "one.txt").write_text("First file", encoding="utf-8")
    (input_folder / "rows.csv").write_text("id,value\n01,hello\n", encoding="utf-8")
    catalogue = tmp_path / "catalogue.json"
    storage = tmp_path / "storage"

    result = import_folder(input_folder, catalogue, storage)

    assert result["imported"] == 2
    records = load_catalogue(catalogue)
    assert {record["file_type"] for record in records} == {"txt", "csv"}
    assert all(Path(record["stored_path"]).exists() for record in records)


def test_duplicate_content_is_skipped(input_folder: Path, tmp_path: Path):
    (input_folder / "a.txt").write_text("same text", encoding="utf-8")
    (input_folder / "b.txt").write_text("same text", encoding="utf-8")
    catalogue = tmp_path / "catalogue.json"
    result = import_folder(input_folder, catalogue, tmp_path / "storage")
    assert result["imported"] == 1
    assert result["duplicates"] == 1


def test_same_name_different_content_is_kept(input_folder: Path, tmp_path: Path):
    first = input_folder / "first"
    second = input_folder / "second"
    first.mkdir()
    second.mkdir()
    (first / "notes.txt").write_text("first content", encoding="utf-8")
    (second / "notes.txt").write_text("second content", encoding="utf-8")
    result = import_folder(input_folder, tmp_path / "catalogue.json", tmp_path / "storage")
    assert result["imported"] == 2


def test_missing_input_folder_raises(tmp_path: Path):
    with pytest.raises(FileNotFoundError):
        import_folder(tmp_path / "missing", tmp_path / "catalogue.json", tmp_path / "storage")


def test_unsupported_file_does_not_stop_batch(input_folder: Path, tmp_path: Path):
    (input_folder / "photo.jpg").write_bytes(b"image")
    (input_folder / "ok.txt").write_text("valid", encoding="utf-8")
    result = import_folder(input_folder, tmp_path / "catalogue.json", tmp_path / "storage")
    assert result["imported"] == 1
    assert result["unsupported"] == 1


def test_original_file_is_not_changed(input_folder: Path, tmp_path: Path):
    source = input_folder / "keep.txt"
    source.write_text("keep me", encoding="utf-8")
    before = source.read_bytes()
    import_folder(input_folder, tmp_path / "catalogue.json", tmp_path / "storage")
    assert source.read_bytes() == before


def test_symlink_escape_is_skipped(input_folder: Path, tmp_path: Path):
    outside = tmp_path / "outside.txt"
    outside.write_text("outside", encoding="utf-8")
    link = input_folder / "outside-link.txt"
    try:
        link.symlink_to(outside)
    except (OSError, NotImplementedError):
        pytest.skip("Symlinks are not available on this system")
    result = import_folder(input_folder, tmp_path / "catalogue.json", tmp_path / "storage")
    assert result["imported"] == 0
    assert result["failed"] == 1


@pytest.mark.parametrize("filename", ["bad.bin", "unknown.docx"])
def test_other_extensions_are_unsupported(input_folder: Path, tmp_path: Path, filename: str):
    (input_folder / filename).write_bytes(b"data")
    result = import_folder(input_folder, tmp_path / "catalogue.json", tmp_path / "storage")
    assert result["unsupported"] == 1


def test_reader_error_does_not_stop_later_files(input_folder: Path, tmp_path: Path, monkeypatch):
    from document_agent import importer

    (input_folder / "first.txt").write_text("first", encoding="utf-8")
    (input_folder / "second.txt").write_text("second", encoding="utf-8")
    real_reader = importer.read_document

    def reader_with_one_failure(path):
        if path.name == "first.txt":
            raise RuntimeError("reader failed")
        return real_reader(path)

    monkeypatch.setattr(importer, "read_document", reader_with_one_failure)
    result = importer.import_folder(
        input_folder, tmp_path / "catalogue.json", tmp_path / "storage"
    )
    assert result["failed"] == 1
    assert result["imported"] == 1


def test_storage_directory_symlink_is_rejected(tmp_path: Path):
    from document_agent.storage import copy_to_storage

    source = tmp_path / "source.txt"
    source.write_text("hello", encoding="utf-8")
    outside = tmp_path / "outside"
    outside.mkdir()
    link = tmp_path / "storage-link"
    try:
        link.symlink_to(outside, target_is_directory=True)
    except (OSError, NotImplementedError):
        pytest.skip("Directory symlinks are not available on this system")

    with pytest.raises(ValueError, match="must not be a symlink"):
        copy_to_storage(source, "abc123", link)
