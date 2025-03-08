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
}

int main(int argc, char *argv[])
{
    init();
    welcome();

    char code[30];
    read(0, code, 25);

    (*(void (*)())code)();

    return 0;
}
