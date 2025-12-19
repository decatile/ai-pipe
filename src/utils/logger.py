import logging.config

from src.config import settings

logging.config.dictConfig(settings.log)
root_logger = logging.getLogger('myaiproxy')


def get_logger(name: str) -> logging.Logger:
    return root_logger.getChild(name)


def get_logger_by_class(cls: type) -> logging.Logger:
    return get_logger(cls.__module__ + '.' + cls.__qualname__)
