#include<stdio.h>
int main()
{
	int val = 1;
	if(*(char *)&val == 1)
	{
		printf("Little-Endian\n");
	}
	else
	{
		printf("Big-Endian\n");
	}
return 0;
}

