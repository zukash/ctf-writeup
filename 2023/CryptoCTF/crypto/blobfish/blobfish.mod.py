#!/usr/bin/env python3

import os
from hashlib import md5
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from PIL import Image
from PIL import ImageDraw
from flag import flag

key = get_random_bytes(8) * 2
iv = md5(key).digest()

cipher = AES.new(key, AES.MODE_CFB, iv=iv)
enc = cipher.encrypt(flag)

img = Image.new("RGB", (800, 50))
drw = ImageDraw.Draw(img)
print(enc.hex())
drw.text((20, 20), enc.hex(), fill=(255, 0, 0))
img.save("flag.mod.png")

hkey = "".join("\\x{:02x}".format(x) for x in key[:10])
print(hkey)

os.system(f'zip -0 flag.mod.zip flag.mod.png -e -P "$(/bin/echo -en "{hkey}")"')
