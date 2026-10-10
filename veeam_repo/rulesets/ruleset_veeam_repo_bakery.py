#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2024 Dragosiz ft. Mario Casero mario.casero@dragosiz.es - License: GNU General Public License v2
# Este archivo es parte de la integración con Checkmk para monitorizar los repositorios de Veeam Backup.

from cmk.rulesets.v1 import Title, Help
from cmk.rulesets.v1.form_specs import (
    CascadingSingleChoice,
    CascadingSingleChoiceElement,
    DefaultValue,
    DictElement,
    Dictionary,
    FixedValue,
)

from cmk.rulesets.v1.rule_specs import AgentConfig, Topic

def _parameter_valuespec_veeam_repo_bakery():
    return Dictionary(
        title=Title("Agent Plugin Parameters"),
        help_text=Help("This will deploy an agent add-on to check the Veeam Backup & Replication repositories."),
        elements={
            "deployment": DictElement(
                parameter_form=CascadingSingleChoice(
                    title=Title("Deployment"),
                    help_text=Help(
                        "Select <tt>Deploy the plugin</tt> to install the agent plugin "
                        "<tt>veeam_repo.ps1</tt> on the host."
                    ),
                    elements=[
                        CascadingSingleChoiceElement(
                            name="deploy_no",
                            title=Title("Do not deploy the plugin"),
                            parameter_form=FixedValue(value=None),
                        ),
                        CascadingSingleChoiceElement(
                            name="deploy_yes",
                            title=Title("Deploy the plugin"),
                            parameter_form=FixedValue(value=None),
                        ),
                    ],
                    prefill=DefaultValue("deploy_yes"),
                ),
                required=True
            ),
        },
    )

rule_spec_agent_veeam_repo = AgentConfig(
    title=Title("Veeam Repo"),
    topic=Topic.GENERAL,
    name="veeam_repo",
    parameter_form=_parameter_valuespec_veeam_repo_bakery,
)
