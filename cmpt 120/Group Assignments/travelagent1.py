def askNumber(number):
    return int(number)

def discountNumber(age):

    if age > 64:
        discount = age - 64
        return discount
    else:
        return 0
    
def totalCosts(flightPrice, hotelPrice, nights, age):

    if age > 64:
        discount = age - 64
        return (flightPrice + (hotelPrice * nights)) * (1.0 - int(discount)/100)
    else:
        return (flightPrice + (hotelPrice * nights))
    
def tripDetails(destination, flightPrice, hotelPrice, nights, age):
    None

def password():
        # This will select the first character of the user's name
    password_first_character = str(name[0])

    # This will select the last character
    password_last_character = str(name[-1])

    # The variable will save the remainder of the age divided by 8
    n = age % 8

    # Create a variable and set it to the formula of the password.
    password = password_last_character * int(n) + password_first_character + (random.randint(0, 5) * "!")
    return password