# Nightmare on Hunt Street

## Solver : `Noderyos`

Firstly, i used [evtx_dump](https://github.com/omerbenamram/evtx) to convert it to xml

# 1

I used a simple grep command with ip address regex `grep -E "([0-9]+\.){3}[0-9]+" *.xml`

## Flag : `10.1.1.42`

# 2

Using `grep "FailureReason" *.xml | wc -l`

## Flag : `32`

# 3



# 4

using `grep "net1 " *.xml`

we get these enumerations commands 
```
Security.xml:    <Data Name="CommandLine">C:\Windows\system32\net1  user</Data>
Security.xml:    <Data Name="CommandLine">C:\Windows\system32\net1  localgroup</Data>
Security.xml:    <Data Name="CommandLine">C:\Windows\system32\net1  share</Data>
```

## Flag : `3`

# 5

same command as number 4
```
Security.xml:    <Data Name="CommandLine">C:\Windows\system32\net1 user susan_admin Susan123! /ADD</Data>
```

## Flag : `Susan123!`
