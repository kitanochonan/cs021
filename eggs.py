# CS021
# Module 3 Assignment
# A program that calculates the number of cartons needed to pack the eggs collected.
 

# One carton can have 12 eggs
CARTON = 12

# Ask for the number of eggs
eggs = int(input("This program will determine the required number of 1-dozen egg cartons. How many eggs did you collect today? "))

# number of eggs needs to be non-negative
if eggs < 0:
    print("Number of eggs cannot be negative.")
else:
    # Calculation
    cartons_num = int(eggs / CARTON)    # In Python3, integer division yields float.
    
    # Number of leftover eggs is remainder of eggs number divided by CARTON (12) 
    leftover_eggs = eggs % CARTON

    #display
    print("We will pack your", format(eggs, "d"), "eggs in", format(cartons_num, "d"), "cartons.\nThere will be", format(leftover_eggs, "d"), "eggs left over.")
