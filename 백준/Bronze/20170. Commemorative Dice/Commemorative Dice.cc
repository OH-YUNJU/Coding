#include <cstdio>

int dice_A[6], dice_B[6];

int gcd(int a, int b)
{
    return b ? gcd(b, a % b) : a;
}
int main()
{
    int numerator = 0, denominator = 36, _gcd;

    for (int i = 0; i < 6; i++)
        scanf("%d", &dice_A[i]);
    for (int i = 0; i < 6; i++)
        scanf("%d", &dice_B[i]);

    for (int i = 0; i < 6; i++)
        for (int j = 0; j < 6; j++)
            if (dice_A[i] > dice_B[j])
                numerator++;

    _gcd = gcd(denominator, numerator);

    printf("%d/%d", numerator / _gcd, denominator / _gcd);
    return 0;
}