function getIP{
    (Get-NetIPAddress).IPv4Address | Select-String "192*"
}
$IP = getIP
$date = Get-Date -Format "dddd mm/dd/yyyy HH:mm K"
$version = $Host.version.Major
 
$Body = "This machine's IP is $IP. User is $ENV:Username. Hostname is $env:computername. PowerShell version is $version. Today's date is $date"

Write-Host($Body)

#Send-MailMessage -To "vanderzj@uc.mail.edu" -From "zvanderpool99@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $Body -smtpServer smtp.google.com -port 587 -UseSSL -Credential (Get-Credential)