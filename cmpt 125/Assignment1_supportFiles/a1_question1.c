// Name: Macklin Tsang
// Student Number: 301567122
// Computing ID: mta149

// Program was written with help of CS Peer Tutor 

// Include header file for function declarations
#include "a1_question1.h"

// Initial declaration of helper function
// Purpose: Manipulate number based on decimal place value
int powerOfTen(int digitHolder);

unsigned int shuffleDigits(unsigned int number){

    // Initialize accumulation variables
    int digitLength = 0;
    int finalResult = 0;

    // Initialize copies of number for counting and array creation
    int digitCounterNumber = number;
    int digitArrayNumber = number;
    
    // While loop to remove trailing zeros for our number copies
    while (digitCounterNumber % 10 == 0) {
        digitCounterNumber /= 10;
        digitArrayNumber /= 10;
    }

    // Find out how many digits there are
    while (digitCounterNumber > 0) { 
        digitCounterNumber /= 10;
        digitLength++;
    }

    // Initialize empty array
    int digitArray[digitLength]; 

    // Storing the 10^digitLength for array creation & result
    int tenthPowerNumber = powerOfTen(digitLength);

    int arrayTenthPower = tenthPowerNumber; // Copy of 10^digitLength for array

    // Iterate and place each leftmost digit into our array
    for (int i = 0; i<digitLength; i++) {
        int singleDigit = digitArrayNumber/arrayTenthPower;
        digitArray[i] = singleDigit;
        digitArrayNumber = digitArrayNumber % arrayTenthPower;
        arrayTenthPower /= 10;
    }

    // Iterate and swap variables in respective indices (from left to right)
    for (int i = 0; i<digitLength/2; i++) { // Stop at the middle of array
        int placeholder = digitArray[0+i];
        digitArray[0+i] = digitArray[digitLength-1-i];
        digitArray[digitLength-1-i] = placeholder;
    }

    // Iterate through array and accumulate finalResult
    for (int i = 0; i<digitLength+1; i++) {
        // Place integer in its respective place value
        finalResult += tenthPowerNumber * digitArray[i];
        tenthPowerNumber /= 10;
    }

    return finalResult;
};

// Helper function to calculate 10^digitLength
int powerOfTen(int digitLength){
    int tenthPower = 1;

    for (int i = 0; i<digitLength-1; i++) {
        tenthPower *= 10;
    }

    return tenthPower;
}
