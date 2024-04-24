#include <stdio.h>

int check(unsigned int a0, unsigned int a1, unsigned int a2)
{
    if (a0 > 2)
    {
        if (a1 > 2)
        {
            if (a2 <= 2)
            {
                return 0;
            }
            if (a0 * a0 * a0 + a1 * a1 * a1 != a2 * a2 * a2)
            {
                return 0;
            }
            return 1;
        }
        return 0;
    }
    return 0;
}

int main()
{
    unsigned int v0;  // [bp-0x1c]
    unsigned int v1;  // [bp-0x18]
    unsigned int v2;  // [bp-0x14]

    printf("Input a> ");
    scanf("%u", &v0);
    printf("Input b> ");
    scanf("%u", &v1);
    printf("Input c> ");
    scanf("%u", &v2);
    printf("(a, b, c) = (%u, %u, %u)\n", *((int *)&v0), *((int *)&v1), *((int *)&v2));
    printf("(a, b, c) = (%u, %u, %u)\n", (v0 * v0 * v0), (v1 * v1 * v1), (v2 * v2 * v2));
    printf("(a + b, c) = (%u, %u)\n", (v0 * v0 * v0) + (v1 * v1 * v1), (v2 * v2 * v2));
    if ((char)check(*((int *)&v0), *((int *)&v1), *((int *)&v2)) != 0)
    {
        puts("wow :o");
        // print_flag();
        return 0;
    }
    puts("Invalid value :(");
    return 0;
}