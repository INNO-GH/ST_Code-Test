#include <stdio.h>


int main(void)
{
	int A, B;
	scanf("%d %d", &A, &B); // Don't Forget &
	if(A>B) printf("A", A);
	else if(A==B) printf("same", A);
	else printf("B", B);
	return 0;
}
