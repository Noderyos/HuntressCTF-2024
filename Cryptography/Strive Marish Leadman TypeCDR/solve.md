# Strive Marish Leadman TypeCDR

## Solver : `Noderyos`

When connecting with netcat we get a value for p,q,d,e,n and a value

variable names looks like RSA cipher, by applying a modular exponent with the value, `d` and `n`, we get the flag

```py
m = pow(value, d, n)
print(m.to_bytes((m.bit_length() + 7) // 8))
```

## Flag : `flag{cf614b15ac1dd461a2e48afdfe21b8e8}`
