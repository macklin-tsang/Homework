def list_of_greater_numbers():
    n = int(input("Enter target number: "))

    userList = int(input("Enter length of list: "))

    list = []

    print("Enter all numbers: ")

    for i in range(userList):
        number = int(input())
        list.append(number)

    newList = []

    for i in range(len(list)):
        if list[i] > n:
            newList.append(list[i])

    print("The numbers in the list greater than the target number are: " + str(newList))

list_of_greater_numbers()
