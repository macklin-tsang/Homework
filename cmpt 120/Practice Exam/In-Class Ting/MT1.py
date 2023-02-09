string = input('Enter a string: ')

first = string[1]

newString = ""

for i in range(len(string)):
    if(string[i] == first and i not in [0,2]):
        newString = newString + '*'
    else:
        newString = newString + string[i]

    