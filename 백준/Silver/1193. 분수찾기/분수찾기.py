n = int(input())

def series(n):
    return n * (n + 1) / 2
def find_number_position(n):
    a = 0
    while True:
        a += 1
        if n <= series(a):
            break
    return a, int(n - series(a - 1))
def find_index(i, k):
    if i % 2 == 0:
        return k - 1, i - k
    else:
        return i - k, k - 1
    
first, second = find_number_position(n)
# 분자와 분모를 구하여 할당
up, down = find_index(first, second)
# 분모 분자 1씩 더하여 정답 생성
up = str(up+1)
down = str(down+1)
print(up+"/"+down)