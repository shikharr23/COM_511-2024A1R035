
"""WAP to input marks of 5 students
for each student, the program should check whteher the entered marks are valid or invalid.
Marks are considered valid only if they are between 0 and 100. If the marks are invalid, the program
should display "invalid marks skipped " and move to the net student without printing those marks

if the marks are valid, the program should display the marks are valid.
"""

for i in range(5):
    marks=int(input())
    if marks>=0 and marks<=100:
        print("Marks are valid: ",marks)
    else:
        print("Invalid marks skipped")

