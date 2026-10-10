#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2024 Dragosiz ft. Mario Casero mario.casero@dragosiz.es - License: GNU General Public License v2
# Este archivo es parte de la integración con Checkmk para monitorizar los repositorios de Veeam Backup.

from pathlib import Path

from .bakery_api.v1 import (
    FileGenerator,
    OS,
    Plugin,
    register,
)

def get_veeam_repo_files() -> FileGenerator:

    yield Plugin(
        base_os=OS.WINDOWS,
        source=Path('veeam_repo.ps1'),
    )

register.bakery_plugin(
    name="veeam_repo",
    files_function=get_veeam_repo_files,
)
