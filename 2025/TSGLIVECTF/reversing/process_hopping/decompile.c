int64_t (* const)() _init()
{
    if (!__gmon_start__)
        return __gmon_start__;
    
    return __gmon_start__();
}

int64_t sub_401020()
{
    int64_t var_8 = 0;
    /* jump -> nullptr */
}

int64_t sub_401030()
{
    int64_t var_8 = 0;
    /* tailcall */
    return sub_401020();
}

int64_t sub_401040()
{
    int64_t var_8 = 1;
    /* tailcall */
    return sub_401020();
}

int64_t sub_401050()
{
    int64_t var_8 = 2;
    /* tailcall */
    return sub_401020();
}

int64_t sub_401060()
{
    int64_t var_8 = 3;
    /* tailcall */
    return sub_401020();
}

int64_t sub_401070()
{
    int64_t var_8 = 4;
    /* tailcall */
    return sub_401020();
}

int64_t sub_401080()
{
    int64_t var_8 = 5;
    /* tailcall */
    return sub_401020();
}

int64_t sub_401090()
{
    int64_t var_8 = 6;
    /* tailcall */
    return sub_401020();
}

int64_t sub_4010a0()
{
    int64_t var_8 = 7;
    /* tailcall */
    return sub_401020();
}

void __cxa_finalize(void* d)
{
    /* tailcall */
    return __cxa_finalize(d);
}

int32_t puts(char const* str)
{
    /* tailcall */
    return puts(str);
}

void __stack_chk_fail() __noreturn
{
    /* tailcall */
    return __stack_chk_fail();
}

int32_t printf(char const* format, ...)
{
    /* tailcall */
    return printf();
}

int32_t fflush(FILE* fp)
{
    /* tailcall */
    return fflush(fp);
}

pid_t waitpid(pid_t pid, int32_t* stat_loc, int32_t options)
{
    /* tailcall */
    return waitpid(pid, stat_loc, options);
}

int32_t __isoc99_scanf(char const* format, ...)
{
    /* tailcall */
    return __isoc99_scanf();
}

void exit(int32_t status) __noreturn
{
    /* tailcall */
    return exit(status);
}

pid_t fork()
{
    /* tailcall */
    return fork();
}

void _start(int64_t arg1, int64_t arg2, void (* arg3)()) __noreturn
{
    int64_t stack_end_1;
    int64_t stack_end = stack_end_1;
    void ubp_av;
    __libc_start_main(main, __return_addr, &ubp_av, nullptr, nullptr, arg3, &stack_end);
    /* no return */
}

uint64_t* const* deregister_tm_clones()
{
    return &stdout;
}

int64_t (* const)() sub_4011a0()
{
    return nullptr;
}

void _FINI_0()
{
    if (data_4040a8)
        return;
    
    if (__cxa_finalize)
        __cxa_finalize(data_404008);
    
    deregister_tm_clones();
    data_4040a8 = 1;
}

int64_t (* const)() _INIT_0()
{
    /* tailcall */
    return sub_4011a0();
}

int64_t sub_401229(int32_t arg1)
{
    if (arg1 == data_4040e8)
        return 0;
    
    if (arg1 == data_4040e0)
        return 0x15;
    
    if (arg1 == data_404120)
        return 1;
    
    if (arg1 == data_4040ec)
        return 0x17;
    
    if (arg1 == data_404100)
        return 0xb;
    
    if (arg1 == data_4040f4)
        return 2;
    
    if (arg1 == data_4040f8)
        return 5;
    
    if (arg1 == data_4040fc)
        return 0xa;
    
    if (arg1 == data_404124)
        return 3;
    
    if (arg1 == data_404144)
        return 0x16;
    
    if (arg1 == data_40411c)
        return 0x18;
    
    if (arg1 == data_404130)
        return 9;
    
    if (arg1 == data_404118)
        return 0x11;
    
    if (arg1 == data_404134)
        return 4;
    
    if (arg1 == data_4040e4)
        return 0x1e;
    
    if (arg1 == data_404108)
        return 0x12;
    
    if (arg1 == data_4040f0)
        return 0x14;
    
    if (arg1 == data_404150)
        return 0x13;
    
    if (arg1 == data_40414c)
        return 8;
    
    if (arg1 == data_40410c)
        return 0x19;
    
    if (arg1 == data_404114)
        return 0x1f;
    
    if (arg1 == data_404104)
        return 6;
    
    if (arg1 == data_404140)
        return 7;
    
    if (arg1 == data_404138)
        return 0xc;
    
    if (arg1 == data_40412c)
        return 0x1d;
    
    if (arg1 == data_404110)
        return 0x1a;
    
    if (arg1 == data_40415c)
        return 0xf;
    
    if (arg1 == data_404148)
        return 0x10;
    
    if (arg1 == data_40413c)
        return 0xd;
    
    if (arg1 == data_404154)
        return 0x1c;
    
    if (arg1 == data_404158)
        return 0x1b;
    
    if (arg1 != data_404128)
        return 0;
    
    return 0xe;
}

int64_t sub_4014c6(int32_t arg1)
{
    if (arg1 == data_4040e0)
        return 0x61;
    
    if (arg1 == data_404120)
        return 0x62;
    
    if (arg1 == data_4040e8)
        return 0x41;
    
    if (arg1 == data_4040ec)
        return 0x61;
    
    if (arg1 == data_404100)
        return 0x54;
    
    if (arg1 == data_4040f4)
        return 0x4b;
    
    if (arg1 == data_4040f8)
        return 0x4e;
    
    if (arg1 == data_4040fc)
        return 0x61;
    
    if (arg1 == data_404124)
        return 0x4b;
    
    if (arg1 == data_404144)
        return 0x6c;
    
    if (arg1 == data_40411c)
        return 0x61;
    
    if (arg1 == data_404130)
        return 0x6f;
    
    if (arg1 == data_404134)
        return 0x61;
    
    if (arg1 == data_4040e4)
        return 0x30;
    
    if (arg1 == data_404108)
        return 0x31;
    
    if (arg1 == data_4040f0)
        return 0x74;
    
    if (arg1 == data_404150)
        return 0x4d;
    
    if (arg1 == data_40414c)
        return 0x35;
    
    if (arg1 == data_40410c)
        return 0x72;
    
    if (arg1 == data_404114)
        return 0x49;
    
    if (arg1 == data_404104)
        return 0x75;
    
    if (arg1 == data_404118)
        return 0x78;
    
    if (arg1 == data_404140)
        return 0x6e;
    
    if (arg1 == data_404138)
        return 0x61;
    
    if (arg1 == data_40412c)
        return 0x42;
    
    if (arg1 == data_404110)
        return 0x38;
    
    if (arg1 == data_40415c)
        return 0x4f;
    
    if (arg1 == data_404148)
        return 0x4d;
    
    if (arg1 == data_40413c)
        return 0x43;
    
    if (arg1 == data_404154)
        return 0x39;
    
    if (arg1 == data_404158)
        return 0x71;
    
    if (arg1 != data_404128)
        return 0x70;
    
    return 0x61;
}

int32_t main(int32_t argc, char** argv, char** envp)
{
    void* fsbase;
    int64_t rax = *(fsbase + 0x28);
    printf("FLAG> ");
    fflush(stdout);
    char var_38[0x28];
    __isoc99_scanf("%31s", &var_38);
    int32_t var_44 = 0;
    pid_t pid;
    
    while (true)
    {
        pid = fork();
        
        if (pid)
            break;
        
        var_44 += 1;
        
        if (var_44 > 0x1f)
        {
            exit(0);
            /* no return */
        }
    }
    
    (&data_4040e0)[var_44] = pid;
    int32_t stat_loc;
    waitpid(pid, &stat_loc, 0);
    
    if (!(stat_loc & 0x7f) && stat_loc >> 8 == 0x63)
    {
        exit(0x63);
        /* no return */
    }
    
    char rax_13 = sub_4014c6(pid);
    
    if ((var_38[sub_401229(pid)] ^ rax_13) != *(((var_44 ^ 0x1f) << 2) + &data_404020))
    {
        puts("\nWrong...");
        exit(0x63);
        /* no return */
    }
    
    if (var_44)
    {
        exit(0);
        /* no return */
    }
    
    if (!stat_loc)
        puts("\nCorrect!");
    
    *(fsbase + 0x28);
    
    if (rax == *(fsbase + 0x28))
        return 0;
    
    __stack_chk_fail();
    /* no return */
}

int64_t _fini() __pure
{
    return;
}

