import sys
n = int(input())
stick = [int(sys.stdin.readline().strip()) for _ in range(n)]

last = stick[-1]
stick.pop()
count = 1

for i in range(n - 2, -1, -1):
    if stick[i] > last:
        count += 1
        last = stick[i]
print(count)