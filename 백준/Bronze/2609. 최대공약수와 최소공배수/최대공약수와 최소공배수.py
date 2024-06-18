a, b = map(int, input().split())


def lcm(a, b):
    return abs(a *b) // gcd(a,b)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(a,b))
print(lcm(a,b))
