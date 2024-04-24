import requests
import re
from randcrack import RandCrack
from tqdm import trange

rc = RandCrack()


def get_random_id():
    url = "https://toorandom-d1c44bdb689b7d08.ctf.pearlctf.in/dashboard"
    res = requests.get(url)
    return re.search(r"Number : (\d+)", res.text).group(1)


S = []
for _ in trange(624):
    rid = int(get_random_id())
    print(rid)
    rc.submit(rid)
    S.append(rid)

while len(S) != 1000000:
    rid = rc.predict_getrandbits(32)
    S.append(rid)

print(f"flag: {S[-1]}")
print(S)
