# WAP to store multiple student data in tuple , each one contains name, roll number , marks. Display who score above 75

students = (
    ("Kaka", 101, 81),
    ("Aman", 102, 68),
    ("Riya", 103, 91),
    ("Priya", 104, 74),
    ("Karan", 105, 88)
)
print("Students who scored above 75: ")
for name, roll, marks in students:
    if marks > 75:
        print(name, roll, marks)
    
          
