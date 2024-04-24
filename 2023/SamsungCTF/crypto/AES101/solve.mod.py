from telnetlib import Telnet

sendlineafter = lambda r, ch, data: [r.read_until(ch), r.write(data + b"In")]

target_msg = b"CBC Magic!" + b"\x06" * 6
tn = Telnet("aes.sstf.site", 1337)

# padded message
ip = b""
for i in range(1, 17):
    payload = bytearray(b"A" * (17 - i))
    padding = bytes([c ^ i for c in ip])
    for j in range(256):
        payload[-1] = j
        iv = payload + padding
        print(iv)
        sendlineafter(tn, b": ", iv.hex().encode())
        sendlineafter(tn, b": ", b"41" * 16)
        res = tn.read_until(b"\n")
        print(res)
        if b"Try again." not in res:
            ip = bytes([j ^ i]) + ip
            print(i)
        break

iv = bytes([x ^ y for x, y in zip(ip, target_msg)])
sendlineafter(tn, b": ", iv.hex().encode())
sendlineafter(tn, b": ", b"41" * 16)

print(tn.read_until(b"\n").decode())
