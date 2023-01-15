#include <stdio.h>

#define N 9

void swap(int* a, int* b);
void SelectSort(int* ptr);

int main(void)
{
	int a[N], i, j, k, sum = 0;
	
	for (i = 0; i < N; i++)
	{
		scanf("%d", a + i);
		sum += a[i];
	}
	SelectSort(a);
	for (i = 0; i < N - 1; i++)
	for (j = 1; j < N; j++)
	{
		if (j != i)
		if (sum - a[i] - a[j] == 100)
			goto here;
	}
here:
	for (k = 0; k < 9; k++)
	if (k != i && k != j)
		printf("%d\n", a[k]);
	return 0;
}

void swap(int* a, int* b)
{
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

void SelectSort(int* ptr)
{
	int i, j;
	for (i = 0; i < N - 1; i++)
	for (j = i + 1; j < N; j++)
	if (ptr[i] > ptr[j])
		swap(ptr + i, ptr + j);
}
