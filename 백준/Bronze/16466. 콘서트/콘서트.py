from heapq import *

n = int(input())
tickets = list(map(int, (input().split())))
heapify(tickets)

if tickets[0] > 1: # 최소가 1이 아니면 1이 정답
    print(1)
else:  # 최소값이 1이라는 뜻
    back = 0
    while tickets:
        a = heappop(tickets)
        if a - back == 1:
            back = a

        else:
            print(back+1)
            break
    if len(tickets) == 0:
        print(a+1)
