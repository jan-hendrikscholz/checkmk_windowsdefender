#!/usr/bin/env python

import subprocess
import shutil
import json
import sys

status = {}
defender = "mdatp"

try:
    assert shutil.which(defender)
except AssertionError:
    sys.exit()

health = [defender, 'health', '--output', 'json' ]
r = subprocess.run(health, capture_output=True, text=True)
output = json.loads(r.stdout)

status['realtime'] = output['realTimeProtectionEnabled']['value']
status['avsignature_age'] = output.get('definitionsUpdatedMinutesAgo')
status['appversion'] = output.get('appVersion')
status['engineVersion'] = output.get('engineVersion')

print(f"<<<win_defender:sep(9)>>>\n{status['realtime']}\t0\t{status['avsignature_age']/1440:.0f}\t{status['appversion']}\t{status['engineVersion']}")