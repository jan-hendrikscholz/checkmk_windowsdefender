#!/usr/bin/env python3


from pathlib import Path

from .bakery_api.v1 import FileGenerator, OS, Plugin, register
from typing import Any,Dict

def get_windowsdefender_files(conf: Dict[str, Any]) -> FileGenerator:
    yield Plugin(base_os=OS.WINDOWS,
                 source=Path("win_defender.ps1"))

register.bakery_plugin(
    name="win_defender",
    files_function=get_windowsdefender_files,
)
