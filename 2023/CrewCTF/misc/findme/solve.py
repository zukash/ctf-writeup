import hashlib

x, y = 35_6682, 138_5695
flag_hash = "cbb510f471de8b8808890599e9893afa"

SIZE = 100
for dx in range(-SIZE, SIZE):
    for dy in range(-SIZE, SIZE):
        nx, ny = x + dx, y + dy
        message = "crew{" + f"{nx / 10000:.4f},{ny / 10000:.4f}" + "}"
        md5_hash = hashlib.md5(message.encode()).hexdigest()
        if flag_hash == md5_hash:
            print(message)
