#include <stdio.h>


int main(void)
{
	int i, start_hour, start_min, end_hour, end_min, sum=0;
	for(i=0;i<5;i++){
		scanf("%d:%d %d:%d", &start_hour, &start_min, &end_hour, &end_min); // We can write scanf by using "%~+~" easily
		// hour should be changed in forms of min, and we should consider min-min
		sum = sum + (end_hour-start_hour)*60 + (end_min-start_min);
	}
	printf("%d", sum);
	return 0;
}
