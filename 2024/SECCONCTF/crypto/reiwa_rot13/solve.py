from sage.all import *
from params import *
from itertools import product
from Crypto.Util.number import *
from Crypto.Cipher import AES
import codecs
import string
import random
import hashlib
from tqdm import tqdm


key = "".join(random.sample(string.ascii_lowercase, 10))
# rot13_key = codecs.encode(key, "rot13")
key = key.encode()
# rot13_key = rot13_key.encode()
key_m = bytes_to_long(key)
# rot13_key_m = bytes_to_long(rot13_key)
print(key_m)


def list2int(L):
    return sum([L[~i] * 256**i for i in range(len(L))])


PR = PolynomialRing(Zmod(n), "x")
x = PR.gen()

for D in tqdm(list(product([13, -13], repeat=10))):
    d = list2int(D)
    # print(d)
    f1 = x**e - c1
    f2 = (x + d) ** e - c2
    g = PR(f1._pari_with_name("x").gcd(f2._pari_with_name("x")))
    if g.degree() == 1:
        key = int(-g.monic()[0])
        key = long_to_bytes(key)
        print(key)
        break

key = hashlib.sha256(key).digest()
cipher = AES.new(key, AES.MODE_ECB)
flag = cipher.decrypt(encyprted_flag)
print(flag)
