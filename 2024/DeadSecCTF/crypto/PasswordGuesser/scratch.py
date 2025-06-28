from collections import Counter
from Crypto.Util.number import *
from Crypto.Cipher import AES
import hashlib
from Crypto.Util.Padding import pad
import math

flag = b"<REDACTED>"
P = 13**37
password = b"<REDACTED>"
pl = list(password)
pl = sorted(pl)
# assert math.prod(pl) % P == sum(pl) % P
password2 = bytes(pl)

print(password2)
print(Counter(password2))

# print(f"counts = {[cnt for _, cnt in Counter(password2).items()]}")
# cipher = AES.new(hashlib.sha256(password2).digest(), AES.MODE_CBC)
# print(f"c = {cipher.encrypt(pad(flag, 16))}")
# print(f"iv = {cipher.iv}")

# len(counts) == 89

for S in [b"ab", b"aab", b"aaab", b"aaaab"]:
    pl = list(S)
    pl = sorted(pl)
    # assert math.prod(pl) % P == sum(pl) % P
    password2 = bytes(pl)
    print(Counter(password2))



# '''
# c = b'q[\n\x05\xad\x99\x94\xfb\xc1W9\xcb`\x96\xb9|CA\xb8\xb5\xe0v\x93\xff\x85\xaa\xa7\x86\xeas#c'
# iv = b'+\xd5}\xd8\xa7K\x88j\xb5\xf7\x8b\x95)n53'
# '''
