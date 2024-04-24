from PIL import Image

# 画像ファイルを開く
image = Image.open("approach.png")  # 画像のファイル名を指定してください

import numpy as np

# Pillow の Image オブジェクトを numpy 配列に変換
M = np.array(image)

# print(M)
# print(M.shape)

h, w, _ = M.shape
print(M.shape)
# di, dj = 1, 4


# for i in range(h - 1):
#     M[i + 1, :-4] = np.clip(M[i + 1, :-4] - M[i, 4:] / 2, 0, 255).astype(np.uint8)

# # print(M[:3, :3])
# # print("++++++++++++++++++++++++++")

# # for i in range(h - 1, -1, -1):

# #     M[i - 1, 1:] += M[i, :-1]

# # print(M[:3, :3])


# image = Image.fromarray(M)
# image.save("output_image.png")
