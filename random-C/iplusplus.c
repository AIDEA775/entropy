#include<stdio.h>

void hola(int x, int y) {
	printf("%d %d", x, y);
}

void main() {
	int i = 0;
	hola(i, i++);
}
