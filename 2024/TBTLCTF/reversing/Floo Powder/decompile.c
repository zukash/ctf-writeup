#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int dword_4020[31] = {
    80365906,   1769232938, 1128934032, 919644615,  268622536,  76757739,
    1906480421, 1839781169, 1764071040, 561586492,  1569349783, 1791633442,
    1419111682, 626666709,  380985946,  780831418,  762273460,  1434245458,
    750052501,  34417081,   244000852,  1179042137, 1198822017, 1411554630,
    1813829152, 133697279,  78464676,   854310990,  1336677923, 1611538180,
    617426944};
char byte_40C0[968];

void sub_11A9() {
  puts("Skulking around Knockturn Alley? Dodgy place...");
  exit(0);
}

int sub_11CA(int a1, int a2, int a3) {
  int result;  // rax

  result = byte_40C0[31 * a1 + a2] == 49;
  if ((byte_40C0[31 * a1 + a2] == 49) !=
      (((dword_4020[a3 / 31] >> (31 - a3 % 31 - 1)) & 1) != 0))
    sub_11A9();
  return result;
}

int main(int a1, char **a2, char **a3) {
  int i;    // [rsp+0h] [rbp-20h]
  int j;    // [rsp+4h] [rbp-1Ch]
  int v6;   // [rsp+8h] [rbp-18h]
  int v7;   // [rsp+Ch] [rbp-14h]
  int v8;   // [rsp+10h] [rbp-10h]
  int v9;   // [rsp+14h] [rbp-Ch]
  int v10;  // [rsp+18h] [rbp-8h]
  int v11;  // [rsp+1Ch] [rbp-4h]

  puts("Now don't forget to speak very, very clearly...");
  for (i = 0; i < 31; ++i) {
    scanf("%s", &byte_40C0[31 * i]);
    if (strlen(&byte_40C0[31 * i]) != 31) sub_11A9();
    for (j = 0; j < 31; ++j) {
      if (byte_40C0[31 * i + j] != 49 && byte_40C0[31 * i + j] != 48)
        sub_11A9();
    }
  }
  v6 = 0;
  v7 = 0;
  v8 = 0;
  v9 = 1;
  while (v6 < 31 && v7 < 31) {
    sub_11CA(v6, v7, v8++);
    if (v9 == 1) {
      v10 = v6 - 1;
      v11 = v7 + 1;
    } else {
      v10 = v6 + 1;
      v11 = v7 - 1;
    }
    if (v10 < 0 || v10 == 31 || v11 < 0 || v11 == 31) {
      if (v9 == 1) {
        v6 += v7 == 30;
        v7 += v7 < 30;
      } else {
        v7 += v6 == 30;
        v6 += v6 < 30;
      }
      v9 = 1 - v9;
    } else {
      v6 = v10;
      v7 = v11;
    }
  }
  puts("Welcome to Diagon Alley!");
  return 0LL;
}