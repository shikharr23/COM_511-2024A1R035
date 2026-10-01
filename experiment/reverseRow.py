n, m = map(int, input().split())

matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

k = int(input())

for i in range(k-1, n, k):
    matrix[i].reverse()

for row in matrix:
    print(row)
