# take password and check if this contains @ and has atleast 8 character

password = input()

print(password.find("@") and len(password) >= 8)    

