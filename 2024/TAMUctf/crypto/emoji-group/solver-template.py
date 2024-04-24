from pwn import *

# io = remote("tamuctf.com", 443, ssl=True, sni="emoji-group")
# io.interactive()
gen = "🏐"
flag = "🔋🌄🔋🪤🦙🦐🥌📗🥱🐓🌏🛬📗🍎🌏⛲👟⛲👳🧷🌏🍲📗🪞🧏🐓🌏🥪🛬🌏🥌🦞👳⛲📢"


def sample(k):
    io = remote("tamuctf.com", 443, ssl=True, sni="emoji-group")
    payload = b"".join([chr(i + 1152).encode() for i in range(k)])
    io.sendlineafter(b":", payload)
    io.recvuntil(b"Your cipher text is:")
    return io.recvline().strip().decode()


G = sample(1152)
G = G[1:]

gen = G.index(gen)
flag = [G.index(c) for c in flag]
print(gen)
print(flag)

print(len(G))
print(G[1:])

# S = [c.encode().hex() for c in sample(1200)]
# T = [c.encode().hex() for c in sample(1200)]

# print(len(set(S)))
# print(len(set(T)))
# print(len(set(S) | set(T)))
