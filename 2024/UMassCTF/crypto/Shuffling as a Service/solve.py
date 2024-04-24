from pwn import *
from tqdm import tqdm
import itertools

KEY_LENGTH = 128
context.log_level = "error"


def ith_chr(i):
    res = ""
    for j in range(1, 9):
        v = 1 << ((KEY_LENGTH * 8) - i * 8 - j)
        io.sendlineafter(b":", f"{v:0{KEY_LENGTH * 2}x}".encode())
        w = int(io.recvline(), 16)
        res += "1" if flag_shuffled & w else "0"
    return chr(int(res, 2))


def starts_at(i):
    payload = "UMASS{"
    payload = "\x00" * i + payload
    payload = payload + "\x00" * (KEY_LENGTH - len(payload))
    payload = int.from_bytes(payload.encode(), "big")
    io.sendlineafter(b":", f"{payload:0{KEY_LENGTH * 2}x}".encode())
    res = int(io.recvline(), 16)
    return bin(res & flag_shuffled).count("1") == bin(payload).count("1")


count = 0
flag = "UMASS{"
# while flag[-1] != "}":
for _ in tqdm(itertools.count()):
    if flag[-1] == "}":
        break
    # io = process(["python", "saas.py"])
    # io = process(["python", "saas.mod.py"])
    io = remote("shuffling-as-a-service.ctf.umasscybersec.org", 1337)
    io.recvuntil(b": \n")
    flag_shuffled = int(io.recvline(), 16)

    offset = -1
    for i in range(2):
        if starts_at(i):
            offset = i

    if offset == -1:
        io.close()
    else:
        c = ith_chr(len(flag) + offset)
        io.close()
        flag += c
        print(flag)


"""
1it [00:01,  1.12s/it]UMASS{6
118it [02:30,  1.22s/it]UMASS{6H
260it [05:15,  1.08s/it]UMASS{6Hu
263it [05:20,  1.30s/it]UMASS{6Huf
365it [07:20,  1.13s/it]UMASS{6Huff
368it [07:25,  1.45s/it]UMASS{6Huff3
378it [07:38,  1.16s/it]UMASS{6Huff3d
468it [09:22,  1.16s/it]UMASS{6Huff3d_
587it [11:42,  1.16s/it]UMASS{6Huff3d_2
703it [14:06,  1.21s/it]UMASS{6Huff3d_2_
719it [14:27,  1.24s/it]UMASS{6Huff3d_2_b
742it [14:57,  1.27s/it]UMASS{6Huff3d_2_b1
768it [15:32,  1.31s/it]UMASS{6Huff3d_2_b1t
822it [16:39,  1.28s/it]UMASS{6Huff3d_2_b1t5
870it [17:40,  1.23s/it]UMASS{6Huff3d_2_b1t5}
871it [17:42,  1.22s/it]
"""
