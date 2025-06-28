#include "out.h"

undefined1 *get_card_name(undefined1 param_1)

{
  switch (param_1) {
    default:
      name_0._0_5_ = 0x6f6e6b6e55;
      name_0._5_2_ = 0x6e77;
      name_0[7] = 0;
      break;
    case 1:
      name_0._0_5_ = 0x2820656341;
      name_0._5_2_ = 0x2931;
      name_0[7] = 0;
      break;
    case 2:
      name_0._0_5_ = 0x28206f7754;
      name_0._5_2_ = 0x2932;
      name_0[7] = 0;
      break;
    case 3:
      name_0._0_5_ = 0x6565726854;
      name_0._5_2_ = 0x2820;
      name_0[7] = 0x33;
      name_0[8] = 0x29;
      name_0[9] = 0;
      break;
    case 4:
      name_0._0_5_ = 0x2072756f46;
      name_0._5_2_ = 0x3428;
      name_0[7] = 0x29;
      name_0[8] = 0;
      break;
    case 5:
      name_0._0_5_ = 0x2065766946;
      name_0._5_2_ = 0x3528;
      name_0[7] = 0x29;
      name_0[8] = 0;
      break;
    case 6:
      name_0._0_5_ = 0x2820786953;
      name_0._5_2_ = 0x2936;
      name_0[7] = 0;
      break;
    case 7:
      name_0._0_5_ = 0x6e65766553;
      name_0._5_2_ = 0x2820;
      name_0[7] = 0x37;
      name_0[8] = 0x29;
      name_0[9] = 0;
      break;
    case 8:
      name_0._0_5_ = 0x7468676945;
      name_0._5_2_ = 0x2820;
      name_0[7] = 0x38;
      name_0[8] = 0x29;
      name_0[9] = 0;
      break;
    case 9:
      name_0._0_5_ = 0x20656e694e;
      name_0._5_2_ = 0x3928;
      name_0[7] = 0x29;
      name_0[8] = 0;
      break;
    case 10:
      name_0._0_5_ = 0x28206e6554;
      name_0._5_2_ = 0x3031;
      name_0[7] = 0x29;
      name_0[8] = 0;
      break;
    case 0xb:
      name_0._0_5_ = 0x206b63614a;
      name_0._5_2_ = 0x3128;
      name_0[7] = 0x30;
      name_0[8] = 0x29;
      name_0[9] = 0;
      break;
    case 0xc:
      name_0._0_5_ = 0x6e65657551;
      name_0._5_2_ = 0x2820;
      name_0[7] = 0x31;
      name_0[8] = 0x30;
      name_0[9] = 0x29;
      name_0[10] = 0;
      break;
    case 0xd:
      name_0._0_5_ = 0x20676e694b;
      name_0._5_2_ = 0x3128;
      name_0[7] = 0x30;
      name_0[8] = 0x29;
      name_0[9] = 0;
      break;
    case 0xe:
      name_0._0_5_ = 0x72656b6f4a;
      name_0._5_2_ = 0x2820;
      name_0[7] = 0x31;
      name_0[8] = 0x30;
      name_0[9] = 0x29;
      name_0[10] = 0;
      break;
    case 0xf:
      name_0._0_5_ = 0x6963657053;
      name_0._5_2_ = 0x6c61;
      name_0[7] = 0x20;
      name_0[8] = 0x28;
      name_0[9] = 0x31;
      name_0[10] = 0x30;
      name_0._11_2_ = 0x29;
  }
  return name_0;
}

byte get_card_value(byte param_1)

{
  if (param_1 == 1) {
    param_1 = 0xb;
  } else if (9 < param_1) {
    param_1 = 10;
  }
  return param_1;
}

byte get_card(long param_1, uint param_2)

{
  byte bVar1;

  bVar1 = *(byte *)(param_1 + (int)param_2 / 2);
  if ((param_2 & 1) == 0) {
    bVar1 = bVar1 & 0xf;
  } else {
    bVar1 = bVar1 >> 4;
  }
  return bVar1;
}

void set_card(long param_1, uint param_2, byte param_3)

{
  int iVar1;

  iVar1 = (int)param_2 / 2;
  if ((param_2 & 1) == 0) {
    *(byte *)(param_1 + iVar1) =
        *(byte *)(param_1 + iVar1) & 0xf0 | param_3 & 0xf;
  } else {
    *(byte *)(param_1 + iVar1) =
        *(byte *)(param_1 + iVar1) & 0xf | (param_3 & 0xf) << 4;
  }
  return;
}

int draw_card(void)

{
  int iVar1;

  iVar1 = FUN_001011d0();
  return iVar1 % 0xf + 1;
}

void view_card(void)

{
  byte bVar1;
  int iVar2;
  undefined8 uVar3;
  long in_FS_OFFSET;
  int local_2c;
  undefined1 *local_28;
  long local_20;

  local_20 = *(long *)(in_FS_OFFSET + 0x28);
  printf("Which card to view? ");
  iVar2 = __isoc99_scanf(&DAT_0010205d, &local_2c);
  if (iVar2 == 1) {
    local_2c = local_2c + -1;
    if (local_2c < 3) {
      local_28 = &DAT_001040e8;
      bVar1 = get_card(&DAT_001040e8, local_2c);
      uVar3 = get_card_name(bVar1);
      printf("Card #%d: %s (0x%X)\n", (ulong)(local_2c + 1), uVar3,
             (ulong)bVar1);
    } else {
      puts("Not your card!");
    }
  } else {
    puts("Invalid input!");
    do {
      iVar2 = getchar();
    } while (iVar2 != 10);
  }
  if (local_20 == *(long *)(in_FS_OFFSET + 0x28)) {
    return;
  }
  // WARNING: Subroutine does not return
  __stack_chk_fail();
}

void replace_card(void)

{
  byte bVar1;
  int iVar2;
  undefined8 uVar3;
  long in_FS_OFFSET;
  int local_2c;
  undefined1 *local_28;
  long local_20;

  local_20 = *(long *)(in_FS_OFFSET + 0x28);
  printf("Which card index to replace? ");
  iVar2 = __isoc99_scanf(&DAT_0010205d, &local_2c);
  if (iVar2 == 1) {
    local_2c = local_2c + -1;
    if (local_2c < 3) {
      bVar1 = draw_card();
      local_28 = &DAT_001040e8;
      uVar3 = get_card_name(bVar1);
      printf("Drew new card: %s (0x%X)\n", uVar3, (ulong)bVar1);
      set_card(local_28, local_2c, bVar1);
      puts("Card replaced!");
    } else {
      puts("Not your card!");
    }
  } else {
    puts("Invalid input!");
    do {
      iVar2 = getchar();
    } while (iVar2 != 10);
  }
  if (local_20 == *(long *)(in_FS_OFFSET + 0x28)) {
    return;
  }
  // WARNING: Subroutine does not return
  __stack_chk_fail();
}

void play_blackjack(void)

{
  bool bVar1;
  byte bVar2;
  byte bVar3;
  byte bVar4;
  byte bVar5;
  int iVar6;
  int iVar7;
  undefined8 uVar8;
  undefined8 uVar9;
  long in_FS_OFFSET;
  int local_3c;
  uint local_38;
  uint local_34;
  long local_30;

  local_30 = *(long *)(in_FS_OFFSET + 0x28);
  bVar2 = draw_card();
  bVar3 = draw_card();
  bVar4 = draw_card();
  bVar5 = draw_card();
  DAT_001040e8 = bVar2 | bVar3 << 4;
  printf("\nWelcome to Blackjack, %s!\n", &DAT_001040a8);
  printf("Your balance: $%d\n", (ulong)player);
  puts("\nYour cards:");
  uVar8 = get_card_name(bVar2);
  printf("Card 1: %s (0x%X)\n", uVar8, (ulong)bVar2);
  uVar8 = get_card_name(bVar3);
  printf("Card 2: %s (0x%X)\n", uVar8, (ulong)bVar3);
  uVar8 = get_card_name(bVar4);
  printf("Dealer\'s face-up card: %s (0x%X)\n", uVar8, (ulong)bVar4);
  bVar1 = true;
  do {
    puts("\nOptions:");
    puts("1. View a card");
    if (bVar1) {
      puts("2. Replace a card (once per game)");
    }
    puts("3. Stand (end your turn)");
    puts("4. Exit game");
    printf("Choose an option: ");
    iVar6 = __isoc99_scanf(&DAT_0010205d, &local_3c);
    if (iVar6 == 1) {
      if (local_3c == 4) {
      LAB_00101c40:
        if (local_30 == *(long *)(in_FS_OFFSET + 0x28)) {
          return;
        }
        // WARNING: Subroutine does not return
        __stack_chk_fail();
      }
      if (local_3c < 5) {
        if (local_3c == 3) {
          uVar8 = get_card_name(bVar5);
          uVar9 = get_card_name(bVar4);
          printf("\nDealer\'s cards: %s (0x%X) and %s (0x%X)\n", uVar9,
                 (ulong)bVar4, uVar8, (ulong)bVar5);
          bVar2 = DAT_001040e8 & 0xf;
          bVar3 = DAT_001040e8 >> 4;
          iVar6 = get_card_value(bVar2);
          iVar7 = get_card_value(bVar3);
          local_38 = iVar7 + iVar6;
          iVar6 = get_card_value(bVar4);
          iVar7 = get_card_value(bVar5);
          local_34 = iVar7 + iVar6;
          if ((0x15 < (int)local_38) && ((bVar2 == 1 || (bVar3 == 1)))) {
            local_38 = local_38 - 10;
          }
          if ((0x15 < (int)local_34) && ((bVar4 == 1 || (bVar5 == 1)))) {
            local_34 = local_34 - 10;
          }
          printf("Your total: %d\n", (ulong)local_38);
          printf("Dealer\'s total: %d\n", (ulong)local_34);
          if ((int)local_38 < 0x16) {
            if ((int)local_34 < 0x16) {
              if ((int)local_34 < (int)local_38) {
                puts("You win!");
                player = player + 0x14;
                DAT_001040a4 = DAT_001040a4 + 1;
              } else if ((int)local_38 < (int)local_34) {
                puts("Dealer wins.");
                player = player - 10;
              } else {
                puts("It\'s a tie!");
              }
            } else {
              puts("Dealer busts! You win!");
              player = player + 0x14;
              DAT_001040a4 = DAT_001040a4 + 1;
            }
          } else {
            puts("You bust! Dealer wins.");
            player = player - 10;
          }
        } else {
          if (3 < local_3c) goto LAB_00101c1a;
          if (local_3c == 1) {
            view_card();
          } else {
            if (local_3c != 2) goto LAB_00101c1a;
            if (bVar1) {
              replace_card();
              bVar1 = false;
            } else {
              puts("You\'ve already replaced a card this game!");
            }
          }
        }
      } else {
      LAB_00101c1a:
        puts("Invalid option!");
      }
    } else {
      puts("Invalid input!");
      do {
        iVar6 = getchar();
      } while (iVar6 != 10);
    }
    if ((local_3c == 3) || (local_3c == 4)) goto LAB_00101c40;
  } while (true);
}

void show_balance(void)

{
  printf("Current balance: $%d\n", (ulong)player);
  printf("Win count: %d\n", (ulong)DAT_001040a4);
  return;
}

void initialize_game(void)

{
  char *pcVar1;
  size_t sVar2;

  player = 100;
  DAT_001040a4 = 0;
  printf("Enter your name: ");
  pcVar1 = fgets(&DAT_001040a8, 0x40, stdin);
  if (pcVar1 != (char *)0x0) {
    sVar2 = strcspn(&DAT_001040a8, "\n");
    (&DAT_001040a8)[sVar2] = 0;
  }
  return;
}

undefined8 main(void)

{
  int iVar1;
  time_t tVar2;
  long in_FS_OFFSET;
  int local_3c;
  __time_t local_38;
  tm *local_30;
  timeval local_28;
  long local_10;

  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  setbuf(stdout, (char *)0x0);
  setbuf(stdin, (char *)0x0);
  tVar2 = time((time_t *)0x0);
  srand((uint)tVar2);
  initialize_game();
  do {
    while (true) {
      while (true) {
        puts("\n=== Squ1rrel Casino Menu ===");
        puts("1. Play Blackjack");
        puts("2. Show Balance");
        puts("3. Exit");
        printf("Choose an option: ");
        iVar1 = __isoc99_scanf(&DAT_0010205d, &local_3c);
        if (iVar1 == 1) break;
        puts("Invalid input!");
        do {
          iVar1 = getchar();
        } while (iVar1 != 10);
      }
      do {
        iVar1 = getchar();
      } while (iVar1 != 10);
      if (local_3c == 3) {
        puts("Thanks for playing at the Squ1rrel Casino!");
        gettimeofday(&local_28, (__timezone_ptr_t)0x0);
        local_38 = local_28.tv_sec;
        local_30 = localtime(&local_38);
        printf("But it\'s only %02d:%02d! Surely you can stay longer?\n",
               (ulong)(uint)local_30->tm_hour, (ulong)(uint)local_30->tm_min);
        if (local_10 == *(long *)(in_FS_OFFSET + 0x28)) {
          return 0;
        }
        // WARNING: Subroutine does not return
        __stack_chk_fail();
      }
      if (local_3c < 4) break;
    LAB_00101ec4:
      puts("Invalid option!");
    }
    if (local_3c == 1) {
      play_blackjack();
    } else {
      if (local_3c != 2) goto LAB_00101ec4;
      show_balance();
    }
  } while (true);
}
