#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <time.h>
#include <unistd.h>

bool is_prime(uint8_t n) {
  if (n < 2)
    return false;
  for (uint8_t i = 2; i * i <= n; i++) {
    if (n % i == 0)
      return false;
  }
  return true;
}

int main() {
  uint8_t *shellcode = (uint8_t *)0x100000000;
  uint8_t *max_map = (uint8_t *)0xffffffff000;

  srand(time(NULL));

  size_t max_off = (max_map - shellcode) / 0x1000;
  size_t add_off = (rand() % max_off) * 0x1000;
  shellcode += add_off;

  if (mmap(shellcode, 0x1000, PROT_READ | PROT_WRITE,
           MAP_FIXED | MAP_ANONYMOUS | MAP_PRIVATE, -1, 0) == MAP_FAILED) {
    perror("mmap failed");
    exit(EXIT_FAILURE);
  }

  printf("Please provide 0x1000 bytes of input:\n");
  if (read(STDIN_FILENO, shellcode, 0x1000) < 0) {
    perror("read failed");
    exit(EXIT_FAILURE);
  }

  for (int i = 0; i < 0x1000; i++) {
    if (!is_prime(shellcode[i])) {
      printf("Input is not all prime numbers.\n");
      exit(EXIT_FAILURE);
    }
  }

  printf("All input bytes are prime numbers.\n");

  if (mprotect(shellcode, 0x1000, PROT_READ | PROT_WRITE | PROT_EXEC) != 0) {
    perror("mprotect failed");
    exit(EXIT_FAILURE);
  }

  memcpy(shellcode, "\x48\x31\xd2", 3);
  void (*shell)() = (void (*)())shellcode;
  asm volatile("xor %%rax, %%rax;"
               "xor %%rbx, %%rbx;"
               "xor %%rcx, %%rcx;"
               "xor %%rdx, %%rdx;"
               "xor %%rsi, %%rsi;"
               "xor %%rdi, %%rdi;"
               "xor %%r8,  %%r8 ;"
               "xor %%r9,  %%r9 ;"
               "xor %%r10, %%r10;"
               "xor %%r11, %%r11;"
               "xor %%r12, %%r12;"
               "xor %%r13, %%r13;"
               "xor %%r14, %%r14;"
               "xor %%r15, %%r15;" ::
                   : "rax", "rbx", "rcx", "rdx", "rsi", "rdi", "r8", "r9",
                     "r10", "r11", "r12", "r13", "r14", "r15");
  shell();

  return 0;
}
