import logging

logger = logging.getLogger(__name__)
def import_message(file_name: str) -> str:
    logger.info("Starting import for %s", file_name)
    if not file_name:
        logger.warning("An empty file name was provided")
        return "Skipped"
    logger.info("Finished import for %s", file_name)
    return "Imported"

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    print(import_message("meeting_notes.md"))
    print(import_message(""))
