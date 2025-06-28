from Crypto.Util.number import long_to_bytes, bytes_to_long
from cryptography.hazmat.primitives.ciphers.algorithms import AES, SM4
from cryptography.hazmat.primitives.ciphers import Cipher, modes
from tqdm import trange
import os


class Paranoia:
    def __init__(self, keys):
        self.keys = keys

    def __pad(self, data: bytes, bs: int) -> bytes:
        return data + (chr(bs - len(data) % bs) * (bs - len(data) % bs)).encode()

    def __encrypt(self, algorithm, data: bytes, key: bytes):
        cipher = Cipher(algorithm(key), modes.ECB())
        encryptor = cipher.encryptor()
        return encryptor.update(data) + encryptor.finalize()

    def encrypt(self, data: bytes):
        """
        🇨🇳 encryption to protect against the 🇺🇸 backdoor and
        🇺🇸 encryption to protect against the 🇨🇳 backdoor

        I'm a genius !
        """

        data = self.__pad(data, 16)
        data = self.__encrypt(AES, data, self.keys[0])
        data = self.__encrypt(SM4, data, self.keys[1])
        return data


def pad(data: bytes, bs: int) -> bytes:
    return data + (chr(bs - len(data) % bs) * (bs - len(data) % bs)).encode()


def encrypt(algorithm, data: bytes, key: bytes):
    cipher = Cipher(algorithm(key), modes.ECB())
    encryptor = cipher.encryptor()
    return encryptor.update(data) + encryptor.finalize()


def decrypt(algorithm, data: bytes, key: bytes):
    cipher = Cipher(algorithm(key), modes.ECB())
    decryptor = cipher.decryptor()
    return decryptor.update(data) + decryptor.finalize()


flag = b"Hero{I_4m_4_p4r4n01d_g3n1u5}"

keys = [os.urandom(16) for _ in range(2)]
paranoia = Paranoia(keys)

banner = b"I don't trust governments, thankfully I've found smart a way to keep my data secure."
ct_banner = paranoia.encrypt(banner)

# print(keys)

# k0 = keys[0][3:]
# k1 = keys[1][3:]

ct_banner = b"\xd5\xae\x14\x9de\x86\x15\x88\xe0\xdc\xc7\x88{\xcfy\x81\x91\xbaH\xb6\x06\x02\xbey_0\xa5\x8a\xf6\x8b?\x9c\xc9\x92\xac\xdeb=@\x9bI\xeeY\xa0\x8d/o\xfa%)\xfb\xa2j\xd9N\xf7\xfd\xf6\xc2\x0b\xc3\xd2\xfc\te\x99\x9aIG\x01_\xb3\xf4\x0fG\xfb\x9f\xab\\\xe0\xcc\x92\xf5\xaf\xa2\xe6\xb0h\x7f}\x92O\xa6\x04\x92\x88"
k0 = b'C\xb0\xc0f\xf3\xa8\n\xff\x8e\x96g\x03"'
k1 = b"Q\x95\x8b@\xfbf\xba_\x9e\x84\xba\x1a7"

# k0p = bytes_to_long(keys[0][:3])
# k1p = bytes_to_long(keys[1][:3])

# D = {}
# key0 = long_to_bytes(k0p, 3) + k0
# D[encrypt(AES, pad(banner, 16), key0)] = key0
# print(D)

# key1 = long_to_bytes(k1p, 3) + k1
# assert decrypt(SM4, ct_banner, key1) in D

D = {}
for k0p in trange(256**3):
    key0 = long_to_bytes(k0p, 3) + k0
    D[encrypt(AES, pad(banner, 16), key0)] = key0

for k1p in trange(256**3):
    key1 = long_to_bytes(k1p, 3) + k1
    d = decrypt(SM4, ct_banner, key1)
    if d in D:
        print("key0 =", D[d])
        print("key1 =", key1)
        break


# print("pt_banner =", banner)
# print("ct_banner =", paranoia.encrypt(banner))
# print("enc_flag  =", paranoia.encrypt(flag))

# # To comply with cryptography export regulations,
# # 6 bytes = 2**48 bits, should be bruteforce-proof anyway
# for n, k in enumerate(keys):
#     print(f"k{n} = {k[3:]}")
