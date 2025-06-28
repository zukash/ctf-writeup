"""
Breakpoint 1, __GI___libc_read (fd=0, buf=0x7ffff7d6b000, nbytes=131072) at ../sysdeps/unix/sysv/linux/read.c:25
(gdb) set {char[9]}0x7ffff7d6b000 = "/bin/sh\x00"
(gdb) set $rdi = 0x7ffff7d6b000
(gdb) set $rip = system
"""
