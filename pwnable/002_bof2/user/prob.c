#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <stdint.h>
#include <string.h>

void init() {
        setvbuf(stdin, 0, 2, 0);
        setvbuf(stdout, 0, 2, 0);
}

int main() {
        char user_input[0x40];
        int loop = 1;
        int IsNotSafe = 0;
        int64_t size = sizeof(user_input);

        init();
        memset(user_input, 0, size);

        while (loop) {
                printf("Input: ");
                read(0, user_input, size+1);

                printf("Your Input: %s", user_input);
        }

        if (IsNotSafe) {
                system("/bin/sh");
        }

        exit(0);
}