import sys
from heapq import *

n = int(input())
nums = list(int(sys.stdin.readline().strip()) for _ in range(n))

heap = []

for i in range(n):
    if nums[i] == 0:
        if heap:
            print(heappop(heap)[1])
        else:
            print(0)
    else: # 저장할 때 2개를 같이저장할 수 있음.
        heappush(heap, (abs(nums[i]), nums[i]))