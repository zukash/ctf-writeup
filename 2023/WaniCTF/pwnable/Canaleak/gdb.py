from pwn import *

io = gdb.debug('./chall', """
    break main
    continue
""")

io.recvline(':')
io.sendline(b'NO')
io.interactive()


# # プロセスを開始する
# bash = process('bash')

# # デバッガーにアタッチする
# gdb.attach(bash, '''
#     set follow-fork-mode child
#     break execve
#     continue
# ''')

# # 対話モードに切り替える
# bash.sendline(b'whoami')
# print(bash.recvline())

# from pwn import *

# context.terminal = 'bash'

# # 新しいプロセスを作りmainで止める
# io = gdb.debug('bash', '''
#     break main
#     continue
# ''')

# # bashにコマンドを送信
# io.sendline(b'echo Hello!')

# # 対話モードに切り替える
# io.interactive()