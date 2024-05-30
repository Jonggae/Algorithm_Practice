n = int(input())

dic = {}

for _ in range(n):
    name, status = input().split()
    dic[name] = status
answer =[]
for n in dic:
    if dic[n] == "enter":
        answer.append(n)

answer = sorted(answer, reverse=True)

for name in answer:
    print(name)