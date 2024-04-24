from pwn import *

D = {}

for file in ["c1", "c2", "c3", "p2"]:
    with open(file, "rb") as f:
        D[file] = f.read()

pad = xor(D["p2"], D["c2"])

print(xor(D["c1"], pad))
print(xor(D["c3"], pad))
