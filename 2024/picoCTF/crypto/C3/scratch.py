import sys

chars = "axyz"

lookup1 = '\n "#()*+/1:=[]abcdefghijklmnopqrstuvwxyz'
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

out = ""

prev = 0
for char in chars:
    cur = lookup1.index(char)
    out += lookup2[(cur - prev) % 40]
    prev = cur

out = "DLSeGAGDgBNJDQJDCFSFnRBIDjgHoDFCFtHDgJpiHtGDmMAQFnRBJKkBAsTMrsPSDDnEFCFtIbEDtDCIbFCFtHTJDKerFldbFObFCFtLBFkBAAAPFnRBJGEkerFlcPgKkImHnIlATJDKbTbFOkdNnsgbnJRMFnRBNAFkBAAAbrcbTKAkOgFpOgFpOpkBAAAAAAAiClFGIPFnRBaKliCgClFGtIBAAAAAAAOgGEkImHnIl"

pt = ""
cur = 0
for char in out:
    diff = lookup2.index(char)
    cur += diff
    pt += lookup1[cur % 40]

print(pt)
sys.stdout.write(out)
