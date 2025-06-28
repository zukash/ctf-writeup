# 例：簡単なアセンブリコードをバイトコードに変換
echo -e "section .data\nhello db 'Hello, World!',0\nsection .text\nglobal _start\n_start:\nmov edx,13\nmov ecx,hello\nmov ebx,1\nmov eax,4\nint 0x80\nmov eax,1\nint 0x80" > hello.asm
nasm -f elf32 hello.asm -o hello.o
ld -m elf_i386 hello.o -o hello
objdump -d hello | grep '[0-9a-f]:' | grep -v 'file' | cut -f2 -d: | cut -f1 -d ' ' | tr -d '\n' | sed 's/\(..\)/\\x\1/g'
