header = open("header.bmp", "rb")
body = open("enc.bmp", "rb")

with open("new.bmp", "wb") as f:
    f.write(header.read())
    f.write(body.read()[100:])
