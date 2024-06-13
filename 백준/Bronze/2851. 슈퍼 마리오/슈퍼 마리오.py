total = 0
nums = []
for i in range(10):
    nums.append(int(input()))

abs_sums = []
sums =[]
for i in range(10):
    total += nums[i]
    sums.append(total)
    abs_sums.append(abs(100 - total))

min_abs = min(abs_sums)
answer = []
for index, value in enumerate(abs_sums):
    if value == min_abs:
        answer.append(sums[index])

print(max(answer))