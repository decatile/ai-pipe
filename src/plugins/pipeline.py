from typing import Any

from src.plugins.abc import AbstractPlugin
from src.utils.logger import get_logger_by_class


class PluginPipeline(AbstractPlugin):
    def __init__(self, plugins: list[AbstractPlugin]):
        self.log = get_logger_by_class(PluginPipeline)
        self.plugins = plugins

    def process(self, body: dict[str, Any]) -> dict[str, Any]:
        self.log.info('Processing request...')
        for plugin in self.plugins:
            body = plugin.process(body)
        self.log.debug('Request successfully processed!')
        return body
