# CS21
# A program that accepts a phone number with alphabets and returns numeric phone number

def main():

    # Prepare a list which contains only a numeric phone number
    numeric_phone_num = []

    # Prepare a list which can contain numeric and alphabet phone number
    phone_num_list = []

    # Ask user a phone number
    phone_alnum = str(input("Enter the telephone number in the format XXX-XXX-XXXX: "))
    while phone_alnum == "":
        phone_alnum = str(input("Enter the telephone number in the format XXX-XXX-XXXX: "))


    ############### input validation ################

    # Check if a user typed '-'. If find(a) cannot find a, it returns -1.
    while phone_alnum.find('-') == -1:
        phone_alnum = str(input("Don't forget to type '-' between numbers.\nEnter the telephone number IN THE FORMAT XXX-XXX-XXXX: "))
        # Make it upper case and split the given phone number by "-"
        phone_num_list += phone_alnum.upper().split("-")

    # Split the phone number and put it to the list phone_num_list
    phone_num_list += phone_alnum.upper().split("-")

    # Check if the phone number is XXX - XXX - XXXX format
    while len(phone_num_list[0]) != 3 or len(phone_num_list[1]) != 3 or len(phone_num_list[2]) != 4:
        phone_alnum = str(input("Incorrect format. Enter the telephone number IN THE FORMAT XXX-XXX-XXXX: "))

        # Check if a user typed something
        while phone_alnum == "":
            phone_alnum = str(input("Enter the telephone number in the format XXX-XXX-XXXX: "))

        # Check if a user typed '-' again
        while phone_alnum.find('-') == -1:
            phone_alnum = str(input(
                "Don't forget to type '-' between numbers.\nEnter the telephone number IN THE FORMAT XXX-XXX-XXXX: "))

        # Once the number passes the check, split it again
        phone_num_list = phone_alnum.upper().split("-")

    ############ input validation ends here #############


    # Check if there is an alphabetical letter in each value of the list and
    # replace the alphabetical letter with a correspond number with alpha2num(a) function.
    for i in range(3):

        # Temporal string variable num
        num = ""

        # If a part of phone number (XXX or XXXX) contains alphabet(s),
        if not phone_num_list[i].isdigit():
            # Pick each letter from the part of phone number
            for letter in phone_num_list[i]:
                # Check if the letter is an alphabet
                if letter.isalpha():
                    # If it is a alphabet, give the alphabet to alpha2num(alphabet) function and get corresponding number.
                    # The corresponding number is added to a temporal string variable "num"
                    num += alpha2num(letter)

<<<<<<< HEAD
                else:
                    num += letter
=======
>>>>>>> origin/master
            # Once all alphabets in a part of the phone number are translated to numbers and added to "num",
            # append "num" to a list which contains only numbers
            numeric_phone_num.append(num)

        # If a part of phone number (XXX or XXXX) contains no alphabets
        else:
            # Add the part to a list which contains only numbers
            numeric_phone_num.append(phone_num_list[i])

    # Display translated phone number
    print("The phone number is ", numeric_phone_num[0], '-', numeric_phone_num[1], '-', numeric_phone_num[2], sep='')

def alpha2num(character):

<<<<<<< HEAD
    if character.isdigit():
        return character

=======
>>>>>>> origin/master
    # Prepare alphabets string
    ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Depending on the index, return different number to main()
    if ALPHABETS.find(character) >= 21:
        return "9"
    elif ALPHABETS.find(character) >= 18:
        return "8"
    elif ALPHABETS.find(character) >= 15:
        return "7"
    elif ALPHABETS.find(character) >= 12:
        return "6"
    elif ALPHABETS.find(character) >= 9:
        return "5"
    elif ALPHABETS.find(character) >= 6:
        return "4"
    elif ALPHABETS.find(character) >= 3:
        return "3"
    elif ALPHABETS.find(character) >= 0:
        return "2"

main()