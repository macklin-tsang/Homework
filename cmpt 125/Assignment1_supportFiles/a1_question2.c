// Name: Macklin Tsang
// Student Number: 301567122
// Computing ID: mta149

// Helped used for selection sort via GeeksForGeeks
// https://www.geeksforgeeks.org/selection-sort/

// Include header file for function declarations
#include "a1_question2.h"

void rangedSort(int array[], unsigned int size, int leftIndex, int rightIndex){

    // Conditionals for right and left index
    
    if (leftIndex > rightIndex){
        int placeholder = rightIndex;
        rightIndex = leftIndex;
        leftIndex = placeholder;
    }
    
    if (leftIndex < 0 || leftIndex >= size){
        leftIndex = 0;
    }

    if (rightIndex < 0 || rightIndex >= size){
        rightIndex = size-1; // Array is 0-indexed, size-1 for rightmost index
    }

    // Selection Sort via GeeksForGeeks
    for (int i = leftIndex; i <= rightIndex; i++){
        int minimumIndex = i;
        for (int j = i + 1; j <= rightIndex; j++) {
            if (array[j] < array[minimumIndex]){
                minimumIndex = j;
            }
        }
        // Swap specified indices
        int placeholder = array[i];
        array[i] = array[minimumIndex];
        array[minimumIndex] = placeholder;
    }

}
