import time
from pwn import *
from collections import defaultdict
from tqdm import trange
import pickle

context.log_level = "ERROR"

# flagの長さ
n = 77
n2 = n * 2
D = [defaultdict(int) for _ in range(n)]

for _ in trange(1000):
    io = remote("crypto.heroctf.fr", 9001)
    m = io.recvregex(rb"time to get sp00(.+)00ky", capture=True)
    flag_xored = bytes.fromhex(m.group(1).decode())
    for i in range(n):
        D[i][flag_xored[i]] += 1
    io.close()
    time.sleep(0.5)

pickle.dump(D, open("D1000.pkl", "wb"))
