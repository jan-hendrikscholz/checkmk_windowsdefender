# checkmk_windowsdefender
CheckMK 2.4 plugin to monitor Windows Defender on Windows

This is basically a port of the plugin, created by [@kevintijssen](https://github.com/kevintijssen/check_mk/tree/master/Windows/Defender) to CheckMK 2.4.

# Installation

## For CheckMK Raw Edition users (mkp):
  1. Download the mkp file either from the release section.
  2. Transfer the file to /omd/sites/<YOURSITE>/share/check_mk/optional_packages/ .
  3. Log on as site user `omd su <YOURSITE>` 
  4. Perform the installation via `mkp install ~/share/check_mk/optional_packages/<PACKAGENAME>.mkp`
  
## For CheckMK Enterprise Edition users (mkp):
  1. Download the mkp file either from the release section.
  2. Logon to your instance. Make sure you have permissions to install mkp's.
  3. Navigate to Setup --> Maintenance --> Extension packages
  4. Click on "Upload package" and select the mkp.
  5. Make sure the plugin is enabled, if not, press the green tickmark.
  6. Activate your changes.
  
## Manual installation
  1. Download the individual files, or use `git clone https://github.com/jan-hendrikscholz/checkmk_windowsdefender.git` to bring them to your CheckMK server
  2. Copy all files recursively to `/opt/omd/sites/<YOURSITE>/` . 
  
# Usage
After the installation is done, make sure to deploy the agent plugins to the machines you wish to see Defender data from. Either configure the agent rule to ship the plugin via a baked agent (only available in CEE), or choose another automated/manual way.
Perform a service discovery to see the new service.
