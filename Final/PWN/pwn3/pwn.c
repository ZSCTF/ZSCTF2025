#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void init()
{
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

void welcome()
{
    puts("Welcome to the zsctf!");
    puts("Do you know overflows? (yes/no)");
}

int main(int argc, char *argv[])
{
    init();
    welcome();

    int real_choice[6];
    char fake_choice[32];

    read(0, fake_choice, 0x2c);
    if (!strcmp("yes", (const char *)real_choice))
    {
        puts("Nice choice!\n");
        system("/bin/sh");
    }
    else
    {
        if (!strcmp("yes", fake_choice))
        {
            puts("don't lie!!!\n");
        }
        else if (!strcmp("no", fake_choice))
        {
            puts("If you don't know, go and learn.\n");
        }
        else
        {
            puts("erroneous input.\n");
        }
    }

    return 0;
}
