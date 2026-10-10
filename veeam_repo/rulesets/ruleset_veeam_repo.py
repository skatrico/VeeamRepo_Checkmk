#!/usr/bin/env python3
# Copyright (C) 2024 Dragosiz ft. Mario Casero mario.casero@dragosiz.es - License: GNU General Public License v2
# Este archivo es parte de la integración con Checkmk para monitorizar los repositorios de Veeam Backup.

from cmk.rulesets.v1 import Title, Help
from cmk.rulesets.v1.form_specs import DefaultValue, DictElement, Dictionary, Float, LevelDirection, SimpleLevels
from cmk.rulesets.v1.rule_specs import CheckParameters, HostAndItemCondition, Topic

def _parameter_valuespec_veeam_repo():
    return Dictionary(
        title = Title("Veeam Repos"),
        help_text = Help("You can set the parameters for veeam_repo services (Local, Scale-out Local, Scale-Out)."),
        elements={
            "veeam_repo_params": DictElement(
                parameter_form = SimpleLevels(
                    title = Title("Explicit percentage for veeam repository"),
                    form_spec_template = Float(),
                    level_direction = LevelDirection.UPPER,
                    prefill_fixed_levels = DefaultValue(value=(80.0, 90.0)),
                ),
                required = True
            ),
        }
    )

rule_spec_veeam_repo = CheckParameters(
    topic = Topic.STORAGE,
    name="veeam_repo",
    title = Title("Veeam repo"),
    parameter_form = _parameter_valuespec_veeam_repo,
    condition = HostAndItemCondition(item_title=Title("Veeam Repo")),
)
