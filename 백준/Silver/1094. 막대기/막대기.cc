#include <stdio.h>

int main() {
	int stick = 64;
	int cm;
	int num = 0;
	
	scanf("%d", &cm);
	
	while(cm > 0) {
		if(stick > cm)
			stick = stick / 2;
		else {
			cm = cm - stick;
			num++;
		}			
	}
	
	printf("%d", num);
}