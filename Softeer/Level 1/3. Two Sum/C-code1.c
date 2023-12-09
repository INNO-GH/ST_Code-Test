#include <stdio.h>


int main(void){	
	int i, num, a, b;
	scanf("%d", &num);
	// If we just need to repeat num'th, for(i=0;i<num;i++) is typical answer
	for(i=0;i<num;i++){
		scanf("%d %d", &a, &b);
		printf("Case #%d: %d\n", i+1, a+b);	
	}
	return 0;
}
