#include <stdio.h>
#include <stdlib.h>
 
int main() {
    int N, K;
    scanf("%d %d", &N, &K);
 
    int* coin = (int*)malloc(sizeof(int) * N);
    for (int i = N-1; i >= 0; i--)
        scanf("%d", &coin[i]);
 
    int cnt = 0, idx = 0;
    while (K > 0) {
        if (K >= coin[idx]) {
            K -= coin[idx];
            cnt++;
        }
        else idx++;
    }
 
    printf("%d\n", cnt);
    free(coin);
    return 0;
}
