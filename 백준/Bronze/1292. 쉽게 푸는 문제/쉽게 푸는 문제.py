a, b = map(int, input().split())


def find_number(b):
    for i in range(1, b + 1):
        if i * (i - 1) // 2 < b <= i * (i + 1) // 2:
            return i

total_sum = 0
for n in range(a, b + 1):
    total_sum += find_number(n)

print(total_sum)
