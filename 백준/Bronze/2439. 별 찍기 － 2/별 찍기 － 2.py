n = int(input())

t = 0
star = "*"
while t < n:
    print(star.rjust(n))
    star = star+"*"
    t += 1