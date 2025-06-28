from pwn import *
from lib import *
import json
from tqdm import tqdm

# context.log_level = "debug"

# io = process(["python", "server.py"])
io = remote("4.246.225.36", 5006)

for beta in tqdm(list(range(field_size))):
    A = 1 * G1
    B = beta * G2
    C = str_to_point("O")

    A_str = point_to_str(A)
    B_str = point_to_str(B)
    C_str = point_to_str(C)

    req = json.dumps({"proof": {"A": A_str, "B": B_str, "C": C_str}})

    io.sendlineafter(b'"}\n', req.encode())
    # io.interactive()
    res = io.recvline()
    print(res)
    if b"Verified" in res:
        break

for _ in range(31):
    io.sendline(req)
io.interactive()
