# CS21
# A program that writes the content of the input file to the output file

def main():
    
    # Ask the user for the name of the file and read the file
    fileName = str(input("Name of the file? (including file extension): "))

    # linenumbers() function accepts file name 
    # and read the same name file (input file) and write the data to ln_inputfile (output file)
    linenumbers(fileName)


def linenumbers(filename):
    try:
        # Open the file
        inputFile = open(filename,'r')
    except IOError:
        print("File does not exist.")

    # Counter
    count = 0

    # Open the output file in appending mode
    try:
        # Open the output file with writing mode
        outputFile = open("ln_" + str(filename), 'w')

    except IOError:
        print("File does not exist.")

     # Read each line of the file
    try:
        for line in inputFile:
            count += 1
            # Write data to the output file
            outputFile.write(str(count) + ": " + line)

        # Close the input file
        inputFile.close()

        # Close the output file
        outputFile.close()
    except UnboundLocalError:
        print("Failed to read the file.")

main()