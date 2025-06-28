from pwn import *
from math import factorial

io = remote("147.182.245.126", "33001")

n = io.recvregex(rb"Calculate the factorial of (\d+)\.", capture=True).group(1)
ans = factorial(int(n))
print(n, ans)
io.send(str(ans).encode())

io.interactive()
