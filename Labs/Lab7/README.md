PS WindowsUpdate
======

# This is a brief explanation of how to install and use the PSWindowsUpdate module in Powershell.

To install PSWindowsUpdate, simply open a Powershell window and enter the following command:

    Install-Module -Name PSWindowsUpdate

Once it has been installed, run the following command to check and make sure it installed correctly:

    Get-Package -Name PSWindowsUpdate

To use the commands found in PSWindowsUpdate, you need to be running Powershell as administrator. If you want to use the commands in scripts, the scripts will need administrator privileges. I added this code block to the top of my scripts to make sure they are running as admin: (sourced from https://superuser.com/questions/108207/how-to-run-a-powershell-script-as-administrator)

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

To see all available Windows Updates, use:

    Get-WindowsUpdate

To install all available Windows Updates, use:

    Install-WindowsUpdate -MicrosoftUpdate -AcceptAll -AutoReboot

The -AutoReboot key will automatically restart your computer to finish the installation process. If that's not something you want to happen, simply remove that key from the command.

To see a list of Windows Updates that have been installed previously, use:

    Get-WUHistory
