int32_t main(int32_t argc, char** argv, char** envp) {
  signal(0xb, win);
  setbuf(__TMC_END__, nullptr);
  printf("Enter number of rows: ");
  int64_t var_38;
  __isoc99_scanf("%llu", &var_38);
  printf("Enter number of cols: ");
  int64_t var_40;
  __isoc99_scanf("%llu", &var_40);

  if ((var_38 * var_40) < var_38) {
    puts("Don't hack!");
    exit(1);
    /* no return */
  }

  void* rax_8 = malloc((var_40 * var_38));

  if (rax_8 == 0) {
    puts("Too large!");
    exit(1);
    /* no return */
  }

  for (int64_t i = 0; i < var_38; i += 1) {
    for (int64_t j = 0; j < var_40; j += 1)
      *(rax_8 + ((var_40 * i) + j)) = ((j + i) & 1);
  }

  puts("I made Ichimatsu design for you!");

  for (int64_t i_1 = 0; i_1 < var_38; i_1 += 1) {
    for (int64_t j_1 = 0; j_1 < var_40; j_1 += 1)
      printf(&data_2091, *(rax_8 + ((var_40 * i_1) + j_1)));

    puts(&data_2095);
  }

  return 0;
}