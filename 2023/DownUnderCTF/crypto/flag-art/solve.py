with open("output.txt") as f:
    flag = f.read()

palette = ".=w-o^*"

D = {}
for c in range(256):
    pattern = ""
    for m in [2, 3, 5, 7]:
        pattern += palette[c % m]
    D[pattern] = c

flag = flag.replace(" ", "").replace("\n", "")
flag = [flag[i : i + 4] for i in range(0, len(flag), 4)]
flag = [chr(D[p]) for p in flag]
print("".join(flag))
