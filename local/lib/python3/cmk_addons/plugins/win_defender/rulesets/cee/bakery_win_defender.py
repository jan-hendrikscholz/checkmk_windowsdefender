#!/usr/bin/env python3
from collections.abc import Mapping

from cmk.rulesets.v1 import Help, Title
from cmk.rulesets.v1.form_specs import (
    DefaultValue,
    DictElement,
    Dictionary,
    SingleChoice,
    SingleChoiceElement,
)
from cmk.rulesets.v1.rule_specs import AgentConfig, Topic


def _migrate(value: object) -> Mapping[str, object]:
    match value:
        case None:
            return {"deployment": "do_not_deploy"}
        case True:
            return {"deployment": "deploy"}
        case dict():
            return value
        case _:
            raise ValueError(value)


def _parameter_form() -> Dictionary:
    return Dictionary(
        migrate=_migrate,
        elements={
            "deployment": DictElement(
                required=True,
                parameter_form=SingleChoice(
                    title=Title("Deployment"),
                    help_text=Help(
                        "This will deploy the agent plugin <tt>win_defender</tt> for getting Windows Defender data."
                    ),
                    elements=[
                        SingleChoiceElement(
                            name="deploy", title=Title("Deploy Windows Defender plugin")
                        ),
                        SingleChoiceElement(
                            name="do_not_deploy",
                            title=Title("Do not deploy Windows Defender plugin"),
                        ),
                    ],
                    prefill=DefaultValue("deploy"),
                ),
            )
        },
    )


rule_spec_agent_config_win_defender = AgentConfig(
    name="win_defender",
    title=Title("Windows Defender"),
    topic=Topic.APPLICATIONS,
    parameter_form=_parameter_form,
)
