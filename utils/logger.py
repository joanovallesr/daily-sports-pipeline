import logging
import os

def get_logger(name):

    # Ensure the logs/ directory exists, so file logging works
    os.makedirs("logs", exist_ok=True)

    # Log file path (one file per module)
    log_file = f"logs/{name}.log"

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers when script is reloaded
    if not logger.handlers:
        # 1. File handler (writes timestamped messages to file)
        file_handler = logging.FileHandler(f"logs/{name}.log")
        file_formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        file_handler.setFormatter(file_formatter)

        # 2. Console handler (prints shorter messages to terminal)
        console_handler = logging.StreamHandler()
        console_formatter = logging.Formatter("%(levelname)s - %(message)s")
        console_handler.setFormatter(console_formatter)

        # Attach both handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    
    return logger