from itertools import combinations
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers import Cipher, modes

def decrypt(ct, key):
    aes = Cipher(AES(key), modes.ECB())
    dec = aes.decryptor()
    pt = dec.update(ct)
    return pt

_ct  = '17c69a812e76d90e455a346c49e22fb6487d9245b3a90af42e67c7b7c3f2823' # 63
_key = 'b5295cd71d2f7cedb377c2ab6cb93' # 29

for i, j, k in combinations(range(len(_key) + 1), 3):
    key = _key
    key = key[:k] + '0' +  key[k:]
    key = key[:j] + '0' +  key[j:]
    key = key[:i] + '0' +  key[i:]
    assert len(key) == 32
    key = bytes.fromhex(key)
    for l in range(len(_ct) + 1):
        ct = _ct
        ct = ct[:l] + '0' + ct[l:]
        assert len(ct) == 64
        ct = bytes.fromhex(ct)
        print(decrypt(ct, key))
