section .data
hello db 'Hello, World!',0
section .text
global _start
_start:
mov edx,13
mov ecx,hello
mov ebx,1
mov eax,4
int 0x80
mov eax,1
int 0x80
