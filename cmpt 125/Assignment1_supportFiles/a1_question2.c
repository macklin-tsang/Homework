#include <stdio.h>
#include "a1_question2.h"

void rangedSort(int array[], unsigned int size, int leftIndex, int rightIndex){
    if (leftIndex > rightIndex){
        int placeholder = rightIndex;
        rightIndex = leftIndex;
        leftIndex = placeholder;
    }
    
    if (leftIndex < 0 || leftIndex >= size){
        leftIndex = 0;
    }

    if (rightIndex >= size){
        rightIndex = size-1;
    }

    // printf("Sorting from index %d to %d\n", leftIndex, rightIndex);

    // Selection Sort

    for (int i = leftIndex; i <= rightIndex; i++){
        int minimumIndex = i;
        for (int j = i + 1; j <= rightIndex; j++) {
            if (array[j] < array[minimumIndex]){
                minimumIndex = j;
            }
        }
        int placeholder = array[i];
        array[i] = array[minimumIndex];
        array[minimumIndex] = placeholder;
    }
    
    // printf("Final array: [");
    // for (int i = 0; i < size; i++){
    //     printf("%d", array[i]);
    //     if (i < size - 1) {
    //         printf(", ");
    //     }
    // }
    // printf("]\n");

}
