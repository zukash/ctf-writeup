from math import e
from pwn import *
from tqdm import trange
import pickle

io = remote('0.cloud.chals.io', '15076')
# io = process(['python3', 'server.py'])

def sample():
    io.sendlineafter(b': ', b'Y')
    return eval(io.recvline())

# sampling
S = []
for _ in trange(250):
    S.append(sample())

# load
try:
    with open('data.pkl', 'rb') as f:
        data = pickle.load(f)
except:
    data = []

print(len(data))

# dump
with open('data.pkl', 'wb') as f:
    data += S
    pickle.dump(data, f)

