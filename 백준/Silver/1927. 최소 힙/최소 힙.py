import sys
from heapq import *

n = int(input())
nums = list(int(sys.stdin.readline().strip()) for _ in range(n))

heap = []
for i in range(n):
    if nums[i] == 0:
        if heap:
            print(heappop(heap))
        else:
            print(0)
    else:
        heappush(heap, nums[i])