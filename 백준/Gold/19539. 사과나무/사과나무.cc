#include <stdio.h>

int main() {
	int arr[100000];
	int num;
	int two = 0, sum = 0;
	
	scanf("%d", &num);
	
	for(int i = 0; i < num; i++) {
		scanf("%d", &arr[i]);
		two += arr[i] / 2;
		sum = sum + arr[i];
	}
	
	if(two >= (sum/3) && sum % 3 == 0)
		printf("YES");
	
	else
		printf("NO");
}