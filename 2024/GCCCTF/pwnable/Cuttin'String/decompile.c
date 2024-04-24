int64_t __LOAD_SYS_READ() __pure
{
    return 0;
}

int64_t __LOAD_SYS_WRITE() __pure
{
    int64_t rax;
    rax = 1;
    return 1;
}

int64_t _PUTS(char* arg1, void* arg2)
{
    char* rdx = arg1;
    if (rdx == 0)
    {
        char i;
        do
        {
            i = *(rdx + arg2);
            rdx = &rdx[1];
        } while (i != 0);
    }
    return syscall(sys_write {1}, 1, arg2, (rdx - 1));
}

int64_t _read_and_print_str(int64_t arg1)
{
    void var_208;
    void* rsi = &var_208;
    syscall(sys_read {0}, 0, rsi, 0x512);
    void* var_210 = &var_208;
    int64_t var_218 = arg1;
    return _PUTS(nullptr, rsi);
}

int64_t _get_len_str()
{
    void var_10;
    void* rsi = &var_10;
    syscall(sys_read {0}, 0, rsi, 8);
    int64_t r10 = 0;
    int64_t rcx = 0;
    while (true)
    {
        int64_t rax_1;
        rax_1 = *(&var_10 + rcx);
        if ((rax_1 != 0 && rax_1 != 0xa))
        {
            if (rax_1 < 0x30)
            {
                break;
            }
            if (rax_1 > 0x39)
            {
                break;
            }
            if (rcx != 0)
            {
                r10 = (r10 * 0xa);
            }
            rax_1 = (rax_1 - 0x30);
            r10 = (r10 + rax_1);
            rcx = (rcx + 1);
            if (rcx != 8)
            {
                continue;
            }
        }
        return rax_1;
    }
    char const* const var_18 = "Error. Enter a number in decimal…";
    int64_t var_20 = 0;
    _PUTS(nullptr, rsi);
    syscall(sys_exit {0x3c}, 0);
    /* no return */
}

int64_t _main_loop(char* arg1, void* arg2)
{
    void* const var_10 = "Enter the length of the string (…";
    int64_t var_18 = 0;
    _PUTS(arg1, arg2);
    void* rsi;
    int64_t r10;
    rsi = _get_len_str();
    void* const var_10_1 = "Enter the string to cut > ";
    int64_t var_18_1 = 0;
    _PUTS(nullptr, rsi);
    int64_t var_10_2 = (r10 + 1);
    void* rsi_1 = _read_and_print_str(1);
    void* const var_10_3 = "\n\n---\n";
    int64_t var_18_2 = 0;
    return _PUTS(&*nullptr->ident.signature[1], rsi_1);
}

void _start(char* arg1, void* arg2) __noreturn
{
    void* const var_8 = "\nCuttin'String, the smallest st…";
    int64_t var_10 = 0;
    void* rsi = _PUTS(arg1, arg2);
    while (true)
    {
        rsi = _main_loop(&*nullptr->ident.signature[1], rsi);
    }
}

