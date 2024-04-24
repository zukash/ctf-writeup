import numpy as np
from PIL import Image

# 画像サンプルのリストを取得
image_files = [f"./flag/{i}.png" for i in range(400)]

# 画像データを格納する配列を初期化（最初の画像からサイズを取得）
image_data = np.array(Image.open(image_files[0]).convert("L"))

# すべての画像のピクセル値の合計を格納する配列を初期化
summed_image_data = np.zeros_like(image_data, dtype=np.float64)

# すべての画像のピクセル値を合計する
for file in image_files:
    img = Image.open(file).convert("L")
    summed_image_data += np.array(img)

# 平均ピクセル値を計算（画像数で合計を割る）
mean_image_data = summed_image_data / len(image_files)

# 平均データをuint8型にキャストして画像として保存
mean_image = Image.fromarray(mean_image_data.clip(0, 255).astype(np.uint8))
mean_image.save("restored_image.png")

# 復元された画像を表示
mean_image.show()
