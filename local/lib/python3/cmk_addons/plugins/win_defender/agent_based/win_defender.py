#!/usr/bin/env python3

from cmk.agent_based.v2 import (
    AgentSection,
    CheckPlugin,
    CheckResult,
    DiscoveryResult,
    Result,
    Service,
    State,
    StringTable,
)


def discover_win_defender(section: StringTable) -> DiscoveryResult:
    yield Service(item="Windows Defender")


def check_win_defender(item: str, section: StringTable) -> CheckResult:
    for rtprot_status, as_age, av_age, am_productversion, am_engineversion in section:
        as_age = int((as_age.replace(" ", "")), 10)
        av_age = int((av_age.replace(" ", "")), 10)
        age = 0
        if as_age > 3:
            age + 1
        if av_age > 3:
            age + 1
        if rtprot_status == "False":
            if age > 0:
                yield Result(
                    state=State.CRIT,
                    summary="RealTime Protection: Disabled(!!), AV database age:"
                    + str(av_age)
                    + " days(!!), AMProductVersion:"
                    + am_productversion
                    + ", AMEngineVersion:"
                    + am_engineversion,
                )
                return
            else:
                yield Result(
                    state=State.CRIT,
                    summary="RealTime Protection: Disabled(!!), AV database age:"
                    + str(av_age)
                    + " days, AMProductVersion:"
                    + am_productversion
                    + ", AMEngineVersion:"
                    + am_engineversion,
                )
                return
        elif age > 0:
            yield Result(
                state=State.CRIT,
                summary="RealTime Protection: Enabled, AV database age: "
                + str(av_age)
                + " days(!!), AMProductVersion:"
                + am_productversion
                + ", AMEngineVersion:"
                + am_engineversion,
            )
            return
        else:
            yield Result(
                state=State.OK,
                summary="RealTime Protection: Enabled, AV database age:"
                + str(av_age)
                + " days, AMProductVersion:"
                + am_productversion
                + ", AMEngineVersion:"
                + am_engineversion,
            )
            return


check_plugin_win_defender = CheckPlugin(
    name="win_defender",
    service_name="%s",
    discovery_function=discover_win_defender,
    check_function=check_win_defender,
)


def parse(string_table: StringTable) -> StringTable:
    return string_table


agent_section_win_defender = AgentSection(
    name="win_defender",
    parse_function=parse,
)
