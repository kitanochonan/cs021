#CS21
#A program that calculates salary

#Ask number of days worked
num_worked = int(input("Number of days worked: "))

#Validate the input
while num_worked < 1:
    num_worked = int(input("Enter number of days >= 1: "))

#Calculation and make a table
print("Salary Earned Each Day\n")
print("Day      Amount ($)")
print("---      ----------")

#Declare sum_amount for total pay
sum_amount = 0

#Calculate and display for the table
for i in range(1, num_worked + 1):
    amount = 0.01*(2**(i-1)) 
    sum_amount += amount #Store total pay in sum_amount
    print(format(i, "2d"), format(amount, "13.2f"))

#Calculate average pay
average_pay = sum_amount / num_worked

#Display total pay and average pay
print("\nYour total pay = $", format(sum_amount, ".2f"), sep="")
print("Your average daily wage = $", format(average_pay, ".2f"), sep="")
