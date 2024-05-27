import sys

count = 0
for line in sys.stdin:

    line = line.strip()
    if line == "#":
        break
    charList = list(line.lower())

    for c in charList:
        if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
            count += 1
    print(count)
    count = 0