n, x = map(int, input().split())
nums = list(map(int, (input().split())))
answer = []
for i in range(n):
    if nums[i]<x:
        answer.append(nums[i])

print(*answer)