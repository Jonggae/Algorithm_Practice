import itertools
import sys

n, m = map(int, input().split())

cards = list(map(int, (input().split())))
# 카드 3개를 뽑아서 m에 최대한 가까운 수가 되어야한다.
# for로 완전탐색을 하면 시간이 오래 걸릴 것 같은데..
# 어차피 중복이 없으므로 그냥해보자

nums = itertools.combinations(cards, 3)
filtered_nums = filter(lambda combo: sum(combo) <= m, nums)

max_num = max(filtered_nums, key=sum)

print(sum(max_num))
