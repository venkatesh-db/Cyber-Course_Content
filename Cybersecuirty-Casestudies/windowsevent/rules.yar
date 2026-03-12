rule SuspiciousPowershellCommand {
    meta:
        description = "Detects suspicious PowerShell commands"
    strings:
        $powershell = "powershell.exe"
        $invokeWebRequest = "Invoke-WebRequest"
        $encodedCommand = "-EncodedCommand"
    condition:
        any of them
}