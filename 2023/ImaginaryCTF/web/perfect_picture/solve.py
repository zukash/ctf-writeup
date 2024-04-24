from PIL import Image
from PIL.ExifTags import TAGS
import piexif
import exiftool


def generate_flag_image():
    # 690x420ピクセルの画像を作成し、すべてのピクセルを(255, 255, 255, 255)（白）で塗りつぶす
    image = Image.new('RGBA', (690, 420), (255, 255, 255, 255))

    # 特定のピクセルの色を設定
    image.putpixel((412, 309), (52, 146, 235, 123))
    image.putpixel((12, 209), (42, 16, 125, 231))
    image.putpixel((264, 143), (122, 136, 25, 213))

    # 画像を保存
    image.save('flag_image.png')

def set_exif_metadata(image_path):
    # exiftoolのインスタンスを作成
    with exiftool.ExifTool() as et:
        # EXIF情報を書き換える
        metadata = {
            "PNG:Description": "jctf{not_the_flag}",
            "PNG:Title": "kool_pic",
            "PNG:Author": "anon"
        }
        args = ["-overwrite_original"]
        for key, value in metadata.items():
            args.append(f"-{key}={value}")
        args.append(image_path)
        et.execute(*args)

    with exiftool.ExifToolHelper() as et:
        metadata = et.get_metadata(image_path)
        print(metadata)

if __name__ == "__main__":
    # generate_flag_image()
    image_path = "flag_image.png"  # EXIF情報を書き換えたい画像のパスを指定
    set_exif_metadata(image_path)
