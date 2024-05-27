import sys

for info in sys.stdin:
    info = info.strip()

    if info == "# 0 0":
        break

    name = list(map(str, info.split()))
    
    if int(name[1]) >17 or int(name[2]) >=80:
        print(name[0], "Senior")
    else:
        print(name[0], "Junior")