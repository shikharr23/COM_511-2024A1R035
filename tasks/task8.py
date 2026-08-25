# calculate SI and Total amount using Principal, rate and time entered by the user

p = int(input())
r = int(input())
t = int(input())\

si = (p*r*t)/100
ta = p + si

print("Simple Interest:", si)
print("Total Amount:", ta)
