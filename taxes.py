# CS21
# A program that calculates property tax

# Assessed value = actual value * 0.6
# Property tax = Assessed value * 0.72 / 100

ASSESSED_VALUE_RATE = 0.6  # Assessed value = actual value * ASSESSED_VALUE_RATE
PROPERTY_TAX_RATE = 0.0072  # Property tax = Assessed value * PROPERTY_TAX_RATE

def main():
    # Ask user for the actual value
    actual_value = float(input("Enter the actual value: "))
    # Check if the value is negative or not
    while actual_value < 0:
        print("Actual value must be >= 0")
        actual_value = float(input("Enter the actual value: "))

    # Calculate assessed value
    assessed_value = float(actual_value * ASSESSED_VALUE_RATE)

    # Calculate property tax
    property_tax = float(assessed_value * PROPERTY_TAX_RATE)

    # Call show_property_tax fundtion
    show_property_tax(assessed_value, property_tax)


def show_property_tax(assessed_value, property_tax):
    # format(x, ",") puts comma to numbers
    # Able to put format specifier after comma in "" of format function
    print("Assessed value: $", format(assessed_value, ",.2f"), sep="")
    print("Property tax: $", format(property_tax, ",.2f"), sep="")

main()