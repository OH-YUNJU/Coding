#include <stdio.h>

int main() {
	
	int num, tmp = 0;
	
	scanf("%d", &num);
	
	while (num - 1 > tmp * 6)
		num = num - 6 * tmp++;
		
	printf("%d\n", ++tmp);
	
	return 0;
}