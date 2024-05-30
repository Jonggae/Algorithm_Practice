n = int(input())

# 확장자를 딕셔너리에 저장하려한다. 확장자가 나타난 횟수만큼 value를 올리면 될듯
dic = {}
extension = []

for _ in range(n):
    name, e = input().split(".")
    extension.append(e)
extension = sorted(extension)

# 모든 확장자를 사전순으로 저장
# 각 확장자의 등장 횟수를 dic으로 저장
for key in extension:
    if key in dic.keys():
        dic[key] += 1
    else:
        dic[key] = 1
# 키와 밸류를 출력
for key in dic.keys():
    print(key,dic[key])