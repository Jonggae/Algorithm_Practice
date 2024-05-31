import itertools
n, m = map(int, input().split())

# append를 사용하면 시간이 걸리지 않을까?
nums = []

for i in range(1, n + 1):
    nums.append(str(i))

C = itertools.combinations(nums, m)
for i in C:
    print(' '.join(i))