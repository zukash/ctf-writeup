# 半分全列挙
from tqdm import tqdm
from hashlib import sha256
from itertools import product
from Crypto.Cipher import AES

chars = b"crew_AES*4=$!?"
n = len(chars)
X = []
for S in product(chars, repeat=3):
    X.append(bytes(S))

L = {}
pt = b"AES_AES_AES_AES!"
for w, x in tqdm(list(product(X, repeat=2))):
    k1 = sha256(w).digest()
    k2 = sha256(x).digest()
    ct = AES.new(k2, AES.MODE_ECB).encrypt(AES.new(k1, AES.MODE_ECB).encrypt(pt))
    L[ct] = (w, x)

ct = bytes.fromhex("edb43249be0d7a4620b9b876315eb430")
for y, z in tqdm(list(product(X, repeat=2))):
    k3 = sha256(y).digest()
    k4 = sha256(z).digest()
    pt = AES.new(k3, AES.MODE_ECB).decrypt(AES.new(k4, AES.MODE_ECB).decrypt(ct))
    if pt in L:
        print("Found!")
        w, x = L[pt]
        print(f"{w = }")
        print(f"{x = }")
        print(f"{y = }")
        print(f"{z = }")
        break

key = sha256(w + x + y + z).digest()
enc_flag = bytes.fromhex(
    "e5218894e05e14eb7cc27dc2aeed10245bfa4426489125a55e82a3d81a15d18afd152d6c51a7024f05e15e1527afa84b"
)
flag = AES.new(key, AES.MODE_ECB).decrypt(enc_flag)

print(flag)
