#!/usr/bin/env python3

from pwn import *

# Connect to the challenge
# r = remote('host', port)  # Replace with actual host/port
# r = process(["python3", "chal.py"])
r = remote("35.200.10.230", 12343)
# context.log_level = "debug"  # Suppress output for clarity

for stage in range(100):
    print(f"Stage {stage + 1}")

    # For each of the 2000 iterations in this stage
    for i in range(2000):
        # Choose a modulus that biases toward digit 1
        # Using 2 * 10^30 makes numbers starting with 1 more likely
        M = 2 * (10**30)

        # r.sendlineafter(b"mod:", str(M).encode())
        r.sendline(str(M).encode())

    # According to Benford's Law, digit 1 should appear most frequently
    # This is especially true with our chosen modulus
    r.sendlineafter(b"most? :", b"1")
    # r.sendline(b"1")


r.interactive()
