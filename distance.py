# CS021 Assignment #5
# A program that calculates distance traveled with speed and hour

def main():

    #Ask user for speed
    speed = float(input("Enter the speed of the vehicle in mph: "))
    #Check if speed is greater than zero
    while speed <= 0:
        print("speed must be greater than zero")
        speed = float(input("Enter the speed of the vehicle in mph: "))
    
    #Ask user for time
    hours = int(input("Enter the number of hours traveled: "))
    #Check if time is greater than zero
    while hours <= 0:
        print("time must be greater than zero")
        hours = int(input("Enter the number of hours traveled: "))
    
    #Call show_travel function
    show_travel(speed, hours)

def show_travel(speed, hours):
    print("Hour  Distance Traveled\n------------------------")
    for i in range(1, hours+1):
        print(format(i, "1d"), format(speed*i, "12.1f"))

main()
