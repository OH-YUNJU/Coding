#include <stdio.h>

int main(){
	int arr[1000001] = {0, 1};
	int n, m;
	
	scanf("%d %d", &n, &m);
	
	for(int i = 2; i <= m; i++) {
		for(int j = 2; j*i <= m; j++) {
			arr[i*j] = 1;
		}
	}
	
	for(int k = n; k <= m; k++) {
		if(!arr[k])
			printf("%d\n", k);
	}

}