# take name and roll no, then generate a username using the first 3 letters and last 2 digits of roll number

name = input()
roll = input()

print(name[0]+name[1]+name[2]+roll[-2]+roll[-1])
