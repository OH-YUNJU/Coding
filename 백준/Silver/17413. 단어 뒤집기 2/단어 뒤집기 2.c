#include <stdio.h>
#include <string.h>
int main()
{
	int a;
	int start = 0;
	int end = 0;
	char arr[100005]={0};
	
	gets(arr);
	int len = strlen(arr);
	for(int i = 0; i<= len; i++)
	{
		if (arr[i] == '\0')
				return 0;
		if(arr[i] == '<')
		{
			while(1)
			{
				printf("%c", arr[i]);
				i++;
				if(arr[i] == '>')
				{
					printf (">");
					start = i + 1;
					break;
				}
			}
		}
		else if(arr[i + 1] == ' ' || arr[i + 1] == '\0' || arr[i + 1] == '<')
		{
			end = i;
			
			for(int j = end; j >= start; j--)
			{
				printf("%c", arr[j]);
			}
			start = i + 1;
		}
		else if(arr[i] == ' ')
		{
			printf(" ");
			start++;
		}
	}
	printf ("\n");
	return 0;
}