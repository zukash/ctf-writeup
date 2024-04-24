int __fastcall main(int argc, const char **argv, const char **envp)
{
  char *v3; // rbx
  size_t v4; // rax
  int v5; // ebp
  int v6; // r12d
  char *v7; // r15
  char s[568]; // [rsp+10h] [rbp-238h] BYREF

  v3 = s;
  setbuf(stdout, 0LL);
  puts("hi, i'm aplet321. how can i help?");
  fgets(s, 512, stdin);
  v4 = strlen(s);
  if ( v4 <= 5 )
    goto LABEL_10;
  v5 = 0;
  v6 = 0;
  v7 = &s[(unsigned int)(v4 - 6) + 1];
  do
  {
    v6 += strncmp(v3, "pretty", 6uLL) == 0;
    v5 += strncmp(v3++, "please", 6uLL) == 0;
  }
  while ( v3 != v7 );
  if ( v5 )
  {
    if ( strstr(s, "flag") )
    {
      if ( v6 + v5 == 54 && v6 - v5 == -24 )
      {
        puts("ok here's your flag");
        system("cat flag.txt");
      }
      else
      {
        puts("sorry, i'm not allowed to do that");
      }
    }
    else
    {
      puts("sorry, i didn't understand what you mean");
    }
  }
  else
  {
LABEL_10:
    puts("so rude");
  }
  return 0;
}
