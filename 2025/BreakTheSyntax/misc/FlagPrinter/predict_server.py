fLag = "StBCTF{WROOOOONG}"
fLAg = "tSBCTF{I_FORGOR_THE_FLAG_SORRY}"
Flag = "SBtCTF{this_is_a_certified_fake_flag}"
FlAG = "BStCTF{W0NG_FLAG_:3}"
flag = "This CTF is organized by a Polish university, we decided to switch to Polish variable names, so we moved flag to flaga"
flaga = "BtSCTF{***reducted***}"

print("Available flags: fLag, fLAg, Flag, FlAG")
print("Unavailable flags: flag")

while True:
    x = input("-> ")
    if x == "flag":
        print("We are sorry, but this one is currently unavailable")
        continue
    if len(x) != 4:
        print("input length needs to be 4")
        continue
    try:
        eval(f"print({x})")
    except Exception as e:
        print(e)
        continue
