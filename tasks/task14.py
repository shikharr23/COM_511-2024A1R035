# takes rupees and notes and calculate how many notes of 500 and 100 are needed

amount = int(input())

fiveHun = amount//500
amount%=500
oneHun = amount//100

print(f"500 notes : {fiveHun} and 100 notes : {oneHun}")
