#!/usr/bin/env python3
from Crypto.Util.number import *
from shlex import quote
import subprocess, sys, signal


class RSA:
    def __init__(self, size):
        self.p = getPrime(size // 2)
        self.q = getPrime(size // 2)
        self.n = self.p * self.q
        self.e = getPrime(size // 2)
        self.d = pow(self.e, -1, (self.p - 1) * (self.q - 1))

    def sign(self, msg: bytes) -> int:
        m = bytes_to_long(msg)
        return pow(m, self.d, self.n)

    def verify(self, msg: bytes, sig: int) -> bool:
        return self.sign(msg) == sig


if __name__ == "__main__":
    rsa = RSA(512)
    print(rsa.d.bit_length())
    print(rsa.e.bit_length())
    print(rsa.p.bit_length())
    print(rsa.q.bit_length())
    print(rsa.n.bit_length())
    # a = b"dummy"
    # b = b"flag"
    # ab = a + b

    # ma, mb, mab = map(bytes_to_long, [a, b, ab])
    # sa, sb, sab = map(rsa.sign, [a, b, ab])

    # n = rsa.n
    # a_ = long_to_bytes(mab - mb)
    # sa_ = rsa.sign(a_)
    # assert sab == (sa_ * sb) % n
    # print(sa)
    # print(sb)
    # print(sab)

    # rsa = RSA(512)
    # while True:
    #     print("1. Sign an echo command")
    #     print("2. Execute a signed command")
    #     print("3. Exit")
    #     choice = int(input("> "))
    #     if choice == 1:
    #         msg = input("Enter message: ")
    #         cmd = f"echo {quote(msg)}"
    #         sig = rsa.sign(cmd.encode())
    #         print("Command:", cmd)
    #         print("Signature:", sig)
    #     elif choice == 2:
    #         cmd = input("Enter command: ")
    #         sig = int(input("Enter signature: "))
    #         if rsa.verify(cmd.encode(), sig):
    #             subprocess.run(
    #                 cmd,
    #                 shell=True,
    #                 stdin=subprocess.DEVNULL,
    #                 stdout=sys.stdout,
    #                 stderr=sys.stderr,
    #             )
    #         else:
    #             print("Signature verification failed")
    #     elif choice == 3:
    #         break
