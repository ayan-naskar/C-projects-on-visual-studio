#include<stdio.h>

int sum(int, int);

int main()
{
	int n, m, sum1, sum2;
	printf("\nEnter the numbers :");
	scanf_s("%d %d", &n, &m);
	sum1 = sum(n, 1);
	printf("\n");
	sum2 = sum(m, 1);
	printf("\nsum1=%d\nsum2=%d", sum1, sum2);
	if (sum1 == m && n==sum2)
		return 1;
	else
		return 0;
}

int sum(int x, int i)
{
	if (x > i && x % i == 0) 
	{
		printf("%d ",i);
		/*if(i==142)
			printf("\nx=%d\n",x);*/
		return i + sum(x, i+1);
	}
	else if (x > i && x % i != 0)
		return sum(x, 1+i);
	else
		return 0;
}

