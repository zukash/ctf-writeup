#include <stdio.h>
#include <string.h>

int main() {
  const int key[50] = {119, 20,  96, 6,   50,  80,  43,  28, 117, 22,
                       125, 34,  21, 116, 23,  124, 35,  18, 35,  85,
                       56,  103, 14, 96,  20,  39,  85,  56, 93,  57,
                       8,   60,  72, 45,  114, 0,   101, 21, 103, 84,
                       39,  66,  44, 27,  122, 77,  36,  20, 122, 7};

  char input[70];
  int result[50];
  int correct = 0;

  printf("Input FLAG : ");
  scanf("%s", input);

  if (strlen(input) != 49) {
    puts("Incorrect FLAG.");
    return 1;
  }

  for (int i = 0; i < 49; i++) {
    result[i] = (input[i] ^ key[i]) ^ key[i + 1];
    if (result[i] == 0) {
      correct++;
    }
  }

  if (correct == 49) {
    printf("Correct! FLAG is %s.\n", input);
  } else {
    puts("Incorrect FLAG.");
    return 1;
  }

  return 0;
}
