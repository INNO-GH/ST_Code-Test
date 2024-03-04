#include <stdio.h>
#include <stdlib.h>

void swap(int** a, int** b);
void quickSort(int** arr, int left, int right);

// Solution -> Choose most expansive and gradually reduce that
int main(void) {
	int W, N, i;
	scanf("%d %d", &W, &N);
	int** a = (int**)malloc(sizeof(int*) * N); // For make N array, we should use memory function
	for (i = 0; i < N; i++) {
		a[i] = (int*)malloc(sizeof(int) * 2);
		scanf("%d %d", &a[i][0], &a[i][1]);
	}
	// Sorting Process (By Price) -> Weight Check (By Weight) 
	// Quick Sort (Memorize) -> Fast Sort Algorithm
	quickSort(a, 0, N-1);
	// Weight Check
	int p_sum = 0, w_sum = 0;
	for (i = N - 1; i >= 0; i--) {
		if (w_sum + a[i][0] > W) { // There's no room in bag
			p_sum = p_sum + (W - w_sum) * a[i][1];
			break;
		}
		else { // There's room in bag
			p_sum = p_sum + a[i][0] * a[i][1];
			w_sum = w_sum + a[i][0];
		}
	}
	printf("%d", p_sum);
	for (i = 0; i < N; i++) {
		free(a[i]);
	}
	free(a);
	return 0;
}

void swap(int** a, int** b) {
	int* c;
	c = *a;
	*a = *b;
	*b = c;
}
// Memorize Quick Sort (Basic Algorithm)
void quickSort(int** arr, int left, int right) {
	if (left >= right) {
		return;
	}

	int pivot = arr[left][1];
	int i = left + 1;
	int j = right;

	while (i <= j) {
		while (i <= right && arr[i][1] < pivot) {
			i++;
		}

		while (j >= left + 1 && arr[j][1] > pivot) {
			j--;
		}

		if (i <= j) {
			swap(&arr[i], &arr[j]);
			i++;
			j--;
		}
	}

	swap(&arr[left], &arr[j]);

	quickSort(arr, left, j - 1);
	quickSort(arr, j + 1, right);
}

// This is practice code for quick sort
/*#include <stdio.h>

void quick(int* arr, int start, int end);

int main() {
	int arr[12] = { 12, 10, 10, 9, 7, 8, 6, 5, 4, 3, 2, 14 };
	quick(arr, 0, 11);
	int i;
	for (i = 0; i < 12; i++) {
		printf("%d ", arr[i]);
	}
}

void quick(int* arr, int start, int end) { // 1. We need array/start/end
	// 2. Clarify the case when we should stop the sorting
	if (start >= end) {
		return;
	}
	// 3. designate pivot/i/j (If we want not start piot, just pick and change it with first!)
	int pivot = arr[start]; 
	int i = start + 1;
	int j = end;
	// 4. move i, j and swap
	while (i <= j) {
		while (i <= end && arr[i] <= pivot) i++;
		while (j >= start + 1 && arr[j] >= pivot) j--;
		if (i <= j) {
			int c;
			c = arr[i];
			arr[i] = arr[j];
			arr[j] = c;
			i++;
			j--;
		}
	}
	int c;
	c = arr[start];
	arr[start] = arr[j];
	arr[j] = c;
	// 5. Recursioning
	quick(arr, start, j - 1);
	quick(arr, j + 1, end);
}*/


