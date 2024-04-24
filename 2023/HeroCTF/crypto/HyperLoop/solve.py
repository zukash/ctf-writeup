flag = bytearray(b"Hero{????????????}")
flag_enc = bytearray(b'\x05p\x07MS\xfd4eFPw\xf9}%\x05\x03\x19\xe8')

prefix = bytearray(b"Hero{}")
enc = bytearray()
for i in range(5):
    enc.append(flag_enc[i] ^ prefix[i])
enc.append(flag_enc[-1] ^ prefix[-1])

answer = bytearray()
for i in range(18):
    answer.append(enc[i % 6] ^ flag_enc[i])

print(answer)
