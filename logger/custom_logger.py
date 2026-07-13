import logging
import os
from datetime import datetime


class CustomLogger:
    def __init__(self, log_dir="logs"):
        # Create logs directory
        self.logs_dir = os.path.join(os.getcwd(), log_dir)
        os.makedirs(self.logs_dir, exist_ok=True)

        # Log file name
        log_file = f"{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.log"
        log_file_path = os.path.join(self.logs_dir, log_file)

        # Configure logging
        logging.basicConfig(
            filename=log_file_path,
            level=logging.INFO,
            format="[%(asctime)s] %(levelname)s [%(filename)s:%(lineno)d] %(funcName)s() - %(message)s",
        )

    def get_logger(self, name=__name__):
        return logging.getLogger(name)

if __name__ == "__main__":
    custom_logger = CustomLogger()
    logger = custom_logger.get_logger(__name__)
    logger.info("This is an info message.")