from pwn import *
from base64 import *
from enc import pad
from tqdm import trange


io = process(["python", "secure.py"])
# io = remote("dyn.ctf.pearlctf.in", "30015")


def encode(message):
    io.sendlineafter(b"Enter plaintext:", message)
    return b64decode(io.recvline().strip()).hex()


def check_suffix(suffix):
    """
    flag の末尾が suffix であるか否か
    """
    if len(suffix) < 16:
        enc = encode(pad(suffix) + b"@" * (16 + len(suffix)))
        return enc[:32] == enc[-32:]
    elif len(suffix) == 16:
        enc = encode(suffix)
        return enc[:32] == enc[-32:]
    else:
        enc = encode(pad(suffix) + b"@" * len(suffix))
        return enc[:64] == enc[-64:]


flag = b"}"
while flag[:1] != b"{":
    for c in trange(0x20, 0x7F):
        predict = chr(c).encode() + flag
        if check_suffix(predict):
            flag = predict
            print(flag)
            break
    else:
        assert False

# pearl{n0t_sn34ky_A3S_3ncrypt10n}
