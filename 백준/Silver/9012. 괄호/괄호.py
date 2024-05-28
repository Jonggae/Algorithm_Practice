n = int(input())
paren = []

for _ in range(n):
    p = input().strip()
    paren.append(p)

def validation(par):
    stack = []

    for char in par:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                return "NO"

    return "YES" if not stack else "NO"


for p in paren:
    result = validation(p)
    print(result)