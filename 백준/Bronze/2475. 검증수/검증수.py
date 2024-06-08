nums = list(map(int,(input().split())))

answer = 0

for n in nums:
    answer +=n**2

print(answer%10)