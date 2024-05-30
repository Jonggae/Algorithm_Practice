word = input()
length = len(word)

answerSet = set()

# 완전 탐색으로 모든 길이의 단어를 set에 저장하여 set의 길이를 반환

def partial_word(str):
    l = len(str)
    for i in range(l):
        for j in range(i + 1, l + 1):
            answerSet.add(str[i:j])
partial_word(word)

print(len(answerSet))
