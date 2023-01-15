#include <stdio.h>

int main() {

	int tmp = 101;
	int num = 0;
	int result = 0;
	
	for(int i = 0; i < 7; i++) {
		scanf("%d", &num);

		if(num % 2 == 1) {
			result = result + num;

			if(num < tmp) {
				tmp = num;
			}
		}
	}
	
	if(result == 0) 
		printf("-1");
	
	else
		printf("%d\n%d", result, tmp);

}