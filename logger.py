import logging
import os.path


def create_log(name, filename):
    # create log file if needed
    file_exists = os.path.isfile(filename)
    if not file_exists:
        file = open(filename, "x")
        file.close()

    # define logger
    logger = logging.getLogger(name)

    # set log level
    logger.setLevel(logging.DEBUG)

    # define file handler and set formatter
    file_handler = logging.FileHandler(filename)
    formatter = logging.Formatter(
        '%(asctime)s : %(levelname)s : %(name)s : %(message)s')
    file_handler.setFormatter(formatter)

    # add file handler to logger
    logger.addHandler(file_handler)

    return logger
