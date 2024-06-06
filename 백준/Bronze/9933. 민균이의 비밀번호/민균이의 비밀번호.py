import sys

n = int(input())
password = list(sys.stdin.readline().strip() for _ in range(n))

dict = {}
revers_dict = {}
target_word = ""

for word in password:
    if word[::-1] in password:
        target_word = word
        break
    elif word[::-1] == word:
        target_word = word
        break

print(len(word),word[len(word)//2])