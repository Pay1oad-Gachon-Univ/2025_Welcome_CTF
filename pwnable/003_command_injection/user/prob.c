
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

void init() {
        setvbuf(stdin, 0, 2, 0);
        setvbuf(stdout, 0, 2, 0);
}

int main() {
        char cmd[256] = "ifconfig";
        char name[24];

        init();

        printf("What is your name? : ");
        read(0, name, 100);
        printf("This is your cmd, %s.", name);

        if( !strncmp(cmd, "ifconfig", 8)) {
                system(cmd);
        } else {
                printf("You can't do that!");
        }

        exit(0);
}