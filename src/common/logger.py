import os
import sys
from logging import getLogger, Formatter, StreamHandler, WARN, INFO, DEBUG, Logger
from logging.handlers import TimedRotatingFileHandler


def get_common_logger(name, log_level="DEBUG", log_file_path=None, std_out=True, when="D", interval=1, backup_count=180) -> Logger:
    """
    create common logger
    :param name:
    :param log_level:
    :param log_file_path:
    :param std_out:
    :param when:
    :param interval:
    :param backup_count:
    :return:
    """
    logger = getLogger(name)
    if log_level == "WARN":
        log_level = WARN
    elif log_level == "INFO":
        log_level = INFO
    else:
        log_level = DEBUG

    formatter = Formatter("%(asctime)s %(levelname)s %(module)s %(lineno)s :%(message)s")
    if log_file_path is not None:
        os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
        handler = TimedRotatingFileHandler(filename=log_file_path, when=when, interval=interval, backupCount=backup_count, encoding="utf-8")
        handler.setLevel(log_level)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        handler.close()
    if std_out:
        handler = StreamHandler(sys.stdout)
        handler.setLevel(log_level)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        handler.close()

    logger.setLevel(log_level)
    logger.propagate = False
    return logger
