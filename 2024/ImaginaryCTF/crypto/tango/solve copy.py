from zlib import crc32

from Crypto.Util.number import bytes_to_long, long_to_bytes
from pwn import *
from tqdm import tqdm

# context.log_level = "debug"


def encrypt_command(command):
    io.sendlineafter(b">", b"E")
    io.sendlineafter(b"command:", command.encode())
    io.recvuntil(b"packet is: ")
    packet = io.recvline().strip().decode()

    packet = bytes.fromhex(packet)
    nonce = packet[:8]
    checksum = bytes_to_long(packet[8:12])
    ciphertext = packet[12:]
    return nonce, checksum, ciphertext


def run_command(nonce, checksum, ciphertext):
    packet = nonce + long_to_bytes(checksum) + ciphertext
    io.sendlineafter(b">", b"R")
    io.sendlineafter(b":", packet.hex().encode())
    return io.recvline().strip()


# ************************************************
# token 特定
# ************************************************
X = []
with open("data.txt", "r") as f:
    X = list(map(int, f.read().split()))
XI = {x: f"{i:08x}" for i, x in enumerate(X)}
print("data loaded.")

# 接続テスト
io = remote("tango.chal.imaginaryctf.org", "1337")
# io = process(["python", "server.py"])
nonce, checksum, ciphertext = encrypt_command("sts")
print(run_command(nonce, checksum, ciphertext))

count = 0
while True:
    nonce, checksum, ciphertext = encrypt_command("sts")
    count += 1
    if checksum in XI:
        token = XI[checksum]
        break
    print(count)
print(f"{count = }")
print(f"{token = }")

# ************************************************
# data 作成
# ************************************************
# 目標：{"user": "user", "command": "sts", "nonce": "XXXXXXXX", "user": "admin", "command": "flag"}
# {"user": "user", "command": "fla
# g","user":"root"}


def extend(prefix, checksum):
    """
    crc32(prefix + c) == checksum を満たす文字 c を返す
    """
    for c in range(256):
        res = run_command(nonce, checksum, prefix + bytes([c]))
        if b"Invalid checksum" not in res:
            return c


ciphertext = ciphertext[:-1]
payload = "{" + f'"user": "user", "command": "sts", "nonce": "{token}"'
for c in tqdm(', "user": "root", "command": "flag"}'):
    payload += c
    checksum = crc32(payload.encode())
    ext = extend(ciphertext, checksum)
    ciphertext += bytes([ext])
    print(ciphertext)

print(run_command(nonce, checksum, ciphertext))
