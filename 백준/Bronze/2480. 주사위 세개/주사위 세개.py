a, b, c = map(int, input().split())

list = [a, b, c]
max = 0

for num in list:
    if max < num:
        max = num

if a == b and b == c:
    print(10000 + a * 1000)
elif a == b:
    print(1000 + a * 100)
elif b == c:
    print(1000 + b * 100)
elif a == c:
    print(1000 + a * 100)

else:
    print(max*100)