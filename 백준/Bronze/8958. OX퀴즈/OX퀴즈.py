
n = int(input().strip())
oxs = [input().strip() for _ in range(n)]

point = 0
temp = 0
answer = []
for ox in oxs:
    for char in ox:
        if char == "O":
            temp += 1
            point +=temp
        else:
            temp = 0
    answer.append(point)
    point = 0
    temp = 0

for i in answer:
    print(i)