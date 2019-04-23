#CS021
#Module 3 Assignment
#A program that prompts the user for three int numbers and dispalys the numbers in descending order

#Ask for integers
first_num = int(input("First number? "))
second_num = int(input("Second number? "))
third_num = int(input("Three number? "))

#Put numbers in descending order and display
#Pattern1: first_num is the biggest
if first_num >= second_num and first_num >= third_num:
    if second_num >= third_num:
        print("Descending order:", first_num, second_num, third_num)
    else:
        print("Descending order:", first_num, third_num, second_num)

#Pattern2: second_num is the biggest
elif second_num >= first_num and second_num >= third_num:
    if first_num >= third_num:
        print("Descending order:", second_num, first_num, third_num)
    else:
        print("Descending order:", second_num, third_num, first_num)

#Pattern3 (else): third_num is the biggest
else:
    if first_num >= second_num:
        print("Descending order:", third_num, first_num, second_num)
    else:
        print("Descending order:", third_num, second_num, first_num)
