//finding the area of triangle and finding if a point lies within it or not
#include<stdio.h>
float dist(int*, int*);
float area(int*,int*,int*);
int main()
{
	int x, y;
	int* p = &x;
	int x1, y1, x2, y2, x3, y3;
	int* a,b,c;
	a = &x1;
	b = &x2;
	c = &x3;
	printf("\nEnter the Point X: ");
	scanf("%d %d", &x, &y);
	printf("\nEnter the values for point A: ");
	scanf("%d,%d", &x1, &y1);
	printf("\nEnter the values for point B: ");
	scanf("%d,%d", &x2, &y2);
	printf("\nEnter the values for point C: ");
	scanf("%d,%d", &x3, &y3);
	if ((area(a, b, p) + area(a, c, p) + area(b, c, p)) == area(a, b, c))
		return 1;
	else
		return 0;
}

float area(int *k, int *l, int*m)
{
	float lenlk=dist(k,l), lenlm=dist(l,m), lenkm(k,m);
	float s = (lenlk + lenlm + lenkm) / 2;
	return pow(s * (s - lenlk) * (s - lenlm) * (s - lenkm), 0.5);
}
float dist(int* x, int* y)
{
	return pow(pow(*x - *y, 2) + (*(x + 1) - *(y + 1)), 0.5);
}