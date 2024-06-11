import sys

from heapq import *
t = int(input())

def sum_cost(file_size):
    total_cost = 0
    heapify(file_size)

    while len(file_size) > 1:
        a = heappop(file_size)
        b = heappop(file_size)

        cost = a + b
        total_cost += cost

        heappush(file_size, cost)

    return total_cost

for _ in range(t):
    chapter = int(input())
    file_size = list(map(int, (sys.stdin.readline().split())))
    print(sum_cost(file_size))
