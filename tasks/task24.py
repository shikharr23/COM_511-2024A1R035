# fill in the given template with name and date
letter = '''
Dear <Name>,
You are selected!
<Date>
'''

name = input()
date = input()

# print(f"Dear {name}\nYou are selected!\n{date}")


letter = letter.replace("<Name>", name)
letter = letter.replace("<Date>", date)

print(letter)
