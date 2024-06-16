import math
n = int(input())

fact = math.factorial(n)

i = 0
count = 0
while True:
    val = fact % 10 ** i
    if val == 0:
        count += 1
        i += 1
    else:
        break
print(count-1)
