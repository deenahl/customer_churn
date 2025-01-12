import logging
import os

def setup_logging(name: str, log_file: str = "app.log", level=logging.INFO):
    """
    Setup and return a logger with a specified name, log file, and level.
    :param name: Name of the logger
    :param log_file: path of log file
    :param level: Logging level (e.g., logging.INFO, logging.DEBUG).
    :return: logging.Logger: Configured logger instance.
    """
    # Create a custom logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create handlers
    console_handler = logging.StreamHandler()  # Logs to console
    file_handler = logging.FileHandler(log_file)  # Logs to a file

    # Create formatters and add them to handlers
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger