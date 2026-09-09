# bill amount as input and apply a discount 

bill = int(input())

if bill > 5000:
    dis = bill * 20 / 100
    print("Total amount:", bill)
    print("discount:",dis)
elif bill >= 3000 and bill <= 5000:
    dis = bill * 10 / 100
    print("Total:",bill)
    print("Discount:",dis)
else:
    print("No discount")
    print("Total amount:",bill)