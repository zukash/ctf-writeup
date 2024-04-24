---
type: writeup
tags:
---

# Attaaaaack1

## 要約

## 考察

<https://qiita.com/ninja400/items/f3dd1e6eb80fd5b39ba9>

```bash
❯ vol -f memdump.raw windows.dlllist | less

❯ vol -f memdump.raw windows.pstree | less   
Volatility 3 Framework 2.4.1    PDB scanning finished                        

PID     PPID    ImageFileName   Offset(V)       Threads Handles SessionId       Wow64   CreateTime      ExitTime

4       0       System  0x8419c020      89      536     N/A     False   2023-02-20 19:01:19.000000      N/A
* 268   4       smss.exe        0x962f2020      2       29      N/A     False   2023-02-20 19:01:19.000000      N/A
352     344     csrss.exe       0x860a8c78      9       462     0       False   2023-02-20 19:01:20.000000      N/A
404     344     wininit.exe     0x855dfd20      3       76      0       False   2023-02-20 19:01:20.000000      N/A
* 480   404     services.exe    0x85ea2368      8       220     0       False   2023-02-20 19:01:20.000000      N/A
** 1280 480     svchost.exe     0x86071818      19      312     0       False   2023-02-20 19:01:22.000000      N/A
** 908  480     svchost.exe     0x85fae030      18      715     0       False   2023-02-20 19:01:21.000000      N/A
** 1420 480     svchost.exe     0x860b73c8      10      146     0       False   2023-02-20 19:01:22.000000      N/A
** 400  480     dllhost.exe     0x86251bf0      15      196     0       False   2023-02-20 19:01:26.000000      N/A
** 2576 480     svchost.exe     0x862cca38      15      232     0       False   2023-02-20 19:01:33.000000      N/A
** 1428 480     taskhost.exe    0x860ba030      9       205     1       False   2023-02-20 19:01:22.000000      N/A
** 2476 480     svchost.exe     0x85f89640      13      369     0       False   2023-02-20 19:03:25.000000      N/A
** 1848 480     vm3dservice.ex  0x8619dd20      4       60      0       False   2023-02-20 19:01:24.000000      N/A
*** 1908        1848    vm3dservice.ex  0x861b5360      2       44      1       False   2023-02-20 19:01:24.000000      N/A
** 952  480     svchost.exe     0x85fb7670      34      995     0       False   2023-02-20 19:01:22.000000      N/A
** 700  480     svchost.exe     0x85ef0a90      8       280     0       False   2023-02-20 19:01:21.000000      N/A
** 580  480     svchost.exe     0x861fc700      6       91      0       False   2023-02-20 19:01:25.000000      N/A
** 2248 480     sppsvc.exe      0x843068f8      4       146     0       False   2023-02-20 19:03:25.000000      N/A
** 1104 480     svchost.exe     0x85ff1380      18      391     0       False   2023-02-20 19:01:22.000000      N/A
** 1236 480     spoolsv.exe     0x8603a030      13      270     0       False   2023-02-20 19:01:22.000000      N/A
** 1884 480     vmtoolsd.exe    0x861a9030      13      290     0       False   2023-02-20 19:01:24.000000      N/A
** 868  480     svchost.exe     0x85f9c3a8      13      309     0       False   2023-02-20 19:01:21.000000      N/A
*** 1576        868     dwm.exe 0x861321c8      5       114     1       False   2023-02-20 19:01:23.000000      N/A
** 1636 480     VGAuthService.  0x841d7500      3       84      0       False   2023-02-20 19:01:23.000000      N/A
** 2276 480     SearchIndexer.  0x8629e188      12      581     0       False   2023-02-20 19:01:31.000000      N/A
** 2404 480     wmpnetwk.exe    0x8630b228      9       212     0       False   2023-02-20 19:01:32.000000      N/A
** 632  480     svchost.exe     0x85f4d030      10      357     0       False   2023-02-20 19:01:21.000000      N/A
*** 3020        632     WmiPrvSE.exe    0x85351030      11      242     0       False   2023-02-20 19:01:45.000000      N/A
*** 1748        632     WmiPrvSE.exe    0x86261030      10      204     0       False   2023-02-20 19:01:25.000000      N/A
** 752  480     svchost.exe     0x919e2958      22      507     0       False   2023-02-20 19:01:21.000000      N/A
*** 1556        752     audiodg.exe     0x84df2458      6       129     0       False   2023-02-20 19:10:50.000000      N/A
** 2168 480     msdtc.exe       0x8629e518      14      158     0       False   2023-02-20 19:01:31.000000      N/A
* 488   404     lsass.exe       0x85ea8610      6       568     0       False   2023-02-20 19:01:20.000000      N/A
* 496   404     lsm.exe 0x85eab718      10      151     0       False   2023-02-20 19:01:20.000000      N/A
416     396     csrss.exe       0x8550b030      9       268     1       False   2023-02-20 19:01:20.000000      N/A
* 1952  416     conhost.exe     0x84365c90      2       49      1       False   2023-02-20 19:03:40.000000      N/A
* 3664  416     conhost.exe     0x84f3d878      2       51      1       False   2023-02-20 19:10:52.000000      N/A
* 2924  416     conhost.exe     0x84384d20      2       49      1       False   2023-02-20 19:03:40.000000      N/A
508     396     winlogon.exe    0x85eacb80      5       115     1       False   2023-02-20 19:01:20.000000      N/A
1596    1540    explorer.exe    0x8613c030      29      842     1       False   2023-02-20 19:01:23.000000      N/A
* 1736  1596    vmtoolsd.exe    0x86189d20      8       179     1       False   2023-02-20 19:01:23.000000      N/A
* 2724  1596    DumpIt.exe      0x84f1caf8      2       38      1       False   2023-02-20 19:10:52.000000      N/A
* 3236  1596    ProcessHacker.  0x853faac8      9       416     1       False   2023-02-20 19:02:37.000000      N/A
2112    2876    cmd.exe 0x843658d0      1       20      1       False   2023-02-20 19:03:40.000000      N/A
2928    2876    cmd.exe 0x84368798      1       20      1       False   2023-02-20 19:03:40.000000      N/A
300     2876    runddl32.exe    0x84398998      10      2314    1       False   2023-02-20 19:03:40.000000      N/A
* 2556  300     notepad.exe     0x84390030      2       58      1       False   2023-02-20 19:03:41.000000      N/A


    svchost.exe
```

## 解法
