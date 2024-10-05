#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "util-program.h"

#define BUF_SIZE 131

void get_wand(int key)
{
    if (key != (0xdeadbaba | get_sid())){
        printf("WRONG KEY for procuring your wand. Keep Trying.\n");
    } else {
        printf("Congratulations Young Wizard! You wield your first wand.\n");
        int id = (rand() % 19000); 
        printf("\nWand ID = %d\n", id);
    }

    return;
}


int enter_academy(int argc, char* input_str)
{
    char *buf_ptr = NULL;
    long long int a;
    long int b;
    short int c;
    int key = 0;
    char buf[BUF_SIZE];
    buf_ptr = buf;
    initialize_buffer(buf_ptr, BUF_SIZE);

    a = 0x41;
    b = 0x42;
    c = 0x42;
    key = argc;
    strcpy(buf_ptr, input_str);
    buf_ptr += strlen(input_str);

    printf("Task 1 :- Procure your wand, Wizard!\n");
    get_wand(key);

    c = a + b + c;
    b = a + b + c;
    a = a + b + c;

    return 0;
}

int main(int argc, char **argv)
{
    if (argc < 2) {
      printf("These are not the arguments you are looking for!\n"); 
      exit(1);
    }

    printf("Welcome to the Magical Academy - CSE543\n");
    char *str;
    read_from_file(argv[1], &str);
    enter_academy(argc, str);
    return 0;
}
