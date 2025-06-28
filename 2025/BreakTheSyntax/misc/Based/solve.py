"""
ascii       | base64
--------------------------
AAA (8 * 3) | BBBB (6 * 4)
AA  (8 * 2) | BBB= (6 * 3)
A   (8 * 1) | BB== (6 * 2)
--------------------------
1 byte を encode する場合は 4 bit (6*2-8*1) 分の自由度がある
"""


def b64char_to_int(c):
    if c.isdigit():
        return ord(c) - ord("0") + 52
    elif c.isalpha():
        if c.islower():
            return ord(c) - ord("a") + 26
        else:
            return ord(c) - ord("A")


from base64 import b64decode, b64encode

top_secret = open("Top_secret").read().splitlines()

message = ""
for secret in top_secret:
    message += b64decode(secret).decode()

true_secret = []
for m in message:
    true_secret.append(b64encode(m.encode()).decode())

assert top_secret != true_secret
assert b64decode("VE==") == b64decode("VA==")

flag = []
for i in range(len(top_secret)):
    if i >= 24:
        # if top_secret[i] != true_secret[i]:
        top = b64char_to_int(top_secret[i][1])
        true = b64char_to_int(true_secret[i][1])
        diff = top ^ true
        flag.append(diff)

for i in range(0, len(flag) - 1, 2):
    c = (flag[i] << 4) + flag[i + 1]
    print(chr(c), end="")
