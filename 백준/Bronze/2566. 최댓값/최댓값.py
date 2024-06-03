import sys
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

max = 0
a = 0
b = 0

for i in range(9):
    for j in range(9):
        if arr[i][j] >= max:
            max = arr[i][j]
            a = i+1
            b = j+1

print(max)
print(a, b)