# OceanLocust

## Solver : `Noderyos`

After losing 2 days trying to decompile the file, I decided to abandon this idea.

I started by creating a very smol PNG file and give it to the executable with different keys (`AAAAAAA.png` and `AABBCDD.png`) then create a simple parser in python `parse.py`, as can be seen, the actual data remained unchanged, but sections was added (`biTg`, `biTa`, `biTe`).

These sections are 1byte long, and if we sort them, we can see that data changed when key char changed (`#` for `A`, `!` for `C`, `&` for `D`).

If we xor the data with corresponding key letter, we get `98`, or `b` in ASCII.

By applying this key on each section, we get the original flag passed to the file.

But if we apply it on the PNG to decode, we get complete gibberish, and sections are longer, but as we know this is XOR, we can XOR the first section with `flag{` and get the key used to XOR, which appear to be the section name (we found `biTab`, which is section name `biTa`, loop on itself)

after modifying the script `solver.py` to apply this, we get the flag

## Flag : `flag{fec87c690b8ec8d65b8bb10ee7bb65d0}`
