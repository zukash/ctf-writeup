from pwn import *

bash = process('bash')
context.terminal

# Attach the debugger
gdb.attach(bash, '''
set follow-fork-mode child
break execve
continue
''')

# Interact with the process
bash.sendline('whoami')