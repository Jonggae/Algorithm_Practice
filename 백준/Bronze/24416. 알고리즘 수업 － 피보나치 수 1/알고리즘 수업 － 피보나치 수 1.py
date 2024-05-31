
k = int(input().strip())


# 아래 동적 프로그래밍을 이용함

def fib(n):
    if n == 1 or n == 2:
        return 1

    f = [0] * (n + 1)
    f[1], f[2] = 1, 1

    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]

    return f[n]


print(fib(k))
print(k - 2)
