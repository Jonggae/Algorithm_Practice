M, D = map(int, (input().split()))

month31 = [3, 5, 7, 8, 10, 12]
month30 = [4, 6, 9, 11]

def days_count(num):
    days = 0
    while num != 0:
        if num-1 in month31:
            day = 31
            days += day
        elif num-1 in month30:
            day = 30
            days += day
        elif num-1 == 2:
            day = 28
            days += day
        elif num-1 == 1:
            day = 31
            days += day
        elif num-1 == 0:
            day = 0
            days+=day
        num -= 1
    return days

result = days_count(M) + D-1
answer = result % 7
if answer == 0:
    print("MON")
elif answer == 1:
    print("TUE")
elif answer == 2:
    print("WED")
elif answer == 3:
    print("THU")
elif answer == 4:
    print("FRI")
elif answer == 5:
    print("SAT")
elif answer == 6:
    print("SUN")
