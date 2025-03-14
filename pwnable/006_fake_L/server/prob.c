#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_LEN 16

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

void vulnerable() {
    char buffer[MAX_LEN];
    int length = 0;

    printf("Enter your input: ");
    gets(buffer);
    // 실제 문자열 길이 저장 (개행 문자 제거)
    length = strlen(buffer);

    // 길이 검사
    if (length > MAX_LEN) {
        printf("ACCESS DENIED!\n");
        abort();
//return;
    }

    printf("ACCESS GRANTED: %s\n", buffer);
    printf("DEBUG: length = %d\n", length);
}

int main() {
	init();
    setbuf(stdout, NULL);
    vulnerable();
    return 0;
}