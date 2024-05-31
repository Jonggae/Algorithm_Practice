import sys

n, m = map(int, input().split())

hear = []
set = set()
answer = []
for _ in range(n):
    name = sys.stdin.readline().strip()
    set.add(name)
for _ in range(n, n + m):
    name = sys.stdin.readline().strip()
    if name in set:
        answer.append(name)

print(len(answer))

print('\n'.join(sorted(answer)))