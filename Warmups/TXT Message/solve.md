# TXT Message

## Solver : `Noderyos`

If we query TXT record for `ctf.games` with `dig ctf.games TXT` we find this string
```
;; ANSWER SECTION:
ctf.games.		8006	IN	TXT	"146 154 141 147 173 061 064 145 060 067 062 146 067 060 065 144 064 065 070 070 062 064 060 061 144 061 064 061 143 065 066 062 146 144 143 060 142 175"
```

As can be seen, some starts with a `0` and numerals don't go over `7`, so it is probably octal representation
by converting it to ASCCI chars, we get the flag

## Flag : `flag{14e072f705d45882401d141c562fdc0b}`
