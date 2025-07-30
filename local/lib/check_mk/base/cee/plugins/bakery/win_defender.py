#!/usr/bin/env python3


from pathlib import Path
from typing import Any, Dict

from .bakery_api.v1 import FileGenerator, OS, Plugin, register


def get_windowsdefender_files(conf: Dict[str, Any]) -> FileGenerator:
    if conf.get("deployment", "do_not_deploy") == "do_not_deploy":
        return
    yield Plugin(base_os=OS.WINDOWS, source=Path("win_defender.ps1"))
    yield Plugin(base_os=OS.LINUX, source=Path("win_defender.py"))


register.bakery_plugin(
    name="win_defender",
    files_function=get_windowsdefender_files,
)
