import sys

n = int(input())
requests = sorted(list(map(int, sys.stdin.readline().split())))
budget = int(input())


# sum(request)가 budget이하이면 그대로 반환
# sum(request)가 budget 이상일때만 상한을 찾음
# requests를 정렬시켜 놓으면..

def solution():
    avg_budget = budget / n

    if sum(requests) <= budget:
        return max(requests)

    total = 0
    for i in range(n):
        if total + requests[i] * (n - i) > budget:
            return (budget - total) // (n - i)
        total += requests[i]

    return requests[-1]


print(solution())