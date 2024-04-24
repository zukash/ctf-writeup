"""
name: hoge
age: 21
height: 112
awesome: true
"""

"""yaml
person1:
    name: hoge
    age: 21
    height: 112
    awesome: true
person2:

    age: 21
    height: 112
    awesome: true
---
person:
    name: hoge
    age: 11
"""
import hashlib
import datetime


hash = hashlib.md5(
        datetime.datetime.utcnow().strftime("%d/%m/%Y %H:%M").encode()
).hexdigest()

print(hash)