from pwn import *

io = remote("treasury.squ1rrel-ctf-codelab.kctf.cloud", "1337")
# io = process(["python", "chall.py"])

io.sendlineafter(b">", b"1")
io.sendlineafter(b">", b"A")
io.recvuntil(b"key:")

key = io.recvline().strip().decode()
iv = bytes.fromhex(key.split(":")[0])
nb = bytes.fromhex(key.split(":")[1])
iv = xor(iv, bytes.fromhex("00" + "00" + "09" + "39" * 13))
key = iv.hex() + ":" + nb.hex()

io.sendlineafter(b">", b"0")
io.sendlineafter(b">", key)

io.interactive()
