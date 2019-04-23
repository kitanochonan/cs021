# CS21
# Lab exercise. A program that calculates from US dollar to Canada dollar

#USD to CAND rate
RATE = 1.33

def main():
    # Ask for USD
    usdollar = float(input("Let's convert your US Dollars to Canadian Dollars\nEnter the value of your US Dollars: "))
    # Give USD to usd2can function and get the return
    candollar = usd2can(usdollar)
    # Show the result
    print("This amount is worth $", format(candollar, ".2f"), "Canadian dollars.")

def usd2can(usd):
    return usd * RATE


main()
