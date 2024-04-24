"""
numpy.random.randintはメルセンヌツイスタが使われている
連続して観測すると、次が予測できるらしい
https://hackmd.io/@iPEQy3ZQTr6grRvwKbAWWw/BkYyAvqq_
"""

from pwn import *

io = remote('static-01.heroctf.fr', 9001)

F = set()
for _ in range(100):
    f = io.recvline()
    F.add(f)
    print(f)
    io.sendline()

print(len(F))