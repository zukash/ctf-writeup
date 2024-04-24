---
type: writeup
tags:
---

# Attaaaaack1

## 要約

## 考察

<https://qiita.com/ninja400/items/f3dd1e6eb80fd5b39ba9>
<https://github.com/lasq88/CTF/tree/main/nahamconctf2021/%5Bforensics%5D%20typewriter>

```bash
❯ vol -f memdump.raw windows.filescan | less
0x3deb8aa8      \Windows\System32\notepad.exe   128q

❯ vol -f memdump.raw windows.dumpfiles --physaddr 0x3deb8aa8  
Volatility 3 Framework 2.4.1
Progress:  100.00  PDB scanning finished                        
Cache FileObject FileName Result

DataSectionObject 0x3deb8aa8 notepad.exe file.0x3deb8aa8.0x85fdc538.DataSectionObject.notepad.exe.dat
ImageSectionObject 0x3deb8aa8 notepad.exe file.0x3deb8aa8.0x842624a0.ImageSectionObject.notepad.exe.img
```

## 解法
