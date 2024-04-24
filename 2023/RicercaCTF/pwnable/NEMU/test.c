#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>

void caller(void (*fp)(void)) {
    fp();
}


int main(void) {
    int a = 1;
    // int b = 2;
    // int c = 3;
    // int d = 4;
    // int e = 5;
    // int f = 6;
    // int g = 7;
    // int h = 8;
    // int i = 9;
    // int j = 10;
    void inner_func(void) {
        printf("%d\n", a);
        // printf("%d\n", b);
        // printf("%d\n", c);
        // printf("%d\n", d);
        // printf("%d\n", e);
        // printf("%d\n", f);
        // printf("%d\n", g);
        // printf("%d\n", h);
        // printf("%d\n", i);
        // printf("%d\n", j);
    }


    inner_func;
    caller(inner_func);
    caller(inner_func);
}

