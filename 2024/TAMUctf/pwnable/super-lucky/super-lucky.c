#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <stdio.h>

int lucky_numbers[777]; 

void init() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);

    volatile int seed;
    int fd = open("/dev/urandom", O_RDONLY);
    read(fd, (char*)&seed, sizeof(seed));
    read(fd, (char*)&lucky_numbers, sizeof(lucky_numbers));
    srand(seed);
    seed = 0;

    close(fd);
}

int main() {
    init();

    puts("I'll give you a flag if you can guess the next 7 calls to rand(). As a benevolent level creator, I'll give you 21 free lucky numbers! Take your pick 0-777:");
    for (int i = 0; i < 21; ++i) {
        unsigned long pick = 0;
        scanf("%lu", &pick);
        printf("Here's lucky number #%d: %d\n", i + 1, lucky_numbers[pick]);
    }

    int all_correct = 1;

    for (int i = 0; i < 7; ++i) {
        int guess = 0;
        printf("Enter guess #%d:\n", i + 1);
        scanf("%d", &guess);
        all_correct &= guess == rand();
    }

    if (all_correct) {
        char buf[64];
        FILE* f = fopen("flag.txt", "r");
        fgets(buf, sizeof(buf), f);
        puts(buf);
    } else {
        puts("That's not correct :(");
    }
}


// 0x2952b853

/**
0x7f76b0918200 <randtbl>:       0x00000003      0x0cf4e270      0x9a7bddca      0x751f0941
0x7f76b0918210 <randtbl+16>:    0x2958671b      0x9ac95a03      0x52a29570      0x52f87a56
0x7f76b0918220 <randtbl+32>:    0xd08ac472      0x17da9e00      0x729df8e7      0x49a495ed
0x7f76b0918230 <randtbl+48>:    0x734d9929      0xd5bb9f41      0xf8713708      0xf38b25f2
0x7f76b0918240 <randtbl+64>:    0x7e112131      0x37ed3bcc      0x180bdc64      0x49cd214c
0x7f76b0918250 <randtbl+80>:    0xb7fdfc86      0xaace4db5      0xdfed78e4      0x2376437d
0x7f76b0918260 <randtbl+96>:    0x9b808a17      0x4b7d362a      0x753a16c0      0x119a9253
0x7f76b0918270 <randtbl+112>:   0x11bf9c6b      0xeb6351da      0xc802b50b      0x563bc19e
*/

// 1509545745
// 1305060083

"""
{    0x00000003,      0x75f25d04,      0x2b0b9e0d ,     0x3ecdc747,
 0x9b9345e7   ,   0x676f8d67   ,   0xd717c968    ,  0x44f4860a,
 0xfe51e258   ,   0xea307a1d   ,   0x09a60cbf    ,  0xb496b415,
 0xe497980e   ,   0x23048de6   ,   0x8f7a9f54    ,  0xd0a0effe,
 0xe79b80c5   ,   0xd5ee6e65   ,   0xec8ca5df    ,  0x1075feaa,
 0x2dea8a97   ,   0xf726f4d3   ,   0x727ab9ca    ,  0xe9f7603b,
 0xcff9691b   ,   0x4230e437   ,   0xa7edf83a    ,  0x5a0fffe0,
0x1dce5c9f    ,  0x01575408    ,  0xfaff8a50     , 0x93e6f016,
}

{3, 1978817796, 722181645, 1053673287, -1684847129, 1735363943, -686306968, 1156875786, -28188072, -365921763, 161877183, -1265191915, -459827186, 587501030, -1887789228, -794759170, -409239355, -705794459, -326326817, 276168362}
{
     0x00000003,      0x7a6361be ,     0x1a143a77 ,     0x332f7ff5,
  0x7ee707b4   ,   0x4192d242    ,  0x433d128f    ,  0x2e38f825,
  0x94166ace   ,   0x2efd3899    ,  0x4e444e95    ,  0xe9905d20,
  0xbadfb82b   ,   0x38d5169f    ,  0x6c6bc422    ,  0xdcdb70f5,
  0x9b373bc5   ,   0x3995b4d9    ,  0xda0b1a35    ,  0x4e308f5f
 }
"""

// 1228772794
// 0xaf2c857
// 12
// 5 + 3