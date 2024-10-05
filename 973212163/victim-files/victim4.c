#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "util-program.h"

#define BUF_SIZE 520
#define STACK_COOKIE 0xDEAD2BAD

void buckbeak(){
    printf("Well done. You helped Sirius safely escape! \n");
    exit(0);
    return;
}

void hogwarts(int argc, char* input_str){
    unsigned long int cookie = STACK_COOKIE;
    char* buf_ptr = NULL;
    int key = argc;
    
    char buf[BUF_SIZE];
    buf_ptr = buf;
    initialize_buffer(buf, BUF_SIZE);

    sscanf(input_str, "%s", buf_ptr);
    buf_ptr += strlen(input_str);
    key += 1;

    if (cookie != STACK_COOKIE) {
        printf("Stack overflow detected.\n");
        exit(1);
    }
    return;
}

int main(int argc, char **argv){

    if ( argc < 2 ) {
        printf("These are not the arguments you are looking for!\n"); 
        exit(0);
    }
    printf("Help Sirius Black escape without being caught by the Dementors.\n");
    char *str;
    read_from_file(argv[1], &str);
    hogwarts(argc, str);
    printf("Oh no! The dementors found you. Try once again.\n");
    return 0;
}