# take 2 input and swap value using temp var

a = int(input())
b = int(input())

print(f"Original value - a : {a} and b : {b} ")

temp = a
a = b
b= temp

print(f"Updated Values - a : {a} and b : {b}")