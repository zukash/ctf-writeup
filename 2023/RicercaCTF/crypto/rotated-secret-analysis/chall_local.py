import os
from Crypto.Util.number import bytes_to_long, getPrime, isPrime

flag = os.environ.get("FLAG", "fakeflag").encode()

while True:
    p = getPrime(32)
    q = (p << 16 | p >> 16) & (
        2**32 - 1
    )  # bitwise rotation (cf. https://en.wikipedia.org/wiki/Bitwise_operation#Rotate)
    if isPrime(q):
        break

n = p * q
e = 0x10001
m = bytes_to_long(flag)

c = pow(m, e, n)

print(f"{n=}")
print(f"{e=}")
print(f"{c=}")

print(f"{p=}")
print(f"{q=}")


print(f"{bin(p)=}")
print(f"{bin(q)=}")

print(f"{bin(p)[2:18]=}")
print(f"{bin(q)[2:18]=}")
