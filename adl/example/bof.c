#include <stdio.h>

/* compiled with -z execstack -fno-stack-protector */

int main(){
	char buf[100];
	setbuf(stdout, NULL);
	printf("%p\n", buf);
	gets(buf);
	return 0;
}