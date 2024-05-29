n = int(input())

i = 1
while i < 2 * n:
    if i <= n:  # 1, 2, 3, 4, 5
        star = '*' * i
        print(star.ljust(n, ' ') + (star.rjust(n, ' ')))
        i += 1
    else:  # 6, 7, 8, 9
        star = '*' * (2 * n - i)
        print(star.ljust(n, ' ') + (star.rjust(n, ' ')))
        i += 1