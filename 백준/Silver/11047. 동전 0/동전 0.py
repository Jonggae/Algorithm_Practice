import sys
n, k = list(map(int, input().split()))
coins = []
for i in range(n):
    coins.append(int(sys.stdin.readline().strip()))

def solution(coins, k):
    cnt = 0
    while k > 0:
        if max(coins) <= k:
            cnt += k // max(coins)
            k = k % max(coins)
            coins.remove(max(coins))
        else:
            coins.remove(max(coins))
    return cnt

print(solution(coins,k))