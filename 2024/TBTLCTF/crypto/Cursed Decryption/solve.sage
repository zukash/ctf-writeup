from Crypto.Util.number import *
from pwn import *

io = process(["python", "server.py"])
# io = remote("0.cloud.chals.io", "18312")


def send(payload):
    io.sendlineafter(b":", bin(payload)[2:].encode())
    io.recvuntil(b"Decrypted: ")
    return len(io.recvline().strip())


io.recvuntil(b"N = ")
n = int(io.recvline())
e = 65537
io.recvuntil(b"enc(flag) = ")
enc = int(io.recvline(), 2)

payload = enc
k = send(payload)
print(k)

# *****************************************************************************
# 二分探索でざっくりとした見積もり
# *****************************************************************************
SIZE = 400
ok = 0
ng = 1 << (510 - k)
while ng - ok > 1:
    mid = (ok + ng) // 2
    payload = enc * pow(mid, e, n) % n
    i = send(payload)
    print(mid, i)
    if i <= SIZE:
        ok = mid
    else:
        ng = mid
print(ok)

flag = (1 << SIZE) // ok
print(long_to_bytes(flag))

# *****************************************************************************
# 素因数分解できないか
# *****************************************************************************
# for p in primes(10000):
#     payload = enc * pow(p, -e, n) % n
#     print(p)
#     if send(payload) <= k:
#         print(p, "ok")

# *****************************************************************************
# 存在範囲を絞っていく → ボツ
# *****************************************************************************
# l, r = 0, 1 << 512
# for x in range(1, 500 - k):
#     x = 1 << x
#     payload = enc * pow(x, e, n) % n
#     i = send(payload)
#     print(f"2**{i} < {x} * m < 2**{i+1}")
#     l = max(l, 2**i // x)
#     r = min(r, (2 ** (i + 1) + x - 1) // x)
#     print(l, r)

# *****************************************************************************
# ざっくりとした見積もりを元に mod n で小さい値を作る → ボツ
# *****************************************************************************
# predict = bytes_to_long(
#     b"TBTL{dummy_dummy_rH\xa7\xf4\xdfq\xef\xb8PzK\xed\xdaBE\xb3\x1fr\xb3\xcf\x8d\xd7\xce\t\xb8\x10\x15~\x1f"
# )
# payload = enc * pow(n // predict, e, n) % n
# print(send(payload))

# *****************************************************************************
# n との大小関係を利用
# *****************************************************************************


io.interactive()


# 500
# b"TBTL{1mpl_3rr0r`\xc4'\xfe\xff\x85\x17:q\xe2c\xda\xef\xd4\xc0\xc9\xc2\xcf\xcd\x15\xa9\x85\x05\xcc\xbeD\xb6\xb5\x0e\xd4\x87\x8b"

# 2, 3, 43
