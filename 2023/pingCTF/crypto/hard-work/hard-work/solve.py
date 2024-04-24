from Crypto.Util.number import long_to_bytes
from base64 import b64decode

with open('task.txt') as f:
    file = f.read()
    file = file.replace('20', '\x20')
    file = file.replace('30', '\x30')
    file = file.replace('31', '\x31')
    file = file.replace('34', '\x34')
    file = file.replace('36', '\x36')

    file = file.replace('6 0', '\60')
    file = file.replace('6 1', '\61')
    file = file.replace('4 0', '\40')

    file = file.replace(' ', '')
    
    flag = long_to_bytes(int(file, 2))

flag_base64 = ''
for x in flag.split(b' '):
    flag_base64 += chr(int(x.decode(), 16))

print(b64decode(flag_base64))