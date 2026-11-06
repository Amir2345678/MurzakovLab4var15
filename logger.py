import logging
def setup_logger():
    logger = logging.getLogger("ShaftCalculator")
    logger.setLevel(logging.ERROR)
    if not logger.handlers:
        file_handler = logging.FileHandler("input_errors.log", encoding="utf-8")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger
error_logger = setup_logger()
