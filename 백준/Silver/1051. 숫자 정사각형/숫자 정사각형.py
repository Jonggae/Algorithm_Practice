n, m = map(int, input().split())
max_length = min(n, m)  # 정사각형 한변의 최대 길이
numbers = [input().strip() for _ in range(n)]
def square(numbers, n, m):
    max_size = 0
    for size in range(1, max_length + 1):
        for i in range(n - size + 1):
            for j in range(m - size + 1):
                if numbers[i][j] == numbers[i][j + size - 1] == numbers[i + size - 1][j] == numbers[i + size - 1][
                    j + size - 1]:
                    max_size = max(max_size, size)
    return max_size

print(square(numbers,n,m)**2)