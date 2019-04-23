# CS21 Assignment 6
# A program that plays the game of 21

import random

def main():
    # To count user's total number
    num_total_user = 0
    # To count computer's total number
    num_total_com = 0
    # Get user response
    response = get_response()

    while response == "y":
        # Get values from roll_dice() function
        user_num, com_num = roll_dice()
        # add user's and computer's die to num_total_user and num_total_com
        num_total_user += user_num
        num_total_com += com_num
        # Show user's total
        print("Points:", format(num_total_user, "d"))
        # make response "n" so that it won't ask response when the total number of user exceeds 21    
        response = "n"
        # Ask again if the user want to roll or not if total number of user < 21
        if num_total_user < 21:
            response = get_response()

    # Show the user's and computer's points
    print("User's points:", format(num_total_user, "d"))
    print("Computer's points:", format(num_total_com, "d"))
    # Compare the user's points and computer's point and show result
    if num_total_user > num_total_com:
        print("User wins")
    elif num_total_user == num_total_com:
        print("Tie Game!")
    else:
        print("Computer wins")

def get_response():
    # Ask if the user want to roll
    response = str(input("Do you want to roll? "))
    
    # Validate the response
    if response != "y" and response != "n":
        response = str(input("Invalid response. Do you want to roll? (y or n)"))

    # Return user response
    return response
    
def roll_dice():
    user_num = random.randint(1, 6)
    com_num = random.randint(1, 6)
    return user_num, com_num

main()
