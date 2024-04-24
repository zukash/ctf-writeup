from itertools import cycle
from pwn import *
import random
from Crypto.Cipher import AES
import time
import os
from flag import flag


class LCG:
    def __init__(self, a, b, m, seed):
        self.a = a
        self.b = b
        self.m = m
        self.state = seed
        self.counter = 0

    def next_state(self):
        ret = self.state
        self.state = (self.a * self.state + self.b) % self.m
        return ret


def is_vulnerable(a):
    """
    周期が短いLCGを生成するパラメータかどうか
    1/16の割合で周期1が見つかる
    """
    m = 288493873028852398739253829029106548736
    b = a % 16
    s = random.randint(1, m - 1)
    lcg = LCG(a, b, m, s)
    S = [lcg.next_state() for _ in range(1000)]
    return len(set(S)) < 100


def get_ciphertext():
    # io = process(["python3", "chall.py"])
    io = remote("challenges1.gcc-ctf.com", "4001")
    io.sendlineafter(b"?", b"49")
    ct = bytes.fromhex(io.recvline().strip().decode())
    io.close()
    return ct


def calc_keystream(ct):
    keystream = xor(ct[:4], b"GCC{")[:3]
    for i in range(0, len(ct), 32):
        left = i + i // 32
        chunk = xor(ct[left : left + 4], b"GCC{")
        keystream += chunk[3:]
    keystream = keystream[:16]
    return keystream


m = 288493873028852398739253829029106548736

while True:
    a = int(time.time())
    if is_vulnerable(a):
        break

ct = get_ciphertext()
ct = ct[33 * 16 * 2 : 33 * 16 * 3]
keystream = calc_keystream(ct)
flag = xor(ct[:32], keystream * 2)
print(flag)

# GCC{pretend_its_a_good_flag_2515}
