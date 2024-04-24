from PIL import Image

with open("white_RGBA.txt") as f:
    RGBA = f.read().strip().split(",")
    RGBA = list(map(int, RGBA))

R = RGBA[0 : len(RGBA) : 4]
G = RGBA[1 : len(RGBA) : 4]
B = RGBA[2 : len(RGBA) : 4]
A = RGBA[3 : len(RGBA) : 4]

print(R.count(254))
print(G.count(254))
print(B.count(254))
print(A.count(254))

R = [0 if x != 255 else 255 for x in R]
G = [0 if x != 255 else 255 for x in G]
B = [0 if x != 255 else 255 for x in B]
A = [0 if x != 255 else 255 for x in A]

w, h = 512, 512
image = Image.new("RGB", (w, h))
matrix = image.load()

X = []
for i in range(512):
    for j in range(512):
        index = i * 512 + j
        matrix[j, i] = (R[index], G[index], B[index])
        if R[index] == 0 or G[index] == 0 or B[index] == 0:
            X.append((i, j))


print(len(X))
print(X)
# image.save("test.jpg")
