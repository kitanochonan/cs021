# CS21
# A program that tallies the frequency of every letter found in the user input

def main():

    # Prepare two lists
    alpha_list = []
    count_list = []


    # Ask a user for a string and make it uppercase
    sentence = str(input("Enter a string: ")).upper()

    # Examine each letter of the input sentence
    for letter in sentence:

        # Prepare a counter
        count = 0

        # Pick each alphabet from the alphabet list
        for alpha in alpha_list:
            # and check if there is a match with the letter from the sentence
            if letter == alpha:
                # If there is, add 1 to the counter
                count += 1
                # escape the loop once it finds a match
                #continue
                break

        # If counter is 1, which means there was a match found
        if count == 1:
            # add 1 to the value of count list. Index needs to be connected with the alphabet list
            count_list[alpha_list.index(letter)] += 1
        # If there wasn't found a match, append the letter to the alphabet list and append 1 in count list.
        else:
            alpha_list.append(letter)
            count_list.append(1)

    # Display
    print("\nLetter\tFreq")
    for i in range(0, len(alpha_list)):
        print(" ", alpha_list[i], format(count_list[i], "6d"))


main()