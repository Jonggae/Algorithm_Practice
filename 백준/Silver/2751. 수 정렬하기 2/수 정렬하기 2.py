import sys
n = int(input())

numbers = []
for nums in sys.stdin:
    nums = nums.strip()
    numbers.append(int(nums))
numbers.sort()
for nums in numbers:
    print(nums)