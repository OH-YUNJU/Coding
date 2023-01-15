#include <stdio.h>

void max(int num1, int num2) {
	for(int result = num1; result; result--) {
		if(num1 % result == 0 && num2 % result == 0) {
			printf("%d", result);
			break;
		}
	}
}

void min(int num1, int num2) {
	for(int result = num1; result; result++) {
		if(result % num1 == 0 && result % num2 == 0) {
			printf("%d", result);
			break;
		}
	}
}

int main() {
	
	int num1, num2;
	
	scanf("%d %d", &num1, &num2);
	max(num1, num2);
	printf("\n");
	min(num1, num2);
	
}