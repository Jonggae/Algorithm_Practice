import sys
input = sys.stdin.read
data = list(map(int, input().split()))
test_case = data[0]
stones = data[1:]

def max_steps(n):
    left, right = 1, n
    answer = 0

    while left<=right:
        mid = (left+right)//2
        sum_mid = mid * (mid+1) //2

        if sum_mid <= n:
            answer = mid
            left = mid +1
        else:
            right = mid-1

    return answer

for n in stones:
    print(max_steps(n))