from pwn import *
from itertools import combinations

# nc 34.132.166.199 11112
io = remote("34.132.166.199", "11112")
# io = process(["python", "squ1rrel-lottery.mod.py"])

L = list(combinations(range(16, 30), 9))

for i in range(40):
    # io.sendline(" ".join(map(str, L[i])))
    io.sendline(b"1 2 3 4 5 6 7 8 61")

io.interactive()

"""
十分条件

どんな 9 個の数字を選んでも 3 個以上の数字が一致する組み合わせが存在する
"""

# 1, 2, ..., 60 の間で 9 個の数字を選ぶ
# どの 9 個の数字を選んでも 3 個以上の数字が一致する組み合わせが存在する
