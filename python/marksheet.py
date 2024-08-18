import sys


# Funtion for taking list of subjects
def get_subjects(subject: int) -> list[str]:
    sub = []
    for i in range(subject):
        subjs = input("Enter the subjects: ")
        #Checks for numerical input
        if not subjs.isalpha():
            print("Name of Subjects should be in alphabetical characters.")
            sys.exit("Invalid Entry") #Exits the program if condition meets
        sub.append(subjs)
    return sub


# Funtion for taking list of students
def get_student(students: int) -> list[str]:
    stu = []
    for i in range(students):
        stud = input("Enter the name of student: ")
        #Checks for numerical input
        if not stud.isalpha():
            print("Name of Subjects should be in alphabetical characters.")
            sys.exit("Invalid Entry")
        stu.append(stud)
    return stu


#For taking marks and calculating percentage and giving output
def marksheet(students: list[str], subjects: list[str]) -> list[int]:
    percentage = []
    for i in range (len(students)):
        add = 0
        for j in range(1, len(subjects)+1):
            add += int(input(f"enter marks of {students[i]} in {subjects[j-1]}: ")) 
            total = (100 * j) 
        per = int((add/total)*100)
        percentage.append(per)

        if percentage[i] >= 40:
            print(students[i], " is passed.")
        else:
            print(students[i], " is failed.")


# Main function
try:
    n = int(input("How many students: "))
    if n < 1:
        print("Number of students must be more than 0")
        sys.exit("Invalid Entry")
    s = int(input("How many subjects: "))
    if s < 1:
        print("Number of subjects must be more than 0")
        sys.exit("Invalid Entry")
    
except NameError:
    print("Number of student and subjects should be positive integer.")
    sys.exit("Invalid Entry")
except ValueError:
    print("Number of student and subjects should be positive integer.")
    sys.exit("Invalid Entry")

name_of_students = get_student(n)
name_of_subjects = get_subjects(s)

print(marksheet(name_of_students, subjects = name_of_subjects))
