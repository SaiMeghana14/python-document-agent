import pytest


@pytest.fixture
def input_folder(tmp_path):
    folder = tmp_path / "input"
    folder.mkdir()
    return folder
