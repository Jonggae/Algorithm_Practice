
n = int(input())
exchange = 1000 - n

count = 0
while exchange != 0:
    if exchange >= 500:
        exchange -= 500
        count += 1
    elif 100 <= exchange < 500:
        exchange -= 100
        count+=1
    elif 50<= exchange <100:
        exchange -=50
        count+=1
    elif 10<= exchange <50:
        exchange-=10
        count +=1
    elif 5<= exchange < 10:
        exchange -= 5
        count+=1
    elif 1<= exchange <5 :
        exchange -=1
        count+=1

print(count)
