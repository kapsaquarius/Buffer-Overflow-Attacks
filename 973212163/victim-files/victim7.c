#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "util-program.h"

#define BUF_SIZE 388

void elder_wand(int argc, char *input_str)
{
    char* buf_ptr = NULL;
    int key = argc;
    
    char buf[BUF_SIZE];
    buf_ptr = buf;
    initialize_buffer(buf, BUF_SIZE);
    puts("Congratulations. There is a new owner of the Elder Wand\n"); 
    printf("\nYour Name is :-\n");
    sprintf(buf_ptr, "%s", input_str);
    buf_ptr += strlen(input_str);
    key += 1;

    return;
}

int main(int argc, char **argv)
{
    if (argc < 2) {
        printf("These are not the arguments you are looking for!\n"); 
        exit(0);
    }
    printf("Its time for you to wield the Elder Wand!\n");
    char *str;
    read_from_file(argv[1], &str);
    elder_wand(argc, str);
    return 0;
}
