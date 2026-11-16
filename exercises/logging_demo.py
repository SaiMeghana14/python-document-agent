"""A small example of INFO, WARNING and ERROR logging."""

import logging

logger = logging.getLogger(__name__)


def import_message(file_name: str) -> str:
    logger.info("Starting import for %s", file_name)
    if not file_name:
        logger.warning("An empty file name was provided")
        return "Skipped"

    try:
        if file_name.endswith(".bad"):
            raise ValueError("This is a sample reader error")
    except ValueError:
        logger.exception("Could not import %s", file_name)
        return "Failed"

    logger.info("Finished import for %s", file_name)
    return "Imported"


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    print(import_message("meeting_notes.md"))
    print(import_message(""))
    print(import_message("broken.bad"))


if __name__ == "__main__":
    main()
