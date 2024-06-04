word = list(input().strip())
alpha = [chr(a) for a in range(97, 123)]

idx = []
idx_word = []
for char in word:
    idx.append(alpha.index(char))
    idx_word.append(word.index(char))

for i in range(len(idx_word)):
    alpha[idx[i]] = idx_word[i]

for i in range(len(alpha)):
    if type(alpha[i]) == str:
        alpha[i] = -1

print(*alpha)
