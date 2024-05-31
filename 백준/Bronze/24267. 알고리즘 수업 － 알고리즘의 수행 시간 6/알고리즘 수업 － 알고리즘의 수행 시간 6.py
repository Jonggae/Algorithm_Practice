n = int(input().strip())
def series(k):
    return k*(k+1)//2

answer= 0
for i in range(1,n-1):
    sum = series(i)
    answer += sum
print(answer)
print(3)