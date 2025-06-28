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

    def __decrypt(self, algorithm, data: bytes, key: bytes):
        cipher = Cipher(algorithm(key), modes.ECB())
        decryptor = cipher.decryptor()
        return decryptor.update(data) + decryptor.finalize()

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

    def decrypt(self, data: bytes):
        """
        🇨🇳 decryption to protect against the 🇺🇸 backdoor and
        🇺🇸 decryption to protect against the 🇨🇳 backdoor

        I'm a genius !
        """

        data = self.__decrypt(SM4, data, self.keys[1])
        data = self.__decrypt(AES, data, self.keys[0])
        return data


keys = [os.urandom(16) for _ in range(2)]
paranoia = Paranoia(keys)

banner = b"I don't trust governments, thankfully I've found smart a way to keep my data secure."
ct_banner = paranoia.encrypt(banner)

print(banner)
print(ct_banner)
print(paranoia.decrypt(ct_banner))

enc_flag = b"\xaf\xe0\xb8h=_\xb0\xfbJ0\xe6l\x8c\xf2\xad\x14\xee\xccw\xe9\xff\xaa\xb2\xe9c\xa4\xa0\x95\x81\xb8\x03\x93\x7fg\x00v\xde\xba\xfe\xb92\x04\xed\xc4\xc7\x08\x8c\x96C\x97\x07\x1b\xe8~':\x91\x08\xcf\x9e\x81\x0b\x9b\x15"

key0 = b'If-C\xb0\xc0f\xf3\xa8\n\xff\x8e\x96g\x03"'
key1 = b"\x94\xcb\x92Q\x95\x8b@\xfbf\xba_\x9e\x84\xba\x1a7"
keys = [key0, key1]
paranoia = Paranoia(keys)
print(paranoia.decrypt(enc_flag))
