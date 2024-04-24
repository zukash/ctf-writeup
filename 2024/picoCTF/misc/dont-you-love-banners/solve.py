from pwn import *

io = remote("tethys.picoctf.net", "55424")

io.sendline(b"My_Passw@rd_@1234")
io.sendlineafter(b"?", b"DEFCON")
io.sendlineafter(b"?", b"John Draper")

io.interactive()


"""
$ find / -name "*flag*" 2> /dev/null
/root/flag.txt

$ cat /root/flag.txt
cat: /root/flag.txt: Permission denied
"""
