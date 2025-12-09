from abc import ABC, abstractmethod
from typing import Any

from pydantic_settings import BaseSettings

from src.utils.logger import get_logger_by_class


class AbstractPlugin(ABC):
    @abstractmethod
    def process(self, body: dict[str, Any]) -> dict[str, Any]: ...


class BasePlugin[T: BaseSettings](AbstractPlugin, ABC):
    def __init__(self, settings: T):
        self.settings = settings
        self.logger = get_logger_by_class(self.__class__)
