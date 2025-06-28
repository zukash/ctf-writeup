from pwn import xor

"""
token = sessionStorage.getItem('token');
response = await fetch('files/8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918/flag.txt', {
                headers: { "x-token": token }
            })
blob = await response.blob()
downloadTag = document.createElement("a");
downloadTag.href = URL.createObjectURL(blob);
downloadTag.download = "flag.enc";    
downloadTag.click();
---
→ flag.enc を取得

zeropad.txt を upload
同様にして、zeropad.enc を取得            
response = await fetch('files/04f8996da763b7a969b1028ee3007569eaf3a635486ddab211d512c85b9df8fb/zeropad.txt', {
                headers: { "x-token": token }
            })
---
あとは xor するだけ
"""


zeropad_plain = b"\x00" * 220

with open("zeropad.txt", "wb") as f:
    f.write(zeropad_plain)

with open("flag.enc", "rb") as f:
    flag_enc = f.read()

with open("zeropad.enc", "rb") as f:
    zeropad_enc = f.read()

flag_plain = xor(flag_enc, zeropad_enc)
print(flag_plain)
