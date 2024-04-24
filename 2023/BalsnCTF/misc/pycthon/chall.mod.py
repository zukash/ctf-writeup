#!/usr/bin/python3 -u
with open('./flag') as f:
    flag = f.read()
payload = input(">>> ")
set_dirty(flag)
sandbox()
eval(payload)