a, b = map(int, (input().split()))
c = int(input().strip())
d = int(input().strip())


def f(n):
    return a * n + b


def g(k):
    return k

boolean = True
for i in range(d,d+1000):
    if f(i) > c * g(i):
        boolean = False
        break

if boolean:
    print(1)
else:
    print(0)