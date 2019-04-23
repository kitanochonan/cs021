# CS 21
# A program that reads the contents of two text files and compares them

def main():
    # Ask user for file names
    filename_1 = str(input("Enter the first file name: "))
    filename_2 = str(input("Enter the second file name: "))
    
    # Open files
    try:
        infile_1 = open(filename_1, "r")
        infile_2 = open(filename_2, "r")
    except IOError:
        print("Failed to open the file")

    # Create sets
    set_one = set()
    set_two = set()

    try:
        # Get the texts
        text_one = infile_1.read().upper()
        text_two = infile_2.read().upper()

        # Punctuation list
        punctuation = [',','.',';',':','!','?','\'','\"']

        # Make it only characters and spaces
        for punc in punctuation:
            text_one = text_one.replace(punc, " ")
            text_two = text_two.replace(punc, " ")

        # Split and make lists
        text_list_one = text_one.split()
        text_list_two = text_two.split()

        # Add elements to set_one
        for ch in text_list_one:
            set_one.add(ch)

        # Add elements to set_two
        for ch in text_list_two:
            set_two.add(ch)

    except UnboundLocalError:
        print("Couldn't compare files.")

    if len(set_one) == 0 and len(set_one) == 0:
        print("Files don't have any data to compare.")
    else:
        # Display
        print("Unique words that contained in both files:", set_one | set_two)
        print("Words that appear in both files:", set_one & set_two)
        print("Words that appear in the first file (", filename_1, ") but not the second (", filename_2, "):", set_one - set_two)
        print("Words that appear in the second file (", filename_2, ") but not the first (", filename_1, "):", set_two - set_one)
        print("Words that appear in either the first (", filename_1, ") or second file (", filename_2,"):", set_one ^ set_two)

main()
