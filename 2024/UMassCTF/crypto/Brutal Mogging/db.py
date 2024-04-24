from pwn import *
from tqdm import trange

context.log_level = "error"

for _ in trange(300):
    io = remote("brutalmogging.ctf.umasscybersec.org", "1337")
    io.recvuntil(b"The encrypted flag is:")
    enc = io.recvline().strip().decode()
    io.close()
    with open("enc.txt", "a") as f:
        f.write(enc + "\n")
