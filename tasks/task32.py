# take 10 digit number and display only last 4 digits . replace the first 6 by ******

num = input()

result = "*" * 6 + num[-4:]

print(result)