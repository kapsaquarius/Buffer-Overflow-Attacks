#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "util-program.h"

#define BUF_SIZE 70

void moaning_myrtle()
{
    printf("Go away Wizard. There is nothing here!\n");
    return;
}

void chamber()
{
    printf("You have opened the Chamber of Secrets. Well done!!\n");
    system("/bin/sh");
    return;
}

int open_chamber(int argc, char* input_str){

    char *buf_ptr = NULL;
    void (*functionPtr)() = moaning_myrtle;
    int key = argc;
    
    char buf[BUF_SIZE];
    buf_ptr = buf;
    initialize_buffer(buf, BUF_SIZE);

    sprintf(buf_ptr, "%s", input_str);
    buf_ptr += strlen(input_str);
    functionPtr();
    key += 1;

    return 0;
}

int main(int argc, char **argv){

    if (argc < 2) {
        printf("These are not the arguments you are looking for!\n"); 
        exit(0);
    }
    printf("This is Moaning Myrtle's bathroom.\n");
    char *str;
    read_from_file(argv[1], &str);
    open_chamber(argc, str);
    return 0;
}