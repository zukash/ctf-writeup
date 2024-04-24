from pwn import *
import tqdm

context.log_level = "WARN"

flag = b"DUCTF{"
while flag[-1] != b"}":
    for c in tqdm.trange(0x20, 256):
        io = process(["python", "pyny.mod.py"])
        io.sendline(flag + chr(c).encode())
        res = io.recvline()
        io.close()
        if b"Correct!" in res:
            flag += chr(c).encode()
            break
    print(flag)
