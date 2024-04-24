from Crypto.Cipher import AES
import math
import os

key = os.urandom(32)
flag = os.environ.get("FLAG", "bctf{fake_flag_fake_flag_fake_flag_fake_flag}")

cipher = AES.new(key, AES.MODE_ECB)


def encrypt(message: str) -> bytes:
    length = math.ceil(len(message) / 16) * 16
    padded = message.encode().ljust(length, b"\0")
    return cipher.encrypt(padded)


# for n in range(60):
#     print(n, encrypt("}" + "\0" * n + flag))

ans = ""
n = 20
while "bctf" not in ans:
    for c in range(20, 128):
        guess = chr(c) + ans
        ct = encrypt(guess + "\0" * 19 + flag)
        if ct[:16] in ct[16:]:
            ans = guess
            print(f"OK: {ans}")
            break
