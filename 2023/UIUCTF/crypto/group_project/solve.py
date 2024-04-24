from Crypto.Util.number import getPrime, long_to_bytes
from random import randint
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

c = 31383420538805400549021388790532797474095834602121474716358265812491198185235485912863164473747446452579209175051706
S = 1
key = hashlib.md5(long_to_bytes(S)).digest()
cipher = AES.new(key, AES.MODE_ECB)
print(cipher.decrypt(long_to_bytes(c)))
# c = int.from_bytes(cipher.encrypt(pad(flag, 16)), "big")
