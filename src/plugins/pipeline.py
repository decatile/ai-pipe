from src.plugins.abc import AbstractPlugin, PluginContext
from src.utils.logger import get_logger_by_class


class PluginPipeline(AbstractPlugin):
    def __init__(self, plugins: list[AbstractPlugin]):
        self.log = get_logger_by_class(PluginPipeline)
        self.plugins = plugins

    def process(self, ctx: PluginContext) -> PluginContext:
        self.log.info('Processing request...')
        for plugin in self.plugins:
            ctx = plugin.process(ctx)
        self.log.debug('Request successfully processed!')
        return ctx
