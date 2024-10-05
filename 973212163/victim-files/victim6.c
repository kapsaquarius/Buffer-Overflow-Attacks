#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "util-program.h"

struct orb {
    void (*orb)();
};

struct wizard {
    char name[471];
};

void no_prophecy()
{
    printf("You couldn't find the prophecy, young Wizard! Try again.\n");
    return;
}

void prophecy()
{
    printf("You are the chosen one. Well done !!!\n");
    return;
}

int main(int argc, char **argv)
{
    if (argc < 2) {
        printf("These are not the arguments you are looking for!\n"); 
        exit(0);
    }

    struct wizard *wiz;
    struct orb *orb_ptr;
    wiz = malloc(sizeof(struct wizard));
    orb_ptr = malloc(sizeof(struct orb));
    orb_ptr->orb = no_prophecy;
    char *str;
    read_from_file(argv[1], &str);
    strcpy(wiz->name, str);
    orb_ptr->orb();

    return 0;
}
