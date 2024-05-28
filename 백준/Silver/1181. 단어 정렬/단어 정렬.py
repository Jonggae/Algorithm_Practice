import sys
n = int(sys.stdin.readline())

length = []
words = []
for line in sys.stdin:
    line = line.strip()
    if line == "0":
        break
    words.append(line)

unique = []
seen = set()
for word in words:
    if word not in seen:
        unique.append(word)
        seen.add(word)

unique.sort(key=lambda x: (len(x), x))
for answer in unique:
    print(answer)
