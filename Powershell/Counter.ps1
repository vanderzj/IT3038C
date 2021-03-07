$Machines = 'vanderzj-win'
$Logfile = "c:\logs\counterdata.log"

Foreach ($machine in $Machines) {
    #$RCounters = Get-Counter -ListSet * -ComputerName $machine
    #"There are {0} counter on {1}" -f $RCounters.count, ($machine)

    $pt = (get-counter -counter "\Processor(_Total)\% Processor Time" -SampleInterval 1 -MaxSamples 10).CounterSamples.CookedValue
    $sample = 1
    foreach ($p in $pt) {
       "Sample {2}: CPU is at {0}% on {1}" -f  [int]$p, $machine, $sample | Out-File -Append $logfile
       $sample++
    }
}