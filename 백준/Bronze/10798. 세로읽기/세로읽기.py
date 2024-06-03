import sys
n = 5
arr = [list(sys.stdin.readline().strip()) for _ in range(n)]

# 입력 행렬의 최대 열 값을 구한다.
max_col = 0
for i in range(5):
    if max_col <= len(arr[i]):
        max_col = len(arr[i])

arr_fill = [["*"] * max_col for _ in range(n)]

for i in range(n):
    for j in range(max_col):
        try:
            arr_fill[i][j] = arr[i][j]
        except IndexError:
            arr_fill[i][j] = arr_fill[i][j]

val = []
for i in range(max_col):
    for j in range(n):
        val.append(arr_fill[j][i])

answer = str(''.join(val))

print(answer.replace("*", ""))
