import os
import shutil
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def clean_runtime_data():
    """
    Cleans up the data/ directory and other temporary artifacts.
    """
    data_dir = "data"
    if os.path.exists(data_dir):
        logger.info(f"Cleaning data directory: {data_dir}")
        for filename in os.listdir(data_dir):
            file_path = os.path.join(data_dir, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                    logger.info(f"Deleted file: {file_path}")
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                    logger.info(f"Deleted directory: {file_path}")
            except Exception as e:
                logger.error(f"Failed to delete {file_path}. Reason: {e}")
    else:
        logger.info("Data directory does not exist. Nothing to clean.")


if __name__ == "__main__":
    clean_runtime_data()
