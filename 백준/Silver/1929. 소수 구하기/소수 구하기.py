m, n = map(int, input().split())

def check_prime(n):
    if n <= 1:
        return False

    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False
    # 5부터 시작하여 n
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

for i in range(m, n+1):
    if check_prime(i):
        print(i)