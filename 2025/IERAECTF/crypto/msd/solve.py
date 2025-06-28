#!/usr/bin/env python3

from pwn import *

# context.log_level = "debug"  # Suppress output for clarity
# Connect to the challenge
# r = remote('host', port)  # Replace with actual host/port
# r = process(["python3", "chal.py"])
# nc 34.146.49.83 12345
r = remote("34.146.49.83", 12345)

for stage in range(100):
    print(f"Stage {stage + 1}")

    # Strategy: Use different moduli to force digit 1 to appear most frequently
    # We'll use a mix of moduli that bias toward digit 1

    for i in range(2000):
        # Strategy: Overwhelmingly favor digit 1 by using many small moduli
        # that force the result to be in 1.xxx format

        if i < 1500:
            # Most queries use modulus very close to 10^30
            # This ensures secret % M is almost always 1.xxx * 10^29
            M = 10**30 + (i % 1000) + 1
        else:
            # Some variation to avoid any edge cases
            M = 2 * 10**30 + (i % 100) + 1

        # r.sendlineafter(b"mod:", str(M).encode())
        r.sendline(str(M).encode())

    # Digit 1 should appear most frequently with our strategy
    r.sendlineafter(b"most? :", b"1")
    # r.sendlineafter("1")

r.interactive()
