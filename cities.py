# CS21
# A program that asks user for a city name, compares that value with the contents of two text files, and reports each match

def main():
    while True:
        # Ask user city name
        city_name = str(input("City name (type 'q' to quit): "))

        # if 'q' was typed, escape the while loop
        if city_name == "q":
            break

        # Using file2list() function, get lists from the file. Give names to each list.
        vt_list = file2list("vt_municipalities.txt")
        nh_list = file2list("nh_municipalities.txt")

        # prepare counters
        count_vt = 0
        count_nh = 0

        # check if the lists contain data with len() and if the city name exists in both lists by adding 1 to counters
        if len(vt_list) > 0:
            for i in range(len(vt_list)):
                if vt_list[i].rstrip().lower() == city_name.lower():    # Use .rstrip() to remove '\n' from each value in the list. Use .lower() to make it case-insensitive.
                    count_vt += 1
                    break   # If there is a match, then it ends the for loop.

        if len(nh_list) > 0:
            for i in range(len(nh_list)):
                if nh_list[i].rstrip().lower() == city_name.lower():
                    count_nh += 1
                    break

        # display whether or not the city is in states
        # Use .lower() and .capitalize() to modify the name of the city
        if count_vt == 1 and count_nh == 1:
            print(city_name.lower().capitalize(), "is in Vermont and New Hampshire.")
        elif count_vt == 1 and count_nh == 0:
            print(city_name.lower().capitalize(), "is in Vermont.")
        elif count_vt == 0 and count_nh == 1:
            print(city_name.lower().capitalize(), "is in New Hampshire.")
        else:
            print("Neither VT nor NH has a city by that name.")

def file2list(file_name):
    # prepare a list
    city_list = []

    # open the file in reading mode
    try:
        input_file = open(file_name, "r")
    except IOError:
        print("***FILE ERROR: ", file_name, "cannot be found.")
    else:
        for line in input_file:
            city_list.append(line)
        input_file.close()
    finally:
        return city_list

main()