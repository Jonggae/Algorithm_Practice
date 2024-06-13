n = int(input())
k = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))


# 입력끝

# n개의 카드 중 k개를 선택하여 가로로 나란히 정수를 만든다.

# itertool없이?
# 이게 itertool과 같음
def permute_k_elements(nums, k):
    def backtrack(path, options):
        if len(path) == k:
            result.append(path)
            return
        for i in range(len(options)):
            backtrack(path + [options[i]], options[:i] + options[i + 1:])

    result = []
    backtrack([], nums)
    return result


answer = set()
permute = permute_k_elements(nums, k)

for p in permute:
    s = ''.join(map(str, p))
    answer.add(s)

# 결과 출력
print(len(answer))