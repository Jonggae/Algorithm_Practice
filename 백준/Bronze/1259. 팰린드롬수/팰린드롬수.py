import sys
nums = []
backNums = []
for num in sys.stdin:
    num = num.strip()

    if num == "0":
        break
    nums.append(num)
    backNums.append(num[::-1])

i = 0
while i < len(nums):
    if nums[i] == backNums[i]:
        print("yes")
        i += 1
    else:
        print("no")
        i += 1

