rows = int(input("Enter the number of rows: "))

columns = int(input("Enter the number of columns: "))

matrix = []

print("Enter values in matrix : ")

for i in range(rows):
    numbers = []
    for j in range(columns):
        numbers.append(int(input()))
    matrix.append(numbers)

for i in range(rows):
    print("Sum of row " + str(i+1) + ": " + str(sum(matrix[i-1])))
