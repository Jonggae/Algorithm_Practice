name = list(input().split("-"))
answer = []

for cap in name:
    answer.append(cap[0])

print(''.join(answer))