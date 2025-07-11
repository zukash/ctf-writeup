/* This file was generated by the Hex-Rays decompiler version 9.1.0.250226.
   Copyright (c) 2007-2021 Hex-Rays <info@hex-rays.com>

   Detected compiler: GNU C++
*/

#include <defs.h>


//-------------------------------------------------------------------------
// Function declarations

__int64 (**init_proc())(void);
void sub_401020();
void sub_401030();
void sub_401040();
void sub_401050();
// void setbuf(FILE *stream, char *buf);
// void *memset(void *s, int c, size_t n);
// ssize_t read(int fd, void *buf, size_t nbytes);
void __fastcall __noreturn start(__int64 a1, __int64 a2, void (*a3)(void));
void dl_relocate_static_pie();
FILE **deregister_tm_clones();
__int64 register_tm_clones();
FILE **_do_global_dtors_aux();
__int64 frame_dummy(); // weak
void gadgets();
__int64 __fastcall gets(void *a1);
int __fastcall main(int argc, const char **argv, const char **envp);
void term_proc();
// int _libc_start_main(int (*main)(int, char **, char **), int argc, char **ubp_av, void (*init)(void), void (*fini)(void), void (*rtld_fini)(void), void *stack_end);
// int puts(const char *s);
// __int64 _gmon_start__(void); weak

//-------------------------------------------------------------------------
// Data declarations

int (*print)(const char *s) = &puts; // weak
FILE *_bss_start; // idb
char completed_0; // weak


//----- (0000000000401000) ----------------------------------------------------
__int64 (**init_proc())(void)
{
  __int64 (**result)(void); // rax

  result = &_gmon_start__;
  if ( &_gmon_start__ )
    return (__int64 (**)(void))_gmon_start__();
  return result;
}
// 404058: using guessed type __int64 _gmon_start__(void);

//----- (0000000000401020) ----------------------------------------------------
void sub_401020()
{
  JUMPOUT(0);
}
// 401026: control flows out of bounds to 0

//----- (0000000000401030) ----------------------------------------------------
void sub_401030()
{
  sub_401020();
}

//----- (0000000000401040) ----------------------------------------------------
void sub_401040()
{
  sub_401020();
}

//----- (0000000000401050) ----------------------------------------------------
void sub_401050()
{
  sub_401020();
}

//----- (0000000000401090) ----------------------------------------------------
// positive sp value has been detected, the output may be wrong!
void __fastcall __noreturn start(__int64 a1, __int64 a2, void (*a3)(void))
{
  __int64 v3; // rax
  int v4; // esi
  __int64 v5; // [rsp-8h] [rbp-8h] BYREF
  char *retaddr; // [rsp+0h] [rbp+0h] BYREF

  v4 = v5;
  v5 = v3;
  _libc_start_main((int (*)(int, char **, char **))main, v4, &retaddr, 0, 0, a3, &v5);
  __halt();
}
// 40109A: positive sp value 8 has been found
// 4010A1: variable 'v3' is possibly undefined

//----- (00000000004010C0) ----------------------------------------------------
void dl_relocate_static_pie()
{
  ;
}

//----- (00000000004010D0) ----------------------------------------------------
FILE **deregister_tm_clones()
{
  return &_bss_start;
}

//----- (0000000000401100) ----------------------------------------------------
__int64 register_tm_clones()
{
  return 0;
}

//----- (0000000000401140) ----------------------------------------------------
FILE **_do_global_dtors_aux()
{
  FILE **result; // rax

  if ( !completed_0 )
  {
    result = deregister_tm_clones();
    completed_0 = 1;
  }
  return result;
}
// 404020: using guessed type char completed_0;

//----- (0000000000401170) ----------------------------------------------------
__int64 frame_dummy()
{
  return register_tm_clones();
}
// 401170: using guessed type __int64 frame_dummy();

//----- (0000000000401176) ----------------------------------------------------
void gadgets()
{
  ;
}

//----- (0000000000401183) ----------------------------------------------------
__int64 __fastcall gets(void *a1)
{
  int v2; // [rsp+1Ch] [rbp-4h]

  v2 = read(0, a1, 0x2BCu);
  if ( v2 > 0 )
    *((_BYTE *)a1 + v2 - 1) = 0;
  return (unsigned int)v2;
}

//----- (00000000004011CF) ----------------------------------------------------
int __fastcall main(int argc, const char **argv, const char **envp)
{
  char s[32]; // [rsp+0h] [rbp-20h] BYREF

  setbuf(_bss_start, 0);
  memset(s, 0, sizeof(s));
  gets(s);
  print(s);
  return 0;
}
// 404010: using guessed type int (*print)(const char *s);

//----- (0000000000401228) ----------------------------------------------------
void term_proc()
{
  ;
}

// nfuncs=24 queued=15 decompiled=15 lumina nreq=0 worse=0 better=0
// ALL OK, 15 function(s) have been successfully decompiled