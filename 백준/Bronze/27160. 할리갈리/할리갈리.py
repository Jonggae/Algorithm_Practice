n = int(input())
dic = {}
for _ in range(n):
    fruit, num = input().split()
    num = int(num)

    if fruit in dic.keys():
        dic[fruit] += num
    else:
        dic[fruit] = num

if any(count == 5 for count in dic.values()):
    print("YES")
else:
    print("NO")
