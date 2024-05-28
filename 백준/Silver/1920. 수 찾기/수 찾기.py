n = int(input())  # 5
listN = list(map(int, input().split()))

m = int(input())  # 5
listM = list(map(int, input().split()))
listN = set(listN)

answer = []
for numM in listM:
    if numM in listN:
        answer.append(1)
    else:
        answer.append(0)

for a in answer:
    print(a)
