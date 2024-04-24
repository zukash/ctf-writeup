from pwn import *
from tqdm import tqdm

context.log_level = 'critical'

def encrypt(message):
    io.recvline()
    io.recvline()
    io.recvline()
    io.recvline()
    io.sendline(b'0')
    io.sendline(message.encode())
    return io.recvline().split()[-1]

encrypted_flag = b"ca6ae6e83d63c90bed34a8be8a0bfd3ded34f25034ec508ae8ec0b7f"
for _ in tqdm(range(1000)):
    io = process('./heaven')
    c = encrypt('ctf4b')
    if c in encrypted_flag:
        break

assert encrypt('ctf4b') in encrypted_flag
flag = 'ctf4b'
while flag[-1] != '}':
    for c in range(0x20, 0x7f):
        predict = flag + chr(c)
        if encrypt(predict) in encrypted_flag:
            flag = predict
            print(flag)
            break
