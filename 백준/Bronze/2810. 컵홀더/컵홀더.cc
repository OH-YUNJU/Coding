#include <stdio.h>

int main() {
	
	char chair[51];
	int peo, cup;
	
	scanf("%d", &peo);
	scanf("%s", &chair);
	
	cup = peo + 1;
	
	for(int i = 0; i < peo; i++) {
		if(chair[i] == 'L') {
			cup--;
      		i++;
      	}
  	}

  	if(cup > peo) 
	  cup = peo;
  	
	printf("%d\n", cup);
  
}