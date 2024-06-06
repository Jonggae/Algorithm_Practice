n = int(input())
letters = list(input())


def char_to_num(char):
    return ord(char) - 96


def find_hash(nums):
    r = 31
    hash = 0
    m = 1234567891
    for i in range(len(nums)):
        hash += nums[i] * r ** i
    return hash % m


nums = []

for char in letters:
    nums.append(char_to_num(char))

print(find_hash(nums))