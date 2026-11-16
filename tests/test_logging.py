import logging

from exercises.logging_demo import import_message


def test_import_message_logs_warning(caplog):
    with caplog.at_level(logging.WARNING):
        result = import_message("")

    assert result == "Skipped"
    assert "An empty file name was provided" in caplog.text


def test_import_message_logs_error_with_traceback(caplog):
    with caplog.at_level(logging.ERROR):
        result = import_message("broken.bad")

    assert result == "Failed"
    assert "Could not import broken.bad" in caplog.text
    assert "ValueError: This is a sample reader error" in caplog.text
