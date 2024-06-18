import sys
n = int(input())
k = int(input())
sensor = sorted(list(map(int,sys.stdin.readline().split())))

diff = []
if n == 1:
    print(0)
    sys.exit()

for i in range(1, n):
    diff.append(sensor[i] - sensor[i-1])

diff.sort()

for _ in range(k-1):
    diff.remove(diff[-1])
print(sum(diff))