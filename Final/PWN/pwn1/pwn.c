#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

const int INPUT_SIZE = 0x10;
void init()
{
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

void welcome()
{
    printf("Welcome to the zsctf 2025!!!\n");
    printf("The list of documents is as follows: ");
    system("ls");
    printf("Now you have a chance to carry out the order.\n");
}

// 检查字符串是否包含字母
int checkInput(const char *str)
{
    while (*str)
    {
        if ((*str >= 'a' && *str <= 'z') || (*str >= 'A' && *str <= 'Z'))
        {
            return 1;
        }
        str++;
    }
    return 0;
}

int main(int argc, char *argv[])
{
    init();
    welcome();

    char buf[INPUT_SIZE];
    printf("what do you want: ");
    read(0, buf, INPUT_SIZE - 1);
    buf[INPUT_SIZE - 1] = '\0';

    // 检查是否包含字母
    if (checkInput(buf))
    {
        printf("Input contains letters. Exiting...\n");
        exit(0);
    }
    system(buf);

    return 0;
}