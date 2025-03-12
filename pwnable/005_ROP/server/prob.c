// gcc -o prob prob.c -no-pie -fstack-protector-strong -z relro
#include <stdio.h>
#include <string.h>
#include <unistd.h>

void Initalize() {
    setvbuf(stdin, (char *)NULL, _IONBF, 0);
    setvbuf(stdout, (char *)NULL, _IONBF, 0);
    setvbuf(stderr, (char *)NULL, _IONBF, 0);
}

void view_cat(){
    puts("                            /|、");
    puts("                          (˚ˎ 。7  ");
    puts("                           |、˜〵          ");
    puts("                          じしˍ,)ノ");   
}

void showMenu() {
    puts("1. Feed");
    puts("2. Pet");
    puts("3. Play");
    puts("4. Give a treat");
    puts("5. Bathe");
    puts("Enter a number from 1 to 5 to choose an action.");
    puts("If you enter a number greater than 5, please try again with a valid option.");
    
}

int main() {
    char name[20];
    int age;
    char *actions[10] = {"Feed", "Pet", "Play", "Give a treat", "Bathe"};
    char buf[8];
    int num;

    Initalize();

    view_cat();

    printf("Enter your cat's name:");
    read(0, &name, 20);

    while (1) {
        showMenu();

        printf("Choose an action: ");
        scanf("%d", &num);

        switch (num) {
            case 0:
                break;
            case 1:
            case 2:
            case 3:
            case 4:
            case 5:
                printf("You %s %s\n", actions[num-1], name);
                break;
            default:
                if (num < 0 || num >= 11){
                    printf("There's an %llu here so we can't add it.\n", actions[num - 1]);
                }
                else{
                    printf("What actions would you like to add? :");
                    read(0, actions[num - 1], 20);
                    printf("You add %s\n", actions[num - 1]);
                }
                break;
        }

        if(num == 0){
            printf("You leave home.\n");
            printf("A word to the cat before you leave : ");
            read(0, buf, 0x100);
            break;
        }

        if (num == 5) {
            puts("Cat ran away under the couch");
            break;
        }
    }

    return 0;
}
