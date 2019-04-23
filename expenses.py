# CS21
# A program to compute the total cost of gasoline used during a user's most recent trip

MPG_HWY = 38 # 2018 MINI Cooper gets 28 mpg in the highway
MPG_CITY = 28 # 2018 MINI Cooper gets 38 mpg in the city
GAS_PRICE = 2.29 #gas price per gallon

def main():
    print("Computing your gasoline expenses...")
    
    # at least excute once
    again = "y"
    while again == "y" or again == "Y":

        # prompt user total miles and validate the input
        total_miles = float(input("\nTotal miles driven: "))
        while total_miles < 0:
            total_miles = float(input("Enter a value > 0: "))
    
        # propmt user highway percentage and validate the input
        highway_percentage = float(input("Percentage of total miles driven on a highway: "))
        while highway_percentage < 0 or highway_percentage > 100:
            highway_percentage = float(input("Enter a value between 0 and 100: "))

        # Output the result
        print("\nHere is the information for your trip:\n")
        print("Total miles:", format(total_miles, ".1f"))

        # Get gas consumption
        gas_consumption = total_gallons(total_miles, highway_percentage)
        print("Gas consumption:", format(gas_consumption, ".1f"), "gal")
        print("Total cost: $", format(gas_expense(gas_consumption), ".2f"), "\n")

        # Ask a user whether to compute again
        again = str(input("Compute gas expense for another trip (y or n)? "))

def total_gallons(total_miles, highway_percentage):
    # Get total highway miles
    total_highway_miles = total_miles * (highway_percentage/100)
    # Get the city miles
    total_city_miles = total_miles - total_highway_miles
    # Calculate total gas consumption and return
    return total_highway_miles/MPG_HWY + total_city_miles/MPG_CITY

def gas_expense(total_gallons):
    return total_gallons * GAS_PRICE

main()

