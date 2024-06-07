import sys
input = sys.stdin.read
data = list(map(int, input().split()))

n = data[0]
my_cards = data[1:n + 1]
m = data[n + 1]
check_nums = data[n + 2:n + 2 + m]


# 입력 끝

# nums의 값이 my_cards에 들어있는지 확인 -> 이진탐색
# 이진탐색은 인덱스의 값을넣으므로.. 그것을 고려하여 작성

def binary_search(target, cards):  # cards는 정렬해야함
    min_val = 0
    max_val = len(cards) - 1

    while min_val <= max_val:
        mid_val = (min_val + max_val) // 2

        if cards[mid_val] == target:
            return 1
        elif cards[mid_val] < target:
            min_val = mid_val + 1

        else:
            max_val = mid_val - 1

    return 0

sorted_my_cards = sorted(my_cards)

result = [binary_search(num, sorted_my_cards) for num in check_nums]

print(*result)
