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
    packet = nonce + long_to_bytes(checksum).rjust(4, b"\x00") + ciphertext
    io.sendline(b"R")
    io.sendline(packet.hex().encode())
    # io.sendlineafter(b">", b"R")
    # io.sendlineafter(b":", packet.hex().encode())
    return io.recvline().strip()


io = remote("tango.chal.imaginaryctf.org", "1337")
# io = process(["python", "server.py"])

# ************************************************
# data 作成
# ************************************************
# {"user": "user", "command": "fla
# g","user":"root"}


def extend(prefix, checksum):
    """
    crc32(prefix + c) == checksum を満たす文字 c を返す
    """
    for c in range(256):
        ciphertext = prefix + bytes([c])
        packet = nonce + long_to_bytes(checksum).rjust(4, b"\x00") + ciphertext
        io.sendline(b"R")
        io.sendline(packet.hex().encode())
    res_all = io.recvrepeat(timeout=5)
    res_all = res_all.split(b"[E]ncrypt a command")
    # print(res_all)
    print(len(res_all))
    for i, res in enumerate(res_all):
        if b"Invalid checksum" not in res:
            print(res)
            return i


prefix = '{"user": "user", "command": "fla'
nonce, checksum, ciphertext = encrypt_command("fla")
ciphertext = ciphertext[: len(prefix)]
payload = prefix

io.clean()

for c in tqdm('g","user":"root"}'):
    payload += c
    checksum = crc32(payload.encode())
    ext = extend(ciphertext, checksum)
    print(ext)
    ciphertext += bytes([ext])
    # print(payload, checksum, ciphertext)

# io.interactive()
print(run_command(nonce, checksum, ciphertext))
