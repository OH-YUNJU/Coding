#include <stdio.h>

int main(void) {
    int self[15000];
    
    for(int i=0; i<15000; i++) self[i] = i+1;
    
    for(int i=0; i<10000; i++) {
        int m = i+1;
        int tmp = m;
        int a = 0, b = 0, result = 0;
        double c = 0;
        while(1) {
            a = m % 10;
            b += a;
            c = (double)m / 10;
            if(c < 10) {
                if(tmp >= 10) result = tmp + b + (int)c;
                if(tmp < 10) result = tmp + b + (int)c*10;
                self[result-1] = 0;
                break;
        }
            m = (int)c;
        }
    }
        for(int i=0; i<10000; i++) {
        if(self[i] != 0) printf("%d\n", i+1);
    }
}