with open("output.mod.txt") as f:
    RR = eval(f.readline().replace("R = ", ""))
    S = eval(f.readline().replace("S = ", ""))

print(len(RR))
print(len(RR[0]))
print(len(S))
