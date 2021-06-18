def main():

    province_list = read_list("provinces.txt")

    counter = province_list[len(province_list) - 1]
    province_list.pop()

    print(province_list)
    print(f"There are {counter} instances of Alberta in the modified list.")


def read_list(filename):
    
    province_list = []
    
    with open(filename, "rt") as provinces:

        counter = 0

        for province in provinces:
            province_list.append(province.strip())
            if province.strip() == "AB" or province.strip() == "Alberta":
                province = "Alberta"
                counter += 1
                print(counter)

        province_list.pop(0)
        province_list.pop()
        province_list.append(counter)

    return province_list


if __name__ == "__main__":
    main()














"""
def main():
    # Read the contents of a text file
    # named plants.txt into a list.
    province_list = read_list("provinces.txt")

    # Print the entire list.
    print(province_list)


def read_list(filename):
    START_NOTE
    Read the contents of a text file into a list and
    return the list. Each element in the list will contain
    one line of text from the text file.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    END_NOTE

    # Create an empty list named text_list.
    province_list = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "rt") as provinces:

        # Read the contents of the text
        # file one line at a time.
        for province in provinces:

            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = province.strip()

            # Append the clean line of text
            # onto the end of the list.
            province_list.append(clean_line)

    # Return the list that contains the lines of text.
    return province_list


# Call main to start this program.
if __name__ == "__main__":
    main()
"""