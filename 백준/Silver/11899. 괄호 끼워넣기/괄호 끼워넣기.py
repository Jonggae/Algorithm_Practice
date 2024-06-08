import sys
paren = list(sys.stdin.readline().strip())

stack = []
surplus_paren = []

for p in paren:
    if p == "(":
        stack.append(p)
    elif p == ")":
        if stack:
            if stack[-1] == "(":
                stack.pop()
            else:
                stack.append(p)
        else:
            stack.append(p)

print(len(stack))