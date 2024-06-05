plate = list(input())
n = len(plate)
h = 10
while len(plate) >1:
    if plate[0] == '(':
        if plate[1] == '(':
            h += 5
            plate.pop(0)
        else:
            h += 10
            plate.pop(0)

    else:
        if plate[1] == ')':
            h += 5
            plate.pop(0)

        else:
            h += 10
            plate.pop(0)


print(h)
