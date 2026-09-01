# without using 3rd variable

a = int(input())
b = int(input())

print(f"Original Value - a : {a} and b : {b}")

a = a + b
b = a - b
a = a - b

print(f"After swapping - a : {a} and b : {b}")

