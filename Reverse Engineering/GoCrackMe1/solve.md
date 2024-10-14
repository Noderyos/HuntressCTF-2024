# GoCrackMe1

## Solver : `Noderyos`

After decompiling `main.main` i saw a string then a XOR, without more thinking, I tried XORed them in Python 
```py
print(''.join(chr(i^0x56) for i in b"0:71-44coc``3dg0cc3c`nf2cno0e24435f0n+"))
```

## Flag : `flag{bb59566e21f55e5680d589f3dbbec0f8}`
