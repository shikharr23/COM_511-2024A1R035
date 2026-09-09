"""WAP to input four numbers from the user and find the greatest number among them"""

for i in range(4):
    number=int(input("Enter a number: "))
    if i == 0:
        greatest = number
    elif number > greatest:
        greatest = number
print("The greatest number is:", greatest)