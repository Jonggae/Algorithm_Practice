n = int(input())
series = list(map(int, input().split()))


# 부분 수열은 순서를 유지해야 한다.
#

def decrease_series(series):
    n = len(series)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i): # i까지의 수열
            if series[j] > series[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
# dp 배열의 값들은 각 위치[i]에서 끝나는 가장 긴 감소하는 부분 수열의 길이
# i 이전의 모든 원소들(j)을 살펴보면서, series[j]>series[i]인 경우에만
# 즉 감소하는 수열일때만 dp[i]를 갱신신# 수열의 '길이'를 구하면 되는것이므로.

print(decrease_series(series))