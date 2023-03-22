def largest(s):

    if len(s) == 0:
        return s

    if s[0] > max:
        max = s[0]

    return largest(s[i:])
    
    print(max)

userList = int(input("Enter length of list: "))

s = []

print("Enter all numbers: ")

for i in range(userList):
    number = int(input())
    s.append(number)

largest(s)
