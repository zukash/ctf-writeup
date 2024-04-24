from Crypto.Util.number import getPrime, long_to_bytes
from random import randint
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

c = 10679224623019895601631054771998536756260529273948325554630759072421765456799864192982507795896029677410562119145911633607280183747646763535259438174402091
S = 1
key = hashlib.md5(long_to_bytes(S)).digest()
cipher = AES.new(key, AES.MODE_ECB)
print(cipher.decrypt(long_to_bytes(c)))
# c = int.from_bytes(cipher.encrypt(pad(flag, 16)), "big")
