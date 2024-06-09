
a = int(input())
b = int(input())
c = int(input())


def first_way(a, b, c):
    return a + b - c

def second_way(a,b,c):
    ab = str(a)+str(b)
    return int(ab)-c

print(first_way(a,b,c,))
print(second_way(a,b,c,))