import sys
n = int(input())
words = [sys.stdin.readline().split() for _ in range(n)]

# 각 단어의 배열을 반대로 만들기 reverse 를 써도 되는가?
# 스택을 쓸 것인가?
reversed_word = [[] for _ in range(n)]

# 새로운 배열에 각 단어의 순서를 뒤집은 배열을 다시 넣음.
for i in range(n):
    for j in range(len(words[i])):
        if len(words[i]) != 0:
            reversed_word[i].append(words[i].pop())


for i in range(n):
    print(f"Case #{i+1}:",*reversed_word[i])