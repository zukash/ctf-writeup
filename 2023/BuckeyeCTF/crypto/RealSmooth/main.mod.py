from pwn import *
from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes


def encrypt(key, nonce, plaintext):
    chacha = ChaCha20.new(
        key=key,
        nonce=nonce,
    )
    return chacha.encrypt(plaintext)


def main():
    lines = open("passwords.mod.txt", "rb").readlines()
    key = get_random_bytes(32)
    nonce = get_random_bytes(8)
    lines = [x.ljust(18) for x in lines]
    for line in lines:
        ct = encrypt(key, nonce, line)
        print(xor(ct, line))
        print(ct.hex())
        print(line)
    # lines = [encrypt(key, nonce, x).hex().encode() for x in lines]
    # open("database.mod.txt", "wb").writelines(lines)
    open("database.mod.txt", "wb").write(b"\n".join(lines))


def solve():
    pt = "".ljust(18).encode()
    target = "24f2dc11e8510fc249ad48"
    while True:
        key = get_random_bytes(32)
        nonce = get_random_bytes(8)
        ct = encrypt(key, nonce, pt).hex()
        if target in ct:
            print("YES")
            print(key)
            print(nonce)
            exit()


if __name__ == "__main__":
    main()
    # solve()
