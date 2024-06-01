n, b = input().split()
b = int(b)

ints = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def charToNum(str):
    if str in ints:
        return int(str)
    else:
        return ord(str) - 55


def changeDigit(nums, k):
    sum = 0
    a = len(nums)
    for i in range(a):
        sum += nums[i] * (k **(a-1- i))
    return sum


arr = []

if b > 10:
    for char in n:
        arr.append(charToNum(char))

else:
    for num in n:
        arr.append(int(num))

print(changeDigit(arr, b))