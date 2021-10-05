#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    DropdownChoice,
)
from cmk.gui.plugins.wato import (
    HostRulespec,
    rulespec_registry,
)

try:
    from cmk.gui.cee.plugins.wato.agent_bakery.rulespecs.utils import (
        RulespecGroupMonitoringAgentsAgentPlugins
    )
except Exception:
    RulespecGroupMonitoringAgentsAgentPlugins = None


def _valuespec_agent_config_win_defender():
    return DropdownChoice(
        title=_('Windows Defender'),
        help=_('This will deploy the agent plugin <tt>win_defender</tt> '
               'for evaluating Windows Defender data.'),
        choices=[
            (True, _('Deploy Windows Defender plugin')),
            (None, _('Do not deploy Windows Defender plugin')),
        ],
    )


if RulespecGroupMonitoringAgentsAgentPlugins is not None:
    rulespec_registry.register(
        HostRulespec(
            group=RulespecGroupMonitoringAgentsAgentPlugins,
            name='agent_config:win_defender',
            valuespec=_valuespec_agent_config_win_defender,
        ))
