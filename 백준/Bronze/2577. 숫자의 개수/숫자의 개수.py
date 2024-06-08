num = 1
count = [0]*10

for _ in range(3):
    num *= int(input().strip())

number = str(num)

for char in number:
    count[int(char)] +=1

for i in count:
    print(i)