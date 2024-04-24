---
type: writeup
tags:
---

# Attaaaaack1

## 要約

## 考察

volatility というツールが有名らしい。brewで入れてみた。

```bash
❯ vol -f memdump.raw windows.info
Volatility 3 Framework 2.4.1
Progress:  100.00  PDB scanning finished                                                                                              
Variable Value

Kernel Base 0x82a42000
DTB 0x185000
Symbols file:///opt/homebrew/Cellar/volatility/2.4.1_1/libexec/lib/python3.11/site-packages/volatility3/symbols/windows/ntkrpamp.pdb/E12E472CBDC1417AA1755893ED23A668-2.json.xz
Is64Bit False
IsPAE True
layer_name 0 WindowsIntelPAE
memory_layer 1 FileLayer
KdDebuggerDataBlock 0x82b7ab78
NTBuildLab 7601.24214.x86fre.win7sp1_ldr_es
CSDVersion 1
KdVersionBlock 0x82b7ab50
Major/Minor 15.7601
MachineType 332
KeNumberProcessors 1
SystemTime 2023-02-20 19:10:54
NtSystemRoot C:\Windows
NtProductType NtProductWinNt
NtMajorVersion 6
NtMinorVersion 1
PE MajorOperatingSystemVersion 6
PE MinorOperatingSystemVersion 1
PE Machine 332
PE TimeDateStamp Thu Aug  2 02:12:23 2018

```

## 解法
