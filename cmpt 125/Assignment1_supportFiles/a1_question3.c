#include <stdio.h>
#include "a1_question3.h"

int squareNumber(int number) { // Helper function to square a given number
    return number * number;
}

double squareRoot(int number) { // Helper function to quare root a given number
    return sqrt(number);
}

float printPointsDistances(unsigned int row, int points[][3], int point[]) {

    double totalEuclideanDistance = 0; // Initialize the accumulator for our final answer

    for (int i = 0; i < row; i++) { // Iterate through each row

        int xDifference = points[i][0] - point[0];
        int xDifferenceSquared = squareNumber(xDifference);

        int yDifference = points[i][1] - point[1];
        int yDifferenceSquared = squareNumber(yDifference);

        int zDifference = points[i][2] - point[2];
        int zDifferenceSquared = squareNumber(zDifference);
        
        double euclideanDistance = squareRoot(xDifferenceSquared + yDifferenceSquared + zDifferenceSquared);

        totalEuclideanDistance += euclideanDistance;

        printf("Euclidean distance from (%d, %d, %d) to (%d, %d, %d) is %f\n", points[i][0],points[i][1],points[i][2], point[0], point[1], point[2], euclideanDistance);
    }

    printf("This is the totalEuclideanDistance: %f\n", totalEuclideanDistance);

    return totalEuclideanDistance;
}
