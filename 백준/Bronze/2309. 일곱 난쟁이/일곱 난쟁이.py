from itertools import *

height = list(int(input()) for _ in range(9))
sum_height = sum(height)


# 조합? 으로 7개를 선택하여 100이되는 경우를 찾아본다?

answer = list(combinations(height, 2))

for c in answer:
    if sum(c) == sum_height - 100:
        height.remove(c[0])
        height.remove(c[1])
        
        break
ans = sorted(height)
for i in ans:
    print(i)
