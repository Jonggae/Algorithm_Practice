import itertools

# 시는 01~12, 분은 00 ~ 59, 초는 00 ~ 59

times = list(map(int, (input().split(":"))))

clock = itertools.permutations(times)
filtered_clock = filter(lambda num: 1 <= num[0] <= 12 and 0 <= num[1] <= 59 and 0 <= num[2] <= 59, clock)

count = 0
for i in filtered_clock:
    count+=1
print(count)