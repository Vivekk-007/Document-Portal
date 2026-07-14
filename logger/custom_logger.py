import logging
from datetime import datetime
from pathlib import Path

from langchain_core.utils import formatter


class CustomLogger:
    def __init__(self, log_dir="logs"):
        """Configure application logging once and write logs at project level."""
        project_root = Path(__file__).resolve().parent.parent
        self.logs_dir = project_root / log_dir
        self.logs_dir.mkdir(parents=True, exist_ok=True)

        log_file = f"{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.log"
        self.log_file_path = self.logs_dir / log_file

    def get_logger(self, name=__name__):
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        logger.propagate = False

        # Avoid adding another handler when this module is re-run in Jupyter.
        if not any(
            isinstance(handler, logging.FileHandler)
            and Path(handler.baseFilename) == self.log_file_path
            for handler in logger.handlers
        ):
            handler = logging.FileHandler(self.log_file_path, encoding="utf-8")
            handler.setFormatter(
                logging.Formatter(
                    "[%(asctime)s] %(levelname)s "
                    "[%(filename)s:%(lineno)d] %(funcName)s() - %(message)s"
                )
            )
            logger.addHandler(handler)
      
        return logger

if __name__ == "__main__":
    custom_logger = CustomLogger()
    logger = custom_logger.get_logger(__name__)
    logger.info("This is an info message.")
