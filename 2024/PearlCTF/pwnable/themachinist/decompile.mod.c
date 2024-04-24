int32_t main(int32_t argc, char** argv, char** envp)
{
    void* fsbase;
    int64_t rax = *(fsbase + 0x28);
    setvbuf(stdout, nullptr, 2, 0);
    setvbuf(stdin, nullptr, 1, 0);
    int32_t var_50 = 0;
    int32_t var_4c = 0;
    int32_t var_48 = 0;
    puts("Welcome to the Sauce Adventure!");
    int32_t rax_44;
    while (true)
    {
        puts("\nMenu:");
        puts("1. The Sauce Guessing Game");
        puts("2. Make Your Own Sauce");
        puts("3. Check Your Eliteness");
        puts("4. Exit");
        printf("Enter your choice (1-4): ");
        int32_t var_5c;
        if (__isoc99_scanf(&data_209b, &var_5c) != 1)
        {
            puts("Invalid input. Please enter a va…");
            int32_t i;
            do
            {
                i = getchar();
            } while (i != 0xa);
        }
        else
        {
            int32_t rax_4 = var_5c;
            if (rax_4 == 4)
            {
                puts("Goodbye! Thanks for playing with…");
            }
            else if (rax_4 > 4)
            {
            label_18a6:
                puts("Invalid choice. Please enter a n…");
            }
            else if (rax_4 != 3)
            {
                if (rax_4 > 3)
                {
                    goto label_18a6;
                }
                if (rax_4 != 1)
                {
                    if (rax_4 != 2)
                    {
                        goto label_18a6;
                    }
                    if (var_4c != 0)
                    {
                        puts("You've already made your own sau…");
                    }
                    else
                    {
                        puts("Welcome to the 'Make Your Own Sa…");
                        puts("Feel free to experiment with var…");
                        char* var_38 = nullptr;
                        printf("Enter an existing sauce that you…");
                        if (__isoc99_scanf(&data_23ab, &var_38) != 1)
                        {
                            puts("Invalid sauce!");
                        }
                        else
                        {
                            printf("Choose an ingredient: ");
                            int32_t var_58;
                            int32_t rax_19 = __isoc99_scanf(&data_209b, &var_58);
                            if (((rax_19 != 1 || (rax_19 == 1 && var_58 < 0)) || ((rax_19 == 1 && var_58 >= 0) && var_58 > 7)))
                            {
                                puts("What ingredient is that?!");
                            }
                            if (((rax_19 == 1 && var_58 >= 0) && var_58 <= 7))
                            {
                                printf("Do you want to add or remove the…");
                                char var_5d;
                                if (__isoc99_scanf(&data_242a, &var_5d) != 1)
                                {
                                    puts("Invalid operation!");
                                }
                                else
                                {
                                    if ((var_5d != 0x61 && var_5d != 0x72))
                                    {
                                        puts("What did you just do?!");
                                    }
                                    if (var_5d == 0x72)
                                    {
                                        if (var_38 == 0)
                                        {
                                            puts("The sauce blew up!");
                                        }
                                        else
                                        {
                                            *var_38 = (*var_38 & !((1 << var_58)));
                                            puts("Ingredient removed successfully.");
                                        }
                                    }
                                    if (var_5d == 0x61)
                                    {
                                        if (var_38 == 0)
                                        {
                                            puts("The sauce blew up!");
                                        }
                                        else
                                        {
                                            *var_38 = (*var_38 | (1 << var_58));
                                            puts("Ingredient added successfully.");
                                        }
                                    }
                                    if (((var_5d == 0x61 && var_38 != 0) || (var_5d == 0x72 && var_38 != 0)))
                                    {
                                        var_4c = 1;
                                    }
                                }
                            }
                        }
                    }
                }
                else if (var_50 != 0)
                {
                    puts("You've already played the secret…");
                }
                else
                {
                    int32_t (* var_18_1)(int32_t argc, char** argv, char** envp) = main;
                    int32_t var_44_1 = 0x64;
                    int32_t var_54_1 = 0;
                    puts("You have stumbled upon a mysteri…");
                    printf("You have %d attempts!\n", var_44_1);
                    while (var_54_1 < var_44_1)
                    {
                        printf("Enter your sauce recipe: ");
                        int64_t var_40;
                        if (__isoc99_scanf(&data_21ba, &var_40) == 1)
                        {
                            var_54_1 = (var_54_1 + 1);
                            if (var_18_1 > var_40)
                            {
                                puts("Oh no! Your sauce is bland!");
                            }
                            else
                            {
                                if (var_18_1 >= var_40)
                                {
                                    puts("Congratulations! You got it righ…");
                                    break;
                                }
                                puts("Whoa! Your sauce is overdone!");
                            }
                        }
                        else
                        {
                            puts("Invalid sauce!");
                            int32_t i_1;
                            do
                            {
                                i_1 = getchar();
                            } while (i_1 != 0xa);
                        }
                    }
                    var_50 = 1;
                    if (var_54_1 == var_44_1)
                    {
                        puts("Sorry, you've reached the maximu…");
                    }
                }
            }
            // rax_4 == 3
            else if (var_48 != 0x539)
            {
                puts("You're not elite enough to acces…");
            }
            // rax_4 == 3 && var_48 == 0x539
            else
            {
                FILE* fp = fopen("flag.txt", &data_24b8);
                if (fp == 0)
                {
                    perror("Error opening file");
                }
                else
                {
                    fseek(fp, 0, 2);
                    int64_t count = ftell(fp);
                    fseek(fp, 0, 0);
                    void* buf = malloc((count + 1));
                    if (buf == 0)
                    {
                        perror("Error allocating memory");
                        fclose(fp);
                        rax_44 = 2;
                        break;
                    }
                    fread(buf, 1, count, fp);
                    *(buf + count) = 0;
                    printf(&data_24ee, buf);
                    free(buf);
                    fclose(fp);
                }
            }
        }
        if (var_5c == 4)
        {
            rax_44 = 0;
            break;
        }
    }
    *(fsbase + 0x28);
    if (rax == *(fsbase + 0x28))
    {
        return rax_44;
    }
    __stack_chk_fail();
    /* no return */
}
