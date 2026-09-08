# take email and print domain

email = input("Enter email: ")
domain = email.split("@")[1]

print(domain)