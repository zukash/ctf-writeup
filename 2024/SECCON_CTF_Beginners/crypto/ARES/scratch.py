import os
from Crypto.Cipher import AES

N_BITS = 1024
key = b"A" * 16


def decrypt(c: bytes):
    iv, ct = c[:16], c[16:]
    pt = AES.new(key, AES.MODE_CBC, iv).decrypt(ct)
    return pt


iv = os.urandom(16)
ct = os.urandom(16)
print(decrypt(iv + ct))


print(int.to_bytes(1, N_BITS // 8, "big"))

print(int.from_bytes(b"\x00" * 100 + b"\x01", "big"))
