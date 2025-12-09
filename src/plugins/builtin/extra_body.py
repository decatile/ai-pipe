from typing import Any

from pydantic_settings import BaseSettings

from src.plugins.abc import BasePlugin, PluginContext


class Settings(BaseSettings):
    overwrite: bool
    extra: dict[str, Any]


class Plugin(BasePlugin[Settings]):
    def process(self, ctx: PluginContext) -> PluginContext:
        assert self.settings.overwrite, 'Currently only "overwrite: true" mode supported'
        for k, v in self.settings.extra.items():
            ctx.body[k] = v
        return ctx

#
# Заметьте, что 'Settings' и 'Plugin' - имеют специальное значение в плагинах!
# Они должны экспортировать именно эти имена.
#
