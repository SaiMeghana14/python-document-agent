import logging


def test_warning_is_written_to_caplog(caplog):
    logger = logging.getLogger("document_agent.test")
    with caplog.at_level(logging.WARNING):
        logger.warning("Could not read sample file")
    assert "Could not read sample file" in caplog.text
