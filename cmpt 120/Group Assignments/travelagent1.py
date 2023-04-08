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

def suggestTrip(music, beach, viennaPrice, baliPrice):

    if bool(music) == True:
        if bool(beach) == True:
            return 'Bali'
        if bool(beach) == False:
            return 'Vienna'
    if bool(music) == False:
        if bool(beach) == True:
            return 'Bali'
        if bool(beach) == False:
            return None
        
def createAccount():

    answer = input("Do you want to create an account").lower.strip()
    
    if answer == 'yes':
        password()
    else:
        None

        
