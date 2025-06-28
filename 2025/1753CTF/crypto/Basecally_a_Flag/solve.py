flag = "1100 1111 1110 1111 1100 1111 1100 1010 1001 1110 1011 1010 1010 1001 1110 1011 1001 1100 1100"
flag = flag.split(" ")
flag = [chr(int(i, 4)) for i in flag]

print("".join(flag))
