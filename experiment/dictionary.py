# program to create records of n students. store each student record as a dictionary containing roll number , name , branch, and marks . store all records in a list and search for a  student using roll number ( roll no must be unique )


n = int(input("Enter number of students: "))

students = []

for i in range(n):
    print(f"\nEnter details of student {i + 1}")

    roll = int(input("Enter roll number: "))

    name = input("Enter name: ")
    branch = input("Enter branch: ")
    marks = float(input("Enter marks: "))

    student = {
        "roll": roll,
        "name": name,
        "branch": branch,
        "marks": marks
    }

    students.append(student)

search_roll = int(input("\nEnter roll number to search: "))

found = False

for student in students:
    if student["roll"] == search_roll:
        print("\nStudent found")
        print("Roll Number:", student["roll"])
        print("Name:", student["name"])
        print("Branch:", student["branch"])
        print("Marks:", student["marks"])
        found = True
        break

if found == False:
    print("Student not found")