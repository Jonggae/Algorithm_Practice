n = int(input())
shop = list(map(int, input().split()))


def drink_milk(shop):
    me = 0
    count = 0

    for i in range(len(shop)):
        if shop[i] == me:
            count += 1
            me += 1
            if me > 2:
                me = 0
       
    return count


print(drink_milk(shop))