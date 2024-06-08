import sys

n = int(input())

input = sys.stdin.readline

score = {}
for i in range(1, n + 1):
    data = list(map(int, (input().split())))
    score[i] = max(data[0:2]) + sum(sorted(data[2:7], reverse=True)[0:2])

print(max(score.values()))
