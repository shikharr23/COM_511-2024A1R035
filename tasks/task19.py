# 3 sub marks out of 100. true if atleast 40 in all 3 avg is atleast 50

a = int(input())
b = int(input())
c = int(input())

avg = (a+b+c)//3
print(a >= 40 and b >= 40 and c >= 40 and avg >= 50)


