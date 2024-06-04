
target_address = input().split(":")

def ip_address(address):
    blank = 0
    code = 0
    for i in target_address:
        if not "" == i:
            code += 1
    blank = 8 - code
    return blank, code


zero = ip_address(target_address)[0]

origin = []
for i in target_address:
    if not i == "":
        origin.append(i)
    else:
        while zero != 0:
            origin.append("0000")
            zero -= 1
answer = []
for i in range(len(origin)):
    if len(origin[i]) != 4:
        answer.append(origin[i].zfill(4))
    else:
        answer.append(origin[i])


print(':'.join(answer))
