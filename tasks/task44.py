""" Write a python program to determine whether a student is eligible for a scholarship
a) The student has a CGPA of 8.5 or above and attendance of 85 percent or above.
b) The student has won a national-level competition.
The program should take CGPA, attendance percentage, and national-level competition status as input, then display whether the student is eligible for the scholarship"""
cgpa = float(input("Enter your CGPA : "))
attendance = int(input("Enter Attendance: "))
status = input("Enter national-level competition status : ").strip().lower()
flag = False
if(status == "true"):
    flag = True
if(cgpa>=8.5 and attendance>=85 or flag):
    print("Eligible for Scholarship")
else:
    print("Not eligible")