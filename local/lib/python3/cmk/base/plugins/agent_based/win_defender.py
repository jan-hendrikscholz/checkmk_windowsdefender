from .agent_based_api.v1 import *
import pprint


def discover_win_defender(section):
        yield Service(item="Windows Defender")


def check_win_defender(item,section):
        for rtprot_status, as_age, av_age, am_productversion, am_engineversion in section:
                as_age= int((as_age.replace(" ","")),10)
                av_age= int((av_age.replace(" ","")),10)
                age = int(0)
                if as_age > 3:
                        age + 1
                if av_age > 3:
                        age + 1
                if rtprot_status == "False":
                        if age > 0:
                                yield Result(state=State.CRIT, summary="RealTime Protection: Disabled(!!), AV database age:" + av_age + " days(!!), AMProductVersion:" + am_productversion + ", AMEngineVersion:" + am_engineversion)
                                return
                        else:
                                yield Result(state=State.CRIT, summary="RealTime Protection: Disabled(!!), AV database age:" + av_age + " days, AMProductVersion:" + am_productversion + ", AMEngineVersion:" + am_engineversion)
                                return
                else:
                        if age > 0:
                                yield Result(state=State.CRIT, summary="RealTime Protection: Enabled, AV database age: " + av_age + " days(!!), AMProductVersion:" + am_productversion + ", AMEngineVersion:" + am_engineversion)
                                return
                        else:
                                yield Result(state=State.OK, summary="RealTime Protection: Enabled, AV database age:" + av_age + " days, AMProductVersion:" + am_productversion + ", AMEngineVersion:" + am_engineversion)
                                return


register.check_plugin(
    name = "win_defender",
    service_name = "%s",
    discovery_function = discover_win_defender,
    check_function = check_win_defender,
)
