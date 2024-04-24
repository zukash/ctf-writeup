from PIL import Image, ImageEnhance

# 画像を読み込む
img = Image.open("./restored_image.png")

# コントラストを上げる
enhancer = ImageEnhance.Contrast(img)
img_enhanced = enhancer.enhance(10.0)  # 2.0はコントラストを上げる強度

# 画像を保存または表示
img_enhanced.save("enhanced_image.png")
img_enhanced.show()
