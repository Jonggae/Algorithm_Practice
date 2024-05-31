import sys
n = int(input().strip())

count = 0
set = set()
for _ in range(n):
    line = sys.stdin.readline().strip()
    if not line == "ENTER":
        set.add(line)
        

    else:
        count += len(set)
        
        set.clear()

count += len(set)

print(count)