# CS21
# A program which gives a letter grade from a numeric grade and creates a histogram of the grades

def main():
    # open a input file
    try:
        num_file = open('grades.txt', 'r')
    except IOError:
        print("File does not exist.")

    # counter for A,B,C,D,F
    count_a = 0
    count_b = 0
    count_c = 0
    count_d = 0
    count_f = 0

    # open a output file
    try:
        let_file = open('grades_out.txt', 'w')
    except IOError:
        print("File does not exist.")


    # read each line and calculate a letter grade with evaluate(float) function
    for line in num_file:
        try:
            letter_grade = evaluate(float(line))
            let_file.write(letter_grade + '\n')

            # add counter
            if letter_grade == 'A':
                count_a += 1
            elif letter_grade == 'B':
                count_b += 1
            elif letter_grade == 'C':
                count_c += 1
            elif letter_grade == 'D':
                count_d += 1
            elif letter_grade == 'F':
                count_f += 1

        except ValueError:
            let_file.write("Invalid numeric grade\n")
            print("Invalid numeric grade was found.")

    try:
        # creates a histogram
        # for grade A
        let_file.write("\nA: ")
        for i in range(0,count_a):
            let_file.write('*')

        # for grade B
        let_file.write("\nB: ")
        for i in range(0,count_b):
            let_file.write('*')

        # for grade C
        let_file.write("\nC: ")
        for i in range(0,count_c):
            let_file.write('*')

        # for grade D
        let_file.write("\nD: ")
        for i in range(0,count_d):
            let_file.write('*')

        # for grade F
        let_file.write("\nF: ")
        for i in range(0,count_f):
            let_file.write('*')

    except ValueError:
        print("Invalid data")

    # close the input file
    num_file.close()

    # close the output file
    let_file.close()

def evaluate(num_grades):
    if num_grades <= 100 and num_grades >= 90:
        return 'A'
    elif num_grades <= 89 and num_grades >= 80:
        return 'B'
    elif num_grades <= 79 and num_grades >= 70:
        return 'C'
    elif num_grades <= 69 and num_grades >= 60:
        return 'D'
    elif num_grades <= 59 and num_grades >= 0:
        return 'F'
    else:
        return "Invalid numeric grades"

main()