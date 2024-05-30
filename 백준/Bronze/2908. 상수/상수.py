nums = list(input().split())
snums = []
for char in nums:
    char = char[::-1]
    snums.append(int(char))

print(max(snums))