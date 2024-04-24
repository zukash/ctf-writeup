int64_t init()
{
    setvbuf(stdout, nullptr, 2, 0);
    setvbuf(stdin, nullptr, 2, 0);
    return setvbuf(stderr, nullptr, 2, 0);
}

int64_t menu()
{
    puts("Enter your choice");
    puts("1. Create a note");
    puts("2. Delete a note");
    puts("3. Edit a note");
    puts("4. Read a note");
    return puts("5. Exit");
}

int32_t main(int32_t argc, char** argv, char** envp)
{
    void* fsbase;
    int64_t rax = *(fsbase + 0x28);
    init();
    int32_t var_1bc = 0;
    while (true)
    {
        menu();
        int32_t var_1c4;
        __isoc99_scanf(&data_2062, &var_1c4);
        getchar();
        void var_1a8;
        if (var_1c4 == 1)
        {
            char* buf = malloc(0x28);
            puts("Enter the note");
            fgets(buf, 0xa, stdin);
            puts("Note created");
            *(&var_1a8 + (var_1bc << 3)) = buf;
            var_1bc = (var_1bc + 1);
        }
        else
        {
            int32_t var_1c0;
            if (var_1c4 == 2)
            {
                puts("Which note do you want to delete…");
                __isoc99_scanf(&data_2062, &var_1c0);
                getchar();
                if (var_1bc < var_1c0)
                {
                    puts("Invalid choice");
                }
                else
                {
                    free(*(&var_1a8 + ((var_1c0 - 1) << 3)));
                }
            }
            else if (var_1c4 == 3)
            {
                puts("Which note do you want to edit?");
                __isoc99_scanf(&data_2062, &var_1c0);
                getchar();
                if (var_1bc < var_1c0)
                {
                    puts("Invalid choice");
                }
                else
                {
                    fgets(*(&var_1a8 + ((var_1c0 - 1) << 3)), 0x64, stdin);
                    puts("Note edited");
                }
            }
            else if (var_1c4 == 4)
            {
                puts("Which note do you want to read?");
                __isoc99_scanf(&data_2062, &var_1c0);
                getchar();
                if (var_1bc < var_1c0)
                {
                    puts("Invalid choice");
                }
                else
                {
                    puts(*(&var_1a8 + ((var_1c0 - 1) << 3)));
                }
            }
            else
            {
                if (var_1c4 == 5)
                {
                    break;
                }
                if (var_1c4 == 0xa)
                {
                    char* buf_1 = malloc(0x4b0);
                    puts("Enter the note");
                    fgets(buf_1, 0xa, stdin);
                    puts("Note created");
                    *(&var_1a8 + (var_1bc << 3)) = buf_1;
                    var_1bc = (var_1bc + 1);
                }
            }
        }
    }
    if (rax == *(fsbase + 0x28))
    {
        return 0;
    }
    __stack_chk_fail();
    /* no return */
}

