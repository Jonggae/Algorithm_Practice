word = input().strip().upper()
dic = {}

for k in word:
    if k in dic.keys():
        dic[k] += 1
    else:
        dic[k] = 1

max = max(dic.values())

answer = []
for value in dic.keys():
    if dic[value] == max:
        answer.append(value)

if not len(answer) == 1:
    print("?")
else:
    print(answer[0])