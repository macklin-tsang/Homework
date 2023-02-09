integers = input("Type various integer numbers separated by commas --> ")

numList = integers.split(",")

sum = 0

for i in range(len(numList)):

    multiplier = int(i)*int(numList[i])

    sum += multiplier

print("The sum of each number multiplied by its (Python) index is " + str(sum))