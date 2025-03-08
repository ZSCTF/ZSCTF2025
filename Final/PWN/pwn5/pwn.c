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
    puts("This time, no backdoor!!!");
    puts("What do you plan to do?");
}

int main(int argc, char *argv[])
{
    init();
    welcome();

    char buf[100];
    read(0, buf, 300);
    if (strlen(buf) > 100)
    {
        exit(0);
    }
    return 0;
}
