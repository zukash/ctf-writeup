from pwn import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import tqdm

io = remote("aes.sstf.site", "1337")


def xor(X, Y):
    return bytearray([x ^ y for x, y in zip(X, Y)])


def is_valid_padding(iv, msg):
    io.sendlineafter(b"IV(hex):", iv.hex().encode())
    io.sendlineafter(b"CipherText(hex):", msg.hex().encode())
    return b"Try again." not in io.recvline()


# CBC Padding Oracle Attack
# https://onedrive.live.com/embed?resid=F7E83213DDD289C7%212526&authkey=!AFIaXM464rL-CKY&em=2

iv = bytearray(b"A" * 16)
msg = bytearray(b"A" * 16)
for i in range(16)[::-1]:
    padding = bytearray.fromhex("00" * i + f"{16-i:02x}" * (16 - i))
    iv = xor(iv, padding)
    for c in tqdm.trange(256):
        iv[i] = c
        if is_valid_padding(iv, msg):
            padding = bytearray.fromhex("00" * i + f"{16-i:02x}" * (16 - i))
            iv = xor(iv, padding)
            print(iv)
            break

iv = xor(iv, pad(b"CBC Magic!", 16))
io.sendlineafter(b"IV(hex):", iv.hex().encode())
io.sendlineafter(b"CipherText(hex):", msg.hex().encode())
io.interactive()

"""
bytearray(b'\xcb4\xdb\xf0\xa2\xcc\xf5|\x99/&\xa1\x12}\x95k')
 86%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▏                                             | 219/256 [00:31<00:05,  7.06it/s]
[*] Switching to interactive mode
 SCTF{CBC_p4dd1n9_0racle_477ack_5tArts_h3re}
"""
