# CS21
# A program that references a file and count the number of
# uppercase letters, lowercase letters, digits, and spaces

def main():

    # Ask a user for a filename
    file_name = str(input("Enter the filename: "))

    # Give the filename to char_analysis(filename) function
    # which has four values to return
    upper_nums, lower_nums, digits, whitespaces = char_analysis(file_name)

    # If there are no letters in the file, or if failed to open the file but still the char_analysis(filename) gives back 0s
    if upper_nums == 0 and lower_nums == 0 and digits == 0 and whitespaces == 0:
        print("Character analysis hasn't been done.")
    else:
        # Display
        print("Uppercase letters:", upper_nums)
        print("Lowercase letters:", lower_nums)
        print("Digits:", digits)
        print("Spaces:", whitespaces)


def char_analysis(filename):

    # Open the file in the reading mode
    try:
        text_file = open(filename, "r")
    except IOError:
        print("Couldn't find the file.")

    # prepare accumulators
    upper_num = 0
    lower_num = 0
    digit = 0
    whitespace = 0

    # Read each line and count numbers of the four values
    try:
        for line in text_file:
            for letter in line:
                if letter.isalpha() and letter.isupper():
                    upper_num += 1
                    #continue
                elif letter.isalpha() and letter.islower():
                    lower_num += 1
                    #continue
                elif letter.isdigit():
                    digit += 1
                    #continue
                #elif letter.isspace() or letter == "" or letter == " ":
                elif letter.isspace():
                    whitespace += 1
                    #continue

    except UnboundLocalError:
        print("Failed to open the file.")

    return int(upper_num), int(lower_num), int(digit), int(whitespace)  # Still possible to pass 0 to main()


main()

############## ?? whitespaces not the same with the sample  ########################