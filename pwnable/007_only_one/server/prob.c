#include <stdio.h>
void init() {
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
}
void flag() {
    char flag[64];
    FILE *fp = fopen("flag.txt", "r");
    if (fp == NULL) {
        printf("Error: flag.txt not found!\n");
        exit(1);
    }
    fgets(flag, sizeof(flag), fp);
    fclose(fp);
    printf("FLAG: %s\n", flag);
}
int main(void) {
		init();
    int num;
    printf("num? ");
    scanf("%d", &num);
    if (num < 0)
        num = -num;
    if (num < 0)
    {
        printf("Success!\n");
  flag();
    }
    else
        printf("Fail!\n");
    return 0;
}