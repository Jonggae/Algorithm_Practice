n, m = map(int, input().split())

arr1 = [list(map(int, input().split())) for _ in range(n)]

arr2 = [list(map(int, input().split())) for _ in range(n)]

sum_arr = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        sum_arr[i][j] = arr1[i][j] + arr2[i][j]

for i in range(n):
    print(*sum_arr[i])
