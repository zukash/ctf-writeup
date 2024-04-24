"""
Welcome to The Finite State Machine:
=======================RULES===========================
The flag is set as the input string, and the alphabets of the language are set to a-z, {, }, _.
Here, you can define your own states and transitions.
If there is no defined transition for a particular letter, then the machine gets trapped.
It must be a DFA, not an NFA.
An output of 1 means that the string is present in the language; 0 means otherwise.
'@' takes the machine from one state to another by consuming any one letter.
'~l' takes the machine from one state to another by consuming one letter unless the letter is 'l'.
Example: '5 @ 6' takes the machine from state 5 to state 6 for all letters.
Example: '6 ~b 7' takes the machine from state 6 to state 7 for all letters except 'b'.
=================================================
Enter number of states: 10
States from q0 to q9 is created.
The starting state is set to q0.
Enter all the final states seperated by space (e.g., 5 7 9) to set q5,q7,q9 as final states: 9
Enter the number of transitions.: 1
Enter the transitions one at a time
Format: initial_state letter final_state
================================
"""

from pwn import *
from tqdm import tqdm


# *****************************************
# flag 長の特定
# *****************************************
def check_length(n):
    io = remote("dyn.ctf.pearlctf.in", 30018)
    io.sendlineafter(b"number of states:", str(n).encode())
    io.sendlineafter(b"final states:", str(n - 1).encode())
    io.sendlineafter(b"number of transitions.:", str(n - 1).encode())
    for i in range(n - 1):
        io.sendlineafter(b">>>", f"{i} @ {i + 1}".encode())
    return int(io.recvline())


assert check_length(11) == 1


# *****************************************
# flag の特定
# *****************************************
def check_prefix(n, prefix):
    io = remote("dyn.ctf.pearlctf.in", 30018)
    io.sendlineafter(b"number of states:", str(n).encode())
    io.sendlineafter(b"final states:", str(n - 1).encode())
    io.sendlineafter(b"number of transitions.:", str(n - 1 + len(prefix)).encode())
    for i, c in enumerate(prefix):
        io.sendlineafter(b">>>", f"{i} {c} {i + 1}".encode())
        io.sendlineafter(b">>>", f"{i} ~{c} {i}".encode())
        # print(f"{i} {c} {i + 1}")
        # print(f"{i} ~{c} {i}")
    for i in range(len(prefix), n - 1):
        io.sendlineafter(b">>>", f"{i} @ {i + 1}".encode())
        # print(f"{i} @ {i + 1}")
    res = io.recvline()
    io.close()
    return int(res)


# assert check_length(11) == 1
# print(check_prefix(11, "dfa"))
flag = ""
while len(flag) < 11:
    for c in tqdm("abcdefghijklmnopqrstuvwxyz{}_"):
        res = check_prefix(11, flag + c)
        if res == 1:
            flag += c
            print(flag)
            break
# dfa_hacked
