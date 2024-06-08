nums = []
for _ in range(10):
    nums.append(int(input()))
set = set()
for num in nums:
    set.add(num%42)

print(len(set))