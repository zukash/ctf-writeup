from pwn import *

X = []
for _ in range(100):
    io = process("./a.out")
    size = io.recvall()
    X.append(int(size))
print(sorted(X))

# 100 個くらい抜き出すと長さが 1 の key が見つかる
