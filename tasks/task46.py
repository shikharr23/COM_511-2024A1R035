# password validation system

password = input()

while len(password) < 8 or '@' not in password:
    print("Wrong, try again")
    password = input("Enter password again:")
print("Password Accepted")