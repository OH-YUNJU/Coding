#include <stdio.h>

int main() {
	int n, tmp;
	int num[1000] = {0 };
	
	scanf("%d", &n);
	
	for(int i = 0; i < n; i++) {
		scanf("%d", &num[i]);
	}
	
	for(int i = 0; i < n; i++) {
		for (int j = 0; j < n-1; j++) {
			if (num[j] < num[j+1]) {
				tmp = num[j+1];
				num[j+1] = num[j];
				num[j] = tmp;
			}
		}
	}
	
	for(int i = n - 1; i > -1; i--) {
		printf("%d\n", num[i]);
	}
}