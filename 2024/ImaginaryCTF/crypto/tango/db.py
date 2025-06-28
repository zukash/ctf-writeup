from zlib import crc32
from tqdm import trange


with open("data.txt", "w") as f:
    for nonce in trange(3 * 10**7):
        nonce = f"{nonce:08x}"
        data = (
            "{" + f'"user": "user", "command": "sts", "nonce": "{nonce}"' + "}"
        ).encode("ascii")
        checksum = crc32(data)
        f.write(f"{checksum}\n")
