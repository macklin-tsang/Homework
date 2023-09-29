// Name: Macklin Tsang
// Student Number: 301567122
// Computing ID: mta149

// Program was written with help of CS Peer Tutor 

// Include header file for function declarations
#include "a1_question3.h"

// Initial declaration of helper function
float squareNumber(int number); 

float printPointsDistances(unsigned int row, int points[][3], int point[]) {

    // Initialize the accumulator for our final answer
    float totalEuclideanDistance = 0; 

    for (int i = 0; i < row; i++) { // Iterate through each row
        // Point Calculations per x, y, z

        int xDifference = points[i][0] - point[0];
        int xDifferenceSquared = squareNumber(xDifference);

        int yDifference = points[i][1] - point[1];
        int yDifferenceSquared = squareNumber(yDifference);

        int zDifference = points[i][2] - point[2];
        int zDifferenceSquared = squareNumber(zDifference);
        
        float euclideanDistance = 
        sqrt(xDifferenceSquared + yDifferenceSquared + zDifferenceSquared);

        // Printing euclidean distances per row to 4 decimal places
        printf("Euclidean distance from (%d, %d, %d) to (%d, %d, %d) is %.4f\n", 
        points[i][0], points[i][1], points[i][2], point[0], point[1], point[2], 
        euclideanDistance);

        // Accumulate euclideanDistance per row
        totalEuclideanDistance += euclideanDistance; 
    }

    return totalEuclideanDistance;
}

// Helper function to square a given number
float squareNumber(int number) { 
    return number * number;
}
