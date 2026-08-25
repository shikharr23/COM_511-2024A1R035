#  take 2 digit num and print its sum - 57 = 5+7 = 12

n = int(input())
sum = 0
a = n%10
n//=10
b = n%10
sum = a+b
print(f"Sum of its digits : {sum}")
