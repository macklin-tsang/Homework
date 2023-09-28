#include <stdio.h>
#include "a1_question1.h"

unsigned int shuffleDigits(unsigned int number){
    int digitLength = 0;
    int digitCounterNumber = number;
    int digitArrayNumber = number;
    int finalResult = 0;
    // make a function to clip off trailing zeros
    while (digitCounterNumber > 0) { // Find out how many digits there are
        digitCounterNumber /= 10;
        digitLength++;
    }

    int digitArray[digitLength]; // Initialize empty array

    int tenthPowerNumber = powerOfTen(digitLength);

    int arrayTenthPower = tenthPowerNumber;

    for (int i = 0; i<digitLength; i++) {
        int singleDigit = digitArrayNumber/arrayTenthPower;
        digitArray[i] = singleDigit;
        digitArrayNumber = digitArrayNumber % arrayTenthPower;
        arrayTenthPower /= 10;
    }

    for (int i = 0; i<digitLength/2; i++) {
        int placeholder = digitArray[0+i];
        digitArray[0+i] = digitArray[digitLength-1-i];
        digitArray[digitLength-1-i] = placeholder;
    }

    for (int i = 0; i<digitLength+1; i++) {
        finalResult += tenthPowerNumber * digitArray[i];
        tenthPowerNumber /= 10;
    }

    return finalResult;
};

int powerOfTen(int digitHolder){
    int tenthPower = 1;

    for (int i = 0; i<digitHolder-1; i++) {
        tenthPower *= 10;
    }

    return tenthPower;
}
