word = input("Enter a string --> ")

word = list(word)

print(word)

vowels = ["a", "e", "i", "o", "u"]

newString = ""

for x in word:
    if x not in vowels:
        newString += x

print(newString)
