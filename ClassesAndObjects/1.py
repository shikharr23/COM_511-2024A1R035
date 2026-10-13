# Create a class and object : Student details
# Problem : Create a Student class to store student details like name, and roll number. 

class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        
student1 = Student("Nikka", 81)
student1.display_details()


