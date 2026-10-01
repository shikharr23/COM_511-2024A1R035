"""
create a database using lists and tuples . each student record must contain roll number , name , branch , and cgpa . store each record as a tuple inside a list  display all records and search for student using roll numbr 
conditions:
- each record should be stores as a tuple
- the complete database should be stored as a list
- roll numbers must be unique
"""


n = int(input("Enter number of students: "))

database = []

for i in range(n):
    print(f"\nEnter details of student {i + 1}")

    roll = int(input("Enter roll number: "))

    while roll in [student[0] for student in database]:
        print("Roll number already exists. Enter a unique roll number.")
        roll = int(input("Enter roll number: "))

    name = input("Enter name: ")
    branch = input("Enter branch: ")
    cgpa = float(input("Enter CGPA: "))

    student = (roll, name, branch, cgpa)

    database.append(student)

print("\nAll Student Records:")

for student in database:
    print(student)

search_roll = int(input("\nEnter roll number to search: "))

found = False

for student in database:
    if student[0] == search_roll:
        print("\nStudent found")
        print("Roll Number:", student[0])
        print("Name:", student[1])
        print("Branch:", student[2])
        print("CGPA:", student[3])
        found = True
        break

if found == False:
    print("Student not found")