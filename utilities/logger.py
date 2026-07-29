# import logging
# import os


# def get_logger(name):
#     log_directory = "logs"

#     if not os.path.exists(log_directory):
#         os.makedirs(log_directory)

#     logger = logging.getLogger(name)

#     if not logger.hasHandlers():
#         logger.setLevel(logging.INFO)

#         file_handler = logging.FileHandler(
#             os.path.join(log_directory, "automation.log"),
#             mode="a",
#             encoding="utf-8"
#         )

#         formatter = logging.Formatter(
#             "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
#         )

#         file_handler.setFormatter(formatter)

#         logger.addHandler(file_handler)

#     return logger


import logging
import os


def get_logger(name):
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # আগের handler remove
    logger.handlers.clear()

    file_handler = logging.FileHandler(
        "logs/automation.log",
        mode="a",
        encoding="utf-8"
    )

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
