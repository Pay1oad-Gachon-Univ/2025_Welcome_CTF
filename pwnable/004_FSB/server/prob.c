//gcc -o prob prob.c -no-pie -Wl,-z,norelro -fcf-protection=none

#include <stdio.h>
#include <string.h>
#include <unistd.h>

void Initalize(){
   setvbuf(stdin, (char *)NULL, _IONBF, 0);
   setvbuf(stdout, (char *)NULL, _IONBF, 0);
   setvbuf(stderr, (char *)NULL, _IONBF, 0);
}

void print_menu(){
    puts("1. Write text.");
    puts("2. Display text.");
    puts("3. Close the book.");
    printf(">> ");
}

void win() {
    char *cmd = "/bin/sh";
    char *args[] = {cmd, NULL};
    execve(cmd, args, NULL);
}

int main(){
    Initalize();

    char page[256];

    int n;

    while(1){
        print_menu();

        scanf("%d", &n);  
        if(n == 1){
            printf("Input: ");
            read(0, page, 0x200);
        }
        else if(n == 2){
            printf("Text: ");
            printf(page);
            memset(page, 0, sizeof(page));
        }
        else if(n == 3){
            break;
        }
        else{
            puts("You have entered an invalid number.");
        }
    }

    return 0;
}
