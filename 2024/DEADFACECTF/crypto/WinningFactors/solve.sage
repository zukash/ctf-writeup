from pwn import *

io = remote("147.182.245.126", "33001")
n = io.recvregex(rb"Calculate the factorial of (\d+)", capture=True).group(1)

print(n)
n = Integer(n)

print(list(factor(n)))

# io.interactive()
