#################################################################
## Windows Defender
##################################################################
## Created By: Kevin Tijssen
## Last updated by: Jan-Hendrik Scholz
##################################################################
$ErrorActionPreference = "SilentlyContinue"
$DefenderData= Get-MpComputerStatus
$RTP = $DefenderData.RealTimeProtectionEnabled
$AS_Age = $DefenderData.AntispywareSignatureAge
$AV_Age = $DefenderData.AntivirusSignatureAge
$AM_ProductVersion = $DefenderData.AMProductVersion
$AM_EngineVersion = $DefenderData.AMEngineVersion
if ($null -ne $DefenderData){
        Write-Host "<<<win_defender:sep(9)>>>"
        Write-Host $RTP`t$AS_Age`t$AV_Age`t$AM_ProductVersion`t$AM_EngineVersion
    }
