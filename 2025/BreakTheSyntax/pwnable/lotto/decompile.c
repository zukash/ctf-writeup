int __fastcall main(int argc, const char **argv, const char **envp) {
  size_t v3;             // rax
  unsigned int v4;       // eax
  int i;                 // [rsp+4h] [rbp-33Ch]
  int j;                 // [rsp+8h] [rbp-338h]
  int k;                 // [rsp+Ch] [rbp-334h]
  __int128 v9;           // [rsp+10h] [rbp-330h] BYREF
  _QWORD v10[50];        // [rsp+20h] [rbp-320h] BYREF
  char s[376];           // [rsp+1B0h] [rbp-190h] BYREF
  __int16 v12;           // [rsp+328h] [rbp-18h]
  char v13;              // [rsp+32Ah] [rbp-16h]
  unsigned __int64 v14;  // [rsp+338h] [rbp-8h]

  v14 = __readfsqword(0x28u);
  memset(&v10[2], 0, 379);
  v9 = 0;
  v10[0] = 0;
  *(_DWORD *)((char *)&v10[40] + 7) = 0;
  getrandom((char *)&v10[40] + 7, 4, 0);
  *(_QWORD *)((char *)&v10[6] + 4) = *(
      _QWORD *)"    .____           __    __          \n"
               "    |    |    _____/  |__/  |_  ____  \n"
               "    |    |   /  _ \\   __\\   __\\/    \\ \n"
               "    |    |__(  <_> )  |  |  | (  <_> )\n"
               "    |_______ \\____/|__|  |__|  \\____/ \n"
               "            \\/                        \n"
               "    Enter 6 numbers in range 1 to 49   \n";
  *(_QWORD *)((char *)&v10[39] + 7) = *(_QWORD *)&aUUUUUU[-16];
  qmemcpy(
      &v10[7], &asc_2008[-((char *)&v10[6] + 4 - (char *)&v10[7])],
      8LL * ((((unsigned int)((char *)&v10[6] + 4 - (char *)&v10[7]) + 275) &
              0xFFFFFFF8) >>
             3));
  strcpy((char *)&v10[41] + 3, "    Better luck next time ;)  \n");
  strcpy((char *)&v10[45] + 3, "    Number of correct guesses: ");
  setbuf(_bss_start, 0);
  printf("%s\n    ", (const char *)&v10[6] + 4);
  memset(s, 0, sizeof(s));
  v12 = 0;
  v13 = 0;
  fgets(s, 379, stdin);
  v3 = strlen(s);
  memcpy((char *)&v10[2] + 4, s, v3);
  srand(*(unsigned int *)((char *)&v10[40] + 7));
  __isoc99_sscanf((char *)&v10[2] + 4, "%u %u %u %u %u %u", &v9,
                  (char *)&v9 + 4, (char *)&v9 + 8, (char *)&v9 + 12, v10,
                  (char *)v10 + 4);
  for (i = 0; i <= 5; ++i) winingNumbers[i] = rand() % 49 + 1;
  for (j = 0; j <= 5; ++j) {
    ++userLookup[*((unsigned int *)&v10[-2] + j)];
    ++winingLookup[winingNumbers[j]];
  }
  for (k = 0; k <= 48; ++k) {
    if (userLookup[k] && winingLookup[k]) {
      v4 = userLookup[k];
      if (winingLookup[k] <= v4) v4 = winingLookup[k];
      LODWORD(v10[2]) += v4;
    }
  }
  if (LODWORD(v10[2]) == 6) {
    system("cat flag");
  } else {
    printf("%s%u\n", (const char *)&v10[45] + 3, LODWORD(v10[2]));
    puts((const char *)&v10[41] + 3);
  }
  return 0;
}
