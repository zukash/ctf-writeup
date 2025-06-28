from string import printable
from collections import Counter


def split_array(arr, chunk_size):
    return [arr[i : i + chunk_size] for i in range(0, len(arr), chunk_size)]


ct = open("flag.txt", "rb").read()
print(ct)
ct = [bin(c)[2:] for c in ct if chr(c) not in printable]
print(ct)
ct = ["".join(c) for c in split_array(ct, 3)]

print(ct)
print(Counter(ct))

# ct = split_array(ct, 8)
# print(ct)
# print(len(ct))


# ct = ["".join(c) for c in ct]
# ct = [int(c[:96], 2) ^ int(c[96:], 2) for c in ct]

# ct = [int(c[96:], 2) for c in ct]
# print(*[f"{int(c):096b}" for c in ct], sep="\n")


