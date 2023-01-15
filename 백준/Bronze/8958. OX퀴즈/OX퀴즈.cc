#include <stdio.h>
#include <string.h>

int main(void) {
    
    int input, score, sum;
    char arr[80];

    scanf("%d", &input);

    for(int i = 0; i < input; i++) {
        sum = 0;
        score = 1;
        scanf("%s", arr);
        
        for(int j = 0; j < strlen(arr); j++) {
            if(arr[j] == 'O') {
                sum += score;
                score++;
            }
            if(arr[j] == 'X')  
				score = 1;
        } 
        printf("%d\n", sum);
    }
}