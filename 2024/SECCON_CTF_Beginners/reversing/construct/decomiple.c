extern struct_0 *g_403fe8;

long long _init() {
  struct struct_0 **v1;  // rax, Other Possible Types: unsigned long

  v1 = g_403fe8;
  if (g_403fe8) v1 = g_403fe8();
  return v1;
}

extern unsigned long long g_403f98;

long long sub_401020() {
  unsigned long v0;  // [bp-0x8]

  v0 = g_403f98;
  goto *((long long *)4210592);
}

long long sub_401030() {
  void *v0;  // [bp-0x8]

  v0 = 0;
  return sub_401020();
}

long long sub_401040() {
  unsigned long long v0;  // [bp-0x8]

  v0 = 1;
  return sub_401020();
}

long long sub_401050() {
  unsigned long long v0;  // [bp-0x8]

  v0 = 2;
  return sub_401020();
}

long long sub_401060() {
  unsigned long long v0;  // [bp-0x8]

  v0 = 3;
  return sub_401020();
}

long long sub_401070() {
  unsigned long long v0;  // [bp-0x8]

  v0 = 4;
  return sub_401020();
}

long long sub_401080() {
  unsigned long long v0;  // [bp-0x8]

  v0 = 5;
  return sub_401020();
}

long long _start() {
  char v0;                // [bp+0x0], Other Possible Types: unsigned long
  unsigned long v1;       // [bp+0x8]
  unsigned long long v2;  // rsi
  unsigned long v3;       // rax
  unsigned long long v4;  // rdx

  v2 = *((long long *)&v0);
  v0 = v3;
  __libc_start_main(main, v2, &v1, 0, 0, v4); /* do not return */
}

// No decompilation output for function sub_401125

extern char __TMC_END__;
extern unsigned long long g_403fe0;

void deregister_tm_clones() { return; }

extern unsigned long long g_403ff0;

long long register_tm_clones() { return 0; }

extern char __TMC_END__;
extern unsigned long long g_403ff8;

long long __do_global_dtors_aux() {
  unsigned long v0;  // [bp-0x8]
  unsigned long v2;  // rax

  if (__TMC_END__) return v2;
  *((int *)&v0) = rbp<8>;
  if (!g_403ff8) {
    __TMC_END__ = 1;
    return (unsigned long long)deregister_tm_clones();
  }
  __cxa_finalize();
}

long long frame_dummy() { return register_tm_clones(); }

long long func_e0db2736(unsigned long a0, unsigned long a1) {
  unsigned long v0;  // [bp-0x18]
  unsigned long v2;  // rax

  v0 = a1;
  if ((unsigned int)a0 != 2) {
    puts("usage: construct <password>");
    _exit(1); /* do not return */
  }
  return v2;
}

typedef struct struct_0 {
  char padding_0[8];
  char *field_8;
} struct_0;

long long func_f8db6e92(unsigned long a0, struct_0 *a1) {
  unsigned int v0;        // [bp-0xc]
  unsigned long long v2;  // rax

  v0 = a0;
  v2 = strlen(a1->field_8);
  if (v2 != 32) exit(1); /* do not return */
  return v2;
}

typedef struct struct_0 {
  char padding_0[8];
  unsigned long long field_8;
} struct_0;

extern char g_402028;
extern unsigned int i;

long long func_91e3f562(unsigned long a0, struct_0 *a1) {
  unsigned int v0;  // [bp-0xc]

  v0 = a0;
  if (!strncmp(i + a1->field_8, &(&g_402028)[i], 2)) {
    i = i + 2;
    return i;
  }
  exit(1); /* do not return */
}

typedef struct struct_0 {
  char padding_0[8];
  unsigned long long field_8;
} struct_0;

extern char g_402050;
extern unsigned int i;

long long func_c285f76d(unsigned long a0, struct_0 *a1) {
  unsigned int v0;  // [bp-0xc]

  v0 = a0;
  if (!strncmp(i + a1->field_8, &(&g_402050)[i], 2)) {
    i = i + 2;
    return i;
  }
  exit(1); /* do not return */
}

typedef struct struct_0 {
  char padding_0[8];
  unsigned long long field_8;
} struct_0;

extern char g_402078;
extern unsigned int i;

long long func_b548021f(unsigned long a0, struct_0 *a1) {
  unsigned int v0;  // [bp-0xc]

  v0 = a0;
  if (!strncmp(i + a1->field_8, &(&g_402078)[i], 2)) {
    i = i + 2;
    return i;
  }
  exit(1); /* do not return */
}

typedef struct struct_0 {
  char padding_0[8];
  unsigned long long field_8;
} struct_0;

extern char g_4020a0;
extern unsigned int i;

long long func_af41723c(unsigned long a0, struct_0 *a1) {
  unsigned int v0;  // [bp-0xc]

  v0 = a0;
  if (!strncmp(i + a1->field_8, &(&g_4020a0)[i], 2)) {
    i = i + 2;
    return i;
  }
  exit(1); /* do not return */
}

typedef struct struct_0 {
  char padding_0[8];
  unsigned long long field_8;
} struct_0;

extern char g_4020c8;
extern unsigned int i;

long long func_1f5eba30(unsigned long a0, struct_0 *a1) {
  unsigned int v0;  // [bp-0xc]

  v0 = a0;
  if (!strncmp(i + a1->field_8, &(&g_4020c8)[i], 2)) {
    i = i + 2;
    return i;
  }
  exit(1); /* do not return */
}

typedef struct struct_0 {
  char padding_0[8];
  unsigned long long field_8;
} struct_0;

extern char g_4020f0;
extern unsigned int i;

long long func_da53ce29(unsigned long a0, struct_0 *a1) {
  unsigned int v0;  // [bp-0xc]

  v0 = a0;
  if (!strncmp(i + a1->field_8, &(&g_4020f0)[i], 2)) {
    i = i + 2;
    return i;
  }
  exit(1); /* do not return */
}

typedef struct struct_0 {
  char padding_0[8];
  unsigned long long field_8;
} struct_0;

extern char g_402118;
extern unsigned int i;

long long func_bae805f6(unsigned long a0, struct_0 *a1) {
  unsigned int v0;  // [bp-0xc]

  v0 = a0;
  if (!strncmp(i + a1->field_8, &(&g_402118)[i], 2)) {
    i = i + 2;
    return i;
  }
  exit(1); /* do not return */
}

typedef struct struct_0 {
  char padding_0[8];
  unsigned long long field_8;
} struct_0;

extern char g_402140;
extern unsigned int i;

long long func_d902e81f(unsigned long a0, struct_0 *a1) {
  unsigned int v0;  // [bp-0xc]

  v0 = a0;
  if (!strncmp(i + a1->field_8, &(&g_402140)[i], 2)) {
    i = i + 2;
    return i;
  }
  exit(1); /* do not return */
}

typedef struct struct_0 {
  char padding_0[8];
  unsigned long long field_8;
} struct_0;

extern char g_402168;
extern unsigned int i;

long long func_74b2a53c(unsigned long a0, struct_0 *a1) {
  unsigned int v0;  // [bp-0xc]

  v0 = a0;
  if (!strncmp(i + a1->field_8, &(&g_402168)[i], 2)) {
    i = i + 2;
    return i;
  }
  exit(1); /* do not return */
}

typedef struct struct_0 {
  char padding_0[8];
  unsigned long long field_8;
} struct_0;

extern char g_402190;
extern unsigned int i;

long long func_3d90c2fa(unsigned long a0, struct_0 *a1) {
  unsigned int v0;  // [bp-0xc]

  v0 = a0;
  if (!strncmp(i + a1->field_8, &(&g_402190)[i], 2)) {
    i = i + 2;
    return i;
  }
  exit(1); /* do not return */
}

typedef struct struct_0 {
  char padding_0[8];
  unsigned long long field_8;
} struct_0;

extern char g_4021b8;
extern unsigned int i;

long long func_69fd4a70(unsigned long a0, struct_0 *a1) {
  unsigned int v0;  // [bp-0xc]

  v0 = a0;
  if (!strncmp(i + a1->field_8, &(&g_4021b8)[i], 2)) {
    i = i + 2;
    return i;
  }
  exit(1); /* do not return */
}

typedef struct struct_0 {
  char padding_0[8];
  unsigned long long field_8;
} struct_0;

extern char g_4021e0;
extern unsigned int i;

long long func_9e540c6a(unsigned long a0, struct_0 *a1) {
  unsigned int v0;  // [bp-0xc]

  v0 = a0;
  if (!strncmp(i + a1->field_8, &(&g_4021e0)[i], 2)) {
    i = i + 2;
    return i;
  }
  exit(1); /* do not return */
}

typedef struct struct_0 {
  char padding_0[8];
  unsigned long long field_8;
} struct_0;

extern char g_402208;
extern unsigned int i;

long long func_35efd7b6(unsigned long a0, struct_0 *a1) {
  unsigned int v0;  // [bp-0xc]

  v0 = a0;
  if (!strncmp(i + a1->field_8, &(&g_402208)[i], 2)) {
    i = i + 2;
    return i;
  }
  exit(1); /* do not return */
}

typedef struct struct_0 {
  char padding_0[8];
  unsigned long long field_8;
} struct_0;

extern char g_402230;
extern unsigned int i;

long long func_3b8e07a4(unsigned long a0, struct_0 *a1) {
  unsigned int v0;  // [bp-0xc]

  v0 = a0;
  if (!strncmp(i + a1->field_8, &(&g_402230)[i], 2)) {
    i = i + 2;
    return i;
  }
  exit(1); /* do not return */
}

typedef struct struct_0 {
  char padding_0[8];
  unsigned long long field_8;
} struct_0;

extern char g_402258;
extern unsigned int i;

long long func_21670b38(unsigned long a0, struct_0 *a1) {
  unsigned int v0;  // [bp-0xc]

  v0 = a0;
  if (!strncmp(i + a1->field_8, &(&g_402258)[i], 2)) {
    i = i + 2;
    return i;
  }
  exit(1); /* do not return */
}

typedef struct struct_0 {
  char padding_0[8];
  unsigned long long field_8;
} struct_0;

extern char g_402280;
extern unsigned int i;

long long func_30b49da1(unsigned long a0, struct_0 *a1) {
  unsigned int v0;  // [bp-0xc]

  v0 = a0;
  if (!strncmp(i + a1->field_8, &(&g_402280)[i], 2)) {
    i = i + 2;
    return i;
  }
  exit(1); /* do not return */
}

typedef struct struct_0 {
  char padding_0[8];
  unsigned long long field_8;
} struct_0;

int main(unsigned long a0) {
  unsigned int v0;  // [bp-0xc]
  struct_0 *v2;     // rsi

  v0 = a0;
  puts("CONGRATULATIONS!");
  printf("The flag is ctf4b{%s}\n", (unsigned int)v2->field_8);
  _exit(0); /* do not return */
}

long long func_dc69ef50() { return puts("WRONG"); }

long long _fini() {
  unsigned long v1;  // rax

  return v1;
}
