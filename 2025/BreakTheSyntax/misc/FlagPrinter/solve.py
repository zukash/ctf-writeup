from pwn import *

hostname = "flagprinter-d407c9011fe75e1e.chal.bts.wh.edu.pl"
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

# io.sendlineafter(b'->', b'ﬂag ')
# io.sendlineafter(b'->', b'ﬂaga')
io.interactive()
