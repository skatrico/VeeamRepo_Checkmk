# Copyright (C) 2024 Dragosiz ft. Mario Casero mario.casero@dragosiz.es - License: GNU General Public License v2
# Este archivo es parte de la integración con Checkmk para monitorizar los repositorios de Veeam Backup.

from cmk.agent_based.v2 import (
    AgentSection,
    CheckPlugin,
    Service,
    Result,
    State,
    Metric,
    check_levels,
    render,
    )

def parsed_veeam_repo(string_table):
    parsed = {}
    for content in string_table:
        if len(content) < 5:
            continue 
        parsed[content[0]] = {
            "size_repo": content[1],
            "used_size": content[2],
            "free_size": content[3],
            "repo_state": content[4]
        }
    return parsed

def discover_veeam_repo_services(section):
        for service_name in section:
            yield Service(item=service_name)

def check_veeam_repo(item, params, section):
    data = section.get(item)
    veeam_repo_params = params["veeam_repo_params"]
    size_repo=float(data['size_repo'])
    free_size=float(data['free_size'])
    used_size=float(data['used_size'])
    repo_state=data["repo_state"]
    percentage_use = (used_size / size_repo) * 100
    
    if repo_state == "False":
        state = State.OK
        summary = f"used percent: {render.percent(percentage_use)} size is {render.bytes(size_repo)}, used: {render.bytes(used_size)}, free: {render.bytes(free_size)}"
        details=f"percent:{render.percent(percentage_use)}\nsize:{render.bytes(size_repo)}\nused:{render.bytes(used_size)}\nfree:{render.bytes(free_size)}"
    else:
        state = State.CRIT
        summary = f"The repository is Unavailable"
        details=f"percent:{render.percent(percentage_use)}\nsize:{render.bytes(size_repo)}\nused:{render.bytes(used_size)}\nfree:{render.bytes(free_size)}"
  
    yield Result(
        state=state,
        summary=summary,
        details=details
        )

    yield from check_levels(
        percentage_use,
        levels_upper = (veeam_repo_params),
        metric_name = "veeam_repo",
        boundaries = (0.0, 100.0),
        )

    yield Metric(name="size_repo", value=size_repo)
    yield Metric(name="used_size", value=used_size)
    yield Metric(name="free_size", value=free_size)

agent_section_veeam_repo = AgentSection(
    name = "veeam_repo",
    parse_function = parsed_veeam_repo,
)

check_plugin_veeam_repo = CheckPlugin(
    name = "veeam_repo",
    service_name = "Veeam Repo %s",
    discovery_function = discover_veeam_repo_services,
    check_function = check_veeam_repo,
    check_default_parameters = {"veeam_repo_params": ("fixed", (80.0, 90.0))},
    check_ruleset_name = "veeam_repo",
)
