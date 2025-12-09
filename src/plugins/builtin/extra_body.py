from typing import Any

from pydantic_settings import BaseSettings

from src.plugins.abc import BasePlugin


class Settings(BaseSettings):
    overwrite: bool
    extra: dict[str, Any]


class Plugin(BasePlugin[Settings]):
    def process(self, body: dict[str, Any]) -> dict[str, Any]:
        assert self.settings.overwrite, 'Currently only "overwrite: true" mode supported'
        for k, v in self.settings.extra.items():
            body[k] = v
        return body

#
# Заметьте, что 'Settings' и 'Plugin' - имеют специальное значение в плагинах!
# Они должны экспортировать именно эти имена.
#
