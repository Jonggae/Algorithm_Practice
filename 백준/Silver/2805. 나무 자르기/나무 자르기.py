import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
m = int(data[1])
trees = list(map(int, data[2:]))


def wood_cut(trees, height):# 해당 톱으로 자른 나무 길이의 합
    wood_h = 0
    for tree in trees:
        if tree > height:
            wood_h += tree-height
    return wood_h

def saw_height(trees, m):
    low, high = 0, max(trees)
    result = 0

    while low <= high:
        mid = (low + high) // 2
        if wood_cut(trees, mid) >= m:
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return result


print(saw_height(trees, m))
