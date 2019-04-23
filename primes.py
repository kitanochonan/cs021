#CS21
#A program that determine if a number is prime or not.

def main():
    print("Welcome to my prime number detector.\nProvide an integer and I will determine if it is prime.")

    #To make this program rum at least once
    try_again = 'Y'

    while try_again == 'Y':

        #Ask for a number
        num = int(input("Enter an integer > 1: "))

        #Validate the number
        while num <= 1:
            num = int(input("Input must be > 1, try again: "))

        if isPrime(num):
            print("The integer", num, "is prime.")
        else:
            print("The integer", num, "isn't prime.")

        #Ask to try again or not
        try_again = input("Do you want to try another number? (Y/N): ").upper()

def isPrime(number):

    if number < 2:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False

    maxFactor = round(number**(1/2))

    for factor in range(3, maxFactor, 2):
        if number % factor == 0:
            return False

    return True

main()