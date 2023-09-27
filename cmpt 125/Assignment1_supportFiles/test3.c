#include <stdio.h>
#include <math.h>
#include "a1_question3.h"

//a helper function that compares 2 floats
void checkAndPrintFloats(float expected, float result) {
    if (fabs(expected-result) < 0.00001) {
        printf("%f (expected) is essentially the same as %f (result), PASS\n", expected, result);
    } else {
        printf("%f (expected) is essentially not the same as %f (result), FAIL\n", expected, result);
    }
}

int main() {
	
	int fourPoints[][3] = {{0, 0, 0}, {0, 2, 0}, {2, 0, 0}, {2, 2, 2}};
	int onePoint[] = {2, 2, 0};
	float totalDistance = printPointsDistances(4, fourPoints, onePoint);
    checkAndPrintFloats(8.828427, totalDistance); //should be very close to 8.828427
   
    return 0;
}