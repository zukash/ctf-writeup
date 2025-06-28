import pickle

n = 77

D = pickle.load(open("D1000.pkl", "rb"))

for i in range(n):
    print(f"============== {i} ==============")
    for c in range(256):
        if c not in D[i]:
            print(c)
    print()
