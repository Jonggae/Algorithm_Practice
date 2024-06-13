import math
n = int(input())

def combination(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n-k))

result = combination(n,5)
print(result)