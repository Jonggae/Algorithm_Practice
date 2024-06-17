import itertools
nums = list(map(int, input().split()))

def find_lcm(a, b):
    return abs(a * b) // find_gcd(a, b)

def find_three_lcm(a,b,c):
    return find_lcm(find_lcm(a,b),c)

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


three_nums = itertools.combinations(nums, 3)
answer = []
for i in three_nums:
    answer.append(find_three_lcm(i[0],i[1],i[2]))

print(min(answer))