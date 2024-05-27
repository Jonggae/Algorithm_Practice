import sys
n = int(sys.stdin.readline().strip())

for _ in range(n):
    line = sys.stdin.readline().strip()
    numbers = list(map(int, line.split()))
    print(sum(numbers))