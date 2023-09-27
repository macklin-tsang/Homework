#include <stdio.h>
#include "a1_question3.h"

double squareNumber(number) {
    return number * number;
}

double squareRoot(double number) {
    return sqrt(number);
}

float printPointsDistances(unsigned int row, int points[][3], int point[]) {

    double totalEuclideanDistance = 0;

    printf("This is the numbers for the 1st row: [%d, %d, %d]\n", points[0][0], points[0][1], points[0][2]);
    printf("This is the numbers for the 2nd row: [%d, %d, %d]\n", points[1][0], points[1][1], points[1][2]);
    printf("This is the numbers for the 3rd row: [%d, %d, %d]\n", points[2][0], points[2][1], points[2][2]);
    printf("This is the numbers for the 4th row: [%d, %d, %d]\n", points[3][0], points[3][1], points[3][2]);

    for (int i = 0; i < row; i++) {

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

    return totalEuclideanDistance;
}