#include <stdio.h>
#include "a1_question1.h"

//a helper function that compares 2 ints
void checkAndPrintInts(int expected, int result) {
    if (expected == result) {
        printf("%d is the same as %d, PASS\n", expected, result);
    } else {
        printf("%d is not the same as %d, FAIL\n", expected, result);
    }
}

int main() {
	
    checkAndPrintInts(1, shuffleDigits(1)); //should return 1
    checkAndPrintInts(321, shuffleDigits(123)); //should return 321
    checkAndPrintInts(765, shuffleDigits(5670)); //should return 765 (no leading zero)

    return 0;
}