#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <string.h>

char bsh[10];

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

void shell()
{
    puts("you get it");
    execve(bsh, 0, 0);
}

void cal()
{
    char your_answer[100];
    srand(time(NULL));
    int num1, num2, correct_answer;
    int op;
    for (int idx = 1;; ++idx)
    {
        num1 = rand() % 100;
        num2 = rand() % 100;
        op = rand() % 2;

        if (op == 0)
        {
            printf("%d + %d = ", num1, num2);
            correct_answer = num1 + num2;
        }
        else
        {
            printf("%d - %d = ", num1, num2);
            correct_answer = num1 - num2;
        }

        read(0, your_answer, 100);
        if (strlen(your_answer) < 4)
        {
            if (atoi(your_answer) == correct_answer)
            {
                puts("Correct!");
            }
            else
            {
                puts("Wrong!");
                exit(0);
            }

            if (idx % 100 == 0)
            {
                puts("You have successfully completed 100 addition and subtraction calculation questions.");
                exit(0);
            }
        }
        else
        {
            break;
        }
    }

    puts("You are so smart, I will give you a gift.");
    printf("backdoor address: %p\n", &shell);
    read(0, your_answer, 200);

    sprintf(bsh, "%s%s", "/bin", "/sh");
}

int main(int argc, char *argv[])
{
    init();
    welcome();

    cal();

    return 0;
}