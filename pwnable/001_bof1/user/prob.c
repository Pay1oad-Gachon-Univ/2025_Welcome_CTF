#include <stdio.h>
#include <unistd.h>

void init() {
	setvbuf(stdin, 0, 2, 0);
	setvbuf(stdout, 0, 2, 0);
}

void get_shell() {
	system("/bin/sh");
}

int main() {
  char buf[0x20];
  
  init();
  
  printf("Input: ");
  scanf("%s", buf);
  
  return 0;
}