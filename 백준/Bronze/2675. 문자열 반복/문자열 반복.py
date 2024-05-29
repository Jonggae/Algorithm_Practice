n = int(input())

# 반복할 횟수와 문자열을 분리하여 저장
# 문자열을 문자 하나씩 반복 횟수만큼 반복하여 출력
# input은 string 이므로 반복 횟수는 int로 저장해야 함
#

for _ in range(n):
    repeat, word = input().split()
    repeat = int(repeat)

    result = []
    # 문자를 횟수만큼 반복하여 result에 저장하게 됨
    for char in word:
        result.append(char*repeat)
    # list의 값으로 저장되어 있으므로 ''.join을 통해 붙여서 출력함
    answer = ''.join(result)

    print(answer)
