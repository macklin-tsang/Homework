#include <stdio.h>
#include "a1_question2.h"

//a helper function that compares the content of 2 int arrays
void checkAndPrintIntArrays(int expected[], int result[], unsigned int size) {
	//use an int to count any mismatches
	int numMismatches = 0;
	for (int i=0; i<size; i++) {
		if (expected[i] != result[i]) numMismatches++;
	}
	
    if (numMismatches == 0) {
        printf("All array elements match, PASS\n");
    } else {
        printf("%d array elements do(es) not match, FAIL\n", numMismatches);
	}
}

int main() {
	
	int myIntArray1[] = {-4, 3, -12, 0, 5, 72, 88, 128, 1, 64};
	int myIntArray2[] = {-4, 3, -12, 0, 5, 72, 88, 128, 1, 64};
	int myIntArray3[] = {-4, 3, -12, 0, 5, 72, 88, 128, 1, 64};
	int myIntArray4[] = {-4, 3, -12, 0, 5, 72, 88, 128, 1, 64};
	int myIntArray5[] = {-4, 3, -12, 0, 5, 72, 88, 128, 1, 64};
	int myIntArray6[] = {-4, 3, -12, 0, 5, 72, 88, 128, 1, 64};
	int myIntArray7[] = {-4, 3, -12, 0, 5, 72, 88, 128, 1, 64};

	//using an explicit way to create an int array as parameter
	//should sort indexes 0 to 3
	rangedSort(myIntArray1, 10, -2, 3);
    checkAndPrintIntArrays((int[]){-12, -4, 0, 3, 5, 72, 88, 128, 1, 64},
							myIntArray1, 10);
	//should sort indexes 7 to 9
	rangedSort(myIntArray2, 10, 10, 7);
    checkAndPrintIntArrays((int[]){-4, 3, -12, 0, 5, 72, 88, 1, 64, 128},
							myIntArray2, 10);
	//should sort indexes 5 to 5 (or simply does not sort)
	rangedSort(myIntArray3, 10, 5, 5);
    checkAndPrintIntArrays((int[]){-4, 3, -12, 0, 5, 72, 88, 128, 1, 64},
							myIntArray3, 10);
	//should sort indexes 0 to 9 (the whole array)
	rangedSort(myIntArray4, 10, 0, 9);
    checkAndPrintIntArrays((int[]){-12, -4, 0, 1, 3, 5, 64, 72, 88, 128},
							myIntArray4, 10);

    // Test when leftIndex is negative and rightIndex is too large
    rangedSort(myIntArray5, 10, -5, 15);
    // After bounds checks, leftIndex should be 0, and rightIndex should be 9.
    // So, it should sort the entire array.
    checkAndPrintIntArrays((int[]){-12, -4, 0, 1, 3, 5, 64, 72, 88, 128}, myIntArray5, 10);

    // Test when leftIndex is too large and rightIndex is negative
    rangedSort(myIntArray6, 10, 15, -5);
    // After bounds checks, leftIndex should be 0, and rightIndex should be 9.
    // So, it should sort the entire array.
    checkAndPrintIntArrays((int[]){-12, -4, 0, 1, 3, 5, 64, 72, 88, 128}, myIntArray6, 10);

    // Test when both leftIndex and rightIndex are too large
    rangedSort(myIntArray7, 10, 15, 15);
    // After bounds checks, leftIndex should be 0, and rightIndex should be 9.
    // So, it should sort the entire array.
    checkAndPrintIntArrays((int[]){-12, -4, 0, 1, 3, 5, 64, 72, 88, 128}, myIntArray7, 10);

    return 0;
}