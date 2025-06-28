void prison(void)

{
  int iVar1;
  char *local_88[4];
  char *local_68;
  char *local_60;
  uint local_4c;
  char local_48[64];

  local_88[0] = "The Professor";
  local_88[1] = "Empty Cell";
  local_88[2] = "Jay. L. Thyme";
  local_88[3] = "Jay. L. Thyme\'s Wife";
  local_68 = "Jay. L. Thyme\'s Wife\'s Boyfriend";
  local_60 = "Rob Banks";
  printf(
      "They gave you the premium stay so at least you get to choose your cell "
      "(1-6): ");
  iVar1 = __isoc99_scanf("%d", &local_4c);
  if (iVar1 == 1) {
    do {
      iVar1 = getchar();
    } while (iVar1 != 10);
    printf("Cell #%d: Your cellmate is %s\n", (ulong)local_4c,
           local_88[(int)(local_4c - 1)]);
    printf("Now let\'s get the registry updated. What is your nam e: ");
    fgets(local_48, 100, (FILE *)stdin);
    puts("...");
    sleep(3);
    puts("...");
    puts(
        "What did you expect. You\'re in here for life this is what  it looks "
        "like for the rest.");
  } else {
    puts("Invalid input!");
    do {
      iVar1 = getchar();
    } while (iVar1 != 10);
  }
  return;
}

undefined8 main(void)

{
  setbuf((FILE *)stdout, (char *)0x0);
  setbuf((FILE *)stdin, (char *)0x0);
  puts("Welcome to Maximum Security Prison.");
  puts("You\'ll be rotting in here for the rest of your life!");
  puts("But first let\'s get you registered and take you to your c ell.");
  prison();
  return 0;
}