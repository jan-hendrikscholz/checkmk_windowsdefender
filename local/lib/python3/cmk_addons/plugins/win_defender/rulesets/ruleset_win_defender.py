#!/usr/bin/env python3

from cmk.rulesets.v1 import Label, Title
from cmk.rulesets.v1.form_specs import BooleanChoice, DefaultValue, DictElement, Dictionary, Float, LevelDirection, SimpleLevels, Integer
from cmk.rulesets.v1.rule_specs import CheckParameters, Topic, HostCondition

def _parameter_form():
    return Dictionary(
        elements = {
            "av_definition_age": DictElement(
                parameter_form = SimpleLevels(
                    title = Title("Max allowed age for the definition (days)"),
                    form_spec_template = Integer(label=Label("Number of days:")),
                    level_direction = LevelDirection.UPPER,
                    prefill_fixed_levels = DefaultValue(value=(1, 3)),
                ),
                required = False,
            ),
            "ignore_realtime": DictElement(
                parameter_form=BooleanChoice(
                    title=Title("Set to green when realtimecheck is disabled"),
                    label=Label("Do not monitor realtime scan"),
                    prefill=DefaultValue(False),
                ),
                required = True,
            ),
        }
    )



rule_spec_win_defender = CheckParameters(
    name = "win_defender",
    title = Title("Windows Defender Settings"),
    topic = Topic.GENERAL,
    parameter_form = _parameter_form,
    condition=HostCondition(),
)
