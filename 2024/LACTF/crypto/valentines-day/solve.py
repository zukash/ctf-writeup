from curses.ascii import isupper
from itertools import cycle

intro = open("intro.txt").read()
text = open("ct.txt").read()

prefix = text[: len(intro)]
print(prefix)
print(intro)

key = []
for a, b in zip(prefix, intro):
    if not a.isalpha():
        continue
    key.append((ord(b) - ord(a)) % 26)


key += [0] * (161 - len(key))
print(key)

cycle_key = cycle(key)

for a in text:
    if not a.isalpha():
        print(a, end="")
        continue
    if a.isupper():
        print(chr((ord(a) - ord("A") + next(cycle_key)) % 26 + ord("A")), end="")
    else:
        print(chr((ord(a) - ord("a") + next(cycle_key)) % 26 + ord("a")), end="")
