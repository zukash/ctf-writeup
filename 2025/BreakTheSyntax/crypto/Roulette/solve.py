from pwn import *
from hashlib import sha256

io = process(
    [
        "openssl",
        "s_client",
        "-connect",
        "roulette.chal.bts.wh.edu.pl:443",
        "-servername",
        "roulette.chal.bts.wh.edu.pl",
        "-quiet",
    ]
)
# io = process(["python", "server_roulette.py"])

D = {}
for bit in range(1 << 17):
    seed = sha256(bytes(bit)).hexdigest()
    seed_hash = sha256(seed.encode()).hexdigest()
    D[seed_hash] = seed

for _ in range(37):
    io.recvuntil(b"Server seed hash (verify later):")
    server_seed_hash = io.recvline().decode().strip()
    server_seed = D[server_seed_hash]
    print(server_seed)

    client_seed = "0"
    while True:
        combined = f"{server_seed}:{client_seed}"
        game_hash = sha256(combined.encode()).hexdigest()
        hash_int = int(game_hash, 16)
        if hash_int % 37 == 13:
            break
        client_seed = str(int(client_seed) + 1)

    io.sendlineafter(b"(press enter to generate):", client_seed.encode())
    io.sendlineafter(b"(number 0-36 or color red/black/green):", b"13")
io.interactive()
