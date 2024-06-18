import math

a, b, v = map(int, input().split())

def days(up, down, goal, day=0):
    if up>=goal:
        return 1

    day_up = up-down
    day = (goal-up) / day_up

    return math.ceil(day)+1

print(days(a,b,v))