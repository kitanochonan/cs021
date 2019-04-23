# CS21
# A program that reads in the contents of a text file and displays a histogram of the frequency that words appear in the text

def main():
    
    # Ask user for a file name
    file_name = str(input("Enter the filename: "))

    # Give the file name to freq(filename) function that returns a dictionary including words and frequency as key-value pairs
    freq_dict = freq(file_name)

    # If the file isn't read successfully freq() function returns False
    if freq_dict == False:
        print("Check the filename you typed.")

    # If the file doesn't have any data in it
    elif len(freq_dict) == 0:
        print("File has no data in it.")

    else:
        # Create a histogram
        print("Word Frequency")
        print("  --------------")
        for ch in freq_dict:
            print("  ", ch, ": ", "*" * freq_dict[ch], sep="")

def freq(filename):

    try:
        # Read file
        infile = open(filename, "r")
    except IOError:
        print("Failed to open the file")
        return False

    # Prepare punctuation list
    punctuation = [',','.',';',':','!','?','\'','\"']

    # replace punctuations with a space
    # Read the file
    text = infile.read().lower()
    for punc in punctuation:
        text = text.replace(punc," ")
    
    # Split the text and make a list of words
    words_list = text.split()

    # Prepare a list which has words and counts as key-value pairs
    words_freq = {}

    # Add words and counts from words_list to words_freq dictionary
    for word in words_list:
        if word in words_freq:
            count = words_freq[word]
            count += 1
            words_freq[word] = count
        else:
            words_freq[word] = 1

    return words_freq


main()
