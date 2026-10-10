#!/usr/bin/env python3
# Copyright (C) 2024 Dragosiz ft. Mario Casero mario.casero@dragosiz.es - License: GNU General Public License v2
# Este archivo es parte de la integración con Checkmk para monitorizar los repositorios de Veeam Backup.

from cmk.graphing.v1 import Title
from cmk.graphing.v1.graphs import Graph, MinimalRange
from cmk.graphing.v1.metrics import Color, DecimalNotation, Metric, Unit, SINotation
from cmk.graphing.v1.perfometers import Closed, FocusRange, Perfometer

graph_veeam_repo_combined = Graph(
    name = "veeam_repo_use",
    title = Title("Services in OK state out of total"),
    simple_lines=[ "size_repo"],
    compound_lines=["used_size", "free_size"],
    minimal_range=MinimalRange(0, 100),
)

metric_veeam_repo_percentage_use = Metric(
    name = "percentage_use",
    title = Title("Percentage of use"),
    unit = Unit(DecimalNotation("%")),
    color = Color.PINK,
)

metric_veeam_repo_used_size = Metric(
    name = "used_size",
    title = Title("Used"),
    unit = Unit(SINotation("bytes")),
    color = Color.LIGHT_GREEN,
)

metric_veeam_repo_free_size = Metric(
    name = "free_size",
    title = Title("Free size"),
    unit = Unit(SINotation("bytes")),
    color = Color.LIGHT_GRAY,
)

metric_veeam_repo_size_repo = Metric(
    name = "size_repo",
    title = Title("Size repo"),
    unit = Unit(SINotation("bytes")),
    color = Color.DARK_GREEN,
)

#perfometer_veeam_repo = Perfometer(
#    name = "percentage_use",
#    focus_range = FocusRange(Closed(0), Closed(100)),
#    segments = [ "percentage_use" ],
#)
