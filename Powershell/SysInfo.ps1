﻿function getIP{
    (Get-NetIPAddress).IPv4Address | Select-String "192*"
}

$IP = getIP

Write-host($IP)