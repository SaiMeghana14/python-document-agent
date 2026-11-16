import json

import pytest

from document_agent.catalogue import CatalogueError, load_catalogue


def test_missing_catalogue_returns_empty_list(tmp_path):
    assert load_catalogue(tmp_path / "missing.json") == []

def test_corrupt_catalogue_raises_clear_error(tmp_path):
    path = tmp_path / "catalogue.json"
    path.write_text("{not json", encoding="utf-8")
    with pytest.raises(CatalogueError, match="Could not read catalogue"):
        load_catalogue(path)

def test_catalogue_must_be_a_list(tmp_path):
    path = tmp_path / "catalogue.json"
    path.write_text(json.dumps({"document": "wrong shape"}), encoding="utf-8")
    with pytest.raises(CatalogueError, match="JSON list"):
        load_catalogue(path)

def test_save_failure_is_reported(tmp_path):
    from unittest.mock import patch

    from document_agent.catalogue import save_records

    target = tmp_path / "catalogue.json"
    with (
        patch("document_agent.catalogue.os.replace", side_effect=OSError("disk full")),
        pytest.raises(CatalogueError, match="Could not save catalogue"),
    ):
        save_records([], target)
