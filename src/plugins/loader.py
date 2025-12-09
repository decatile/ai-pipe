from typing import Any, cast
from importlib import import_module

from pydantic_settings import BaseSettings

from src.config import ProfileSettings
from src.plugins.pipeline import PluginPipeline
from src.utils.logger import get_logger_by_class
from src.plugins.abc import BasePlugin, AbstractPlugin


class PluginLoader:
    def __init__(self) -> None:
        self.log = get_logger_by_class(PluginLoader)

    def load_plugin(self, name: str, settings: dict[str, Any]) -> AbstractPlugin:
        self.log.info(f'({name}) Loading plugin...')
        module = import_module(name)

        self.log.debug(f'({name}) Verifying classes...')
        assert issubclass(module.Plugin, BasePlugin), 'Should derive from AbstractPlugin'
        assert issubclass(module.Settings, BaseSettings), 'Should derive from BaseSettings'

        self.log.debug(f'({name}) Reading settings...')
        settings = module.Settings(**settings)

        self.log.debug(f'({name}) Instantiating class...')
        plugin = module.Plugin(settings)

        self.log.debug(f'({name}) Successfully initialized!')
        return cast(BasePlugin[BaseSettings], plugin)

    def load_pipeline_for_profile(self, profile: ProfileSettings) -> AbstractPlugin:
        result = []

        for plugin in profile.plugins:
            result.append(self.load_plugin(plugin.name, plugin.config))

        return PluginPipeline(result)
