#CS021
#Module 3 Assignment
#A program that calculates weight from mass
#weight = mass * GRAVITY

#Gravity define
GRAVITY = 9.8

#Ask for mass 
mass = float(input("Enter the object's mass in kilograms: "))

#evaluate if the mass is valid
if mass <= 0:
    print("The number is invalid.")
else:
    #calculation and display
    weight = mass * GRAVITY 
    print("Obeject Weight:", format(weight, ".2f"))

    #evaluate the weight is too heavy or too light
    if weight > 500:
        print("The object is too heavy. It weighs more than 500 Newtons.")
    elif weight < 100:
        print("The object is too light. It weighs less than 100 Newtons.")
