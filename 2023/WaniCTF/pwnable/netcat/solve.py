from pwn import *

io = remote('netcat-pwn.wanictf.org', 9001)

for _ in range(3):
    problem = io.recvuntil('=')
    print(problem)
    problem = problem.split(b'\n')[-1]
    problem = problem.decode()
    problem = problem.replace('=', '')
    answer = str(eval(problem)).encode()
    print(answer)
    io.sendline(answer)

io.interactive()
print(io.recvrepeat())