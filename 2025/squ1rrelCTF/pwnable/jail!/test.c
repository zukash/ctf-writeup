#include <unistd.h>

void main() {
//    execve("/bin/sh", NULL, NULL);
   execve("sh", NULL, NULL);
}