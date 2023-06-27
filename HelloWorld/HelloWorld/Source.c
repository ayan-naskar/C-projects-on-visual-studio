#include<stdio.h>
//ayan liVES in Kol
//ei input er last e problem hoche
int main() {
	char a[40], b[40];
	int i, diff = (int)'a' - (int)'A';
	printf("Enter your sentence->\n");
	get_s(a,39);
	for (i = 0;a[i] != '\0';i++) {
		if (a[i] == ' ')
			b[i] = ' ';
		else if ((int)a[i] <= (int)'Z')
			b[i] = a[i] + diff;
		else
			b[i] = a[i] - diff;
	}
	printf("\nToggeled sentence->");
	printf("%s",b);
	return 0;
}