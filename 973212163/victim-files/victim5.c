#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "util-program.h"

#define BUF_SIZE 298
#define STACK_COOKIE 0xDEAD2BAD

void round_1()
{
    unsigned long int cookie = STACK_COOKIE;
    printf("Hurray! You slayed the dragon and found a golden egg!\n");
    int id = (rand() % 19000); 
    printf("Round Code = %d\n\n", id);

    if (cookie != STACK_COOKIE) {
        printf("Stack overflow detected.\n");
        exit(1);
    }

    return;
}

void round_2()
{
    unsigned long int cookie = STACK_COOKIE;
    printf("Well Done! You rescued your friend from the lake!\n");
    int id = (rand() % 19000); 
    printf("Round Code = %d\n\n", id);

    if (cookie != STACK_COOKIE) {
        printf("Stack overflow detected.\n");
        exit(1);
    }

    return;
}

void round_3()
{
    unsigned long int cookie = STACK_COOKIE;
    printf("Excellent! You completed the maze and found your ultimate champion cup!\n");
    printf("Congratulations on winning the Triwizard tournament!\n");
    int id = (rand() % 19000); 
    printf("Round Code = %d\n\n", id);

    if (cookie != STACK_COOKIE) {
        printf("Stack overflow detected.\n");
        exit(1);
    }

    return;
}

int tournament(int argc, char* input_str)
{
    unsigned long int cookie = STACK_COOKIE;
    char* buf_ptr = NULL;

    char buf[BUF_SIZE];
    buf_ptr = buf;
    initialize_buffer(buf, BUF_SIZE);

    sscanf(input_str, "%s", buf_ptr);
    buf_ptr += strlen(input_str);
    
    if (cookie != STACK_COOKIE) {
        printf("Stack overflow detected.\n");
        exit(1);
    }

    return 0;
}

int main(int argc, char **argv)
{
    if (argc < 2) {
        printf("These are not the arguments you are looking for!\n"); 
        exit(0);
    }
    printf("Welcome to the Triwizard Tournament.\n");
    char *str;
    read_from_file(argv[1], &str);
    tournament(argc, str);
    return 0;
}