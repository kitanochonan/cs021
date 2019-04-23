# CS21
# A program that accepts input data about employees' name, hours worked, and hourly rate,
# and computes total pay to payroll.txt (output file) with total payroll and average paycheck

def main():

    # initialize lists
    names =[]
    hours_worked = []
    hourly_rates = []

    # prepare a counter
    count = 0

    # prepare total_pay
    total_pay = 0

    # prepare a counter for checking if there is a long name (over 15 characters)
    long_name_count = 0

    # set 20 spaces for names
    space4names = 20

    # if there is a long name (over 15 characters) detected, replace the number of spaces to give for names
    max_length_name = 0


    # open an output file

    try:
        output_file = open("payroll.txt", "w")
    except IOError:
        print("Failed to open an output file.")

    while True:
        # Ask an employee's name
        name = str(input("Name (just hit Enter when done) : "))

        # when user hit Enter, escape from the while loop
        if name == "":
            break

        # Catch ValueError (if user type something non-numeric)
        try:
            # Ask user hours worked and hourly rate
            hours = float(input("Hours worked: "))
            hourly_rate = float(input("Hourly rate: "))
        except ValueError:  # if ValueError is found, every code below is going to be skipped by "continue"
            print("Values must be numeric.\nPlease input employee's name and values again.")
            continue    # Go back to the start of while loop. Do not append values to lists.

        # add name, hours worked, and hourly rate to each list
        names.append(name)
        hours_worked.append(hours)
        hourly_rates.append(hourly_rate)
        # calculate total pay
        total_pay += hours * hourly_rate
        # Add count
        count += 1

    # Add spaces equally after name to make the output file tidy
    # If there is a name over 15 characters in names list
    for i in range(0, count):
        if len(names[i]) > 15:
            # Add long name counter
            long_name_count += 1
            # Replace max_length_name with the length of the long name if there is a longer name in the list
            if len(names[i]) >= max_length_name:
                max_length_name = len(names[i])

    # when there is at least one long name,
    if long_name_count > 0:
        # update space for names
        space4names = max_length_name + 5
        # Add spaces after each name
        for i in range(0, count):
            # Until it reaches the updated space size (space4names)
            while len(names[i]) < space4names:
                names[i] = names[i] + " "
    # when there is no long name
    else:
        for i in range(0, count):
            # Add spaces until it reaches the space size given (space4names)
            while len(names[i]) < space4names:
                names[i] = names[i] + " "


    # Write data to the output file
    for i in range(0, count):
        output_file.write(names[i] + format(hours_worked[i], ".2f") + format(hourly_rates[i], "9.2f") + format(hours_worked[i] * hourly_rates[i], "9.2f") + "\n")

    # if count > 0, which means at least one employee's data was input, display total pay and average pay check
    if count > 0:
        output_file.write("\nTotal Payroll = $" + format(total_pay, ".2f") + "\n")
        output_file.write("Average Paycheck = $" + format(total_pay / count, ".2f"))

    # close the output file
    output_file.close()

main()
