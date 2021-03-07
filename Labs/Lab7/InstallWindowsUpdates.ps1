# Checks to see if the script is running with elevated privileges. If not, closes and reopens with elevated privileges.
param([switch]$Elevated)

function Test-Admin {
    $currentUser = New-Object Security.Principal.WindowsPrincipal $([Security.Principal.WindowsIdentity]::GetCurrent())
    $currentUser.IsInRole([Security.Principal.WindowsBuiltinRole]::Administrator)
}

if ((Test-Admin) -eq $false)  {
    if ($elevated) {
        # tried to elevate, did not work, aborting
    } else {
        Start-Process powershell.exe -Verb RunAs -ArgumentList ('-noprofile -noexit -file "{0}" -elevated' -f ($myinvocation.MyCommand.Definition))
    }
    exit
}

# Returns a list of available Windows Updates
Get-WindowsUpdate

# Asks the user if they want to install the available Windows Updates. If the user answers yes (y), installs updates and restarts the system.
$Update = Read-Host -Prompt 'Would you like to install these Windows Updates now? This requires a restart. y/n, default n'
if ($Update = 'y'){
    Install-WindowsUpdate -MicrosoftUpdate -AcceptAll -AutoReboot
}
