n = int(input())
nums = list(map(int, (input().split())))


def prime(n):  # n이 소수인가 아닌가
    div = []
    for a in range(2, n + 1):
        if n % a == 0:
            div.append(a)
    if len(div) == 1:
        return True
    else:
        return False

count = 0
for n in nums:
    if prime(n) == True:
        count+=1
print(count)