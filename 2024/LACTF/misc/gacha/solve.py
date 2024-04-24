from PIL import Image

# 画像ファイルを開く
fis = Image.open("./chall/fiscl.png")
uwu = Image.open("./chall/uwu.png")
owo = Image.open("./chall/owo.png")


# 画像のサイズが同じであることを確認する
if uwu.size != owo.size:
    print("画像のサイズが一致しません")
    exit()

# 画像のピクセルデータを取得する
pixels1 = uwu.load()
pixels2 = owo.load()

# 新しい画像の作成
new_image = Image.new("RGB", uwu.size)

# XOR演算を実行し、新しい画像にピクセルデータを設定する
for i in range(uwu.size[0]):
    for j in range(uwu.size[1]):
        r1, g1, b1 = pixels1[i, j]
        r2, g2, b2 = pixels2[i, j]
        new_r = r1 ^ r2
        new_g = g1 ^ g2
        new_b = b1 ^ b2
        new_image.putpixel((i, j), (new_r, new_g, new_b))

# 新しい画像を保存する
new_image.save("output.png")
