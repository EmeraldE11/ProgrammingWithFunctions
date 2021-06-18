def main():
    student_dict = {}

    with open("students.csv", "rt") as students_file:
        next(students_file)
        # Read the contents of the text
        # file one line at a time.
        for line in students_file:
            student_info = line.strip().split(",")
            student_dict[student_info[0]] = student_info[1]
    
    search(student_dict)

def search(dictionary):
    num = input("Please enter an I-Number (xxxxxxxxx): ")
    
    if num in dictionary.keys():
        name = dictionary.get(num)
        print(name)
    else:
        print("No such student")

main()