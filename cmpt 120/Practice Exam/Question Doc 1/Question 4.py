def palindrome():
    string = input()

    if string[len(string)//2::-1] == string[len(string)//2::1]:
        return True
    else:
        return False

palindrome()