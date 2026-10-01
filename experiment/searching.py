# python program to perform searching activity using linear and binary search
# python program to perform searching activity using linear and binary search

data = list(map(int, input("Enter the elements: ").split()))

target = int(input("Enter the target: "))

# Linear Search
linear_index = -1

for i in range(len(data)):
    if data[i] == target:
        linear_index = i
        break

if linear_index == -1:
    print(f"Target {target} not found using Linear Search")
else:
    print(f"Target {target} found at index {linear_index} using Linear Search")


# Binary Search
data.sort()

low = 0
high = len(data) - 1
binary_index = -1

while low <= high:
    mid = (low + high) // 2

    if data[mid] == target:
        binary_index = mid
        break
    elif data[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if binary_index == -1:
    print(f"Target {target} not found using Binary Search")
else:
    print(f"Target {target} found at index {binary_index} using Binary Search")

print("Sorted data:", data)