import sys
n = int(input())
coordinates = list(map(int, sys.stdin.readline().split()))

set_coord = sorted(set(coordinates))

coord_index_dict = {}
for index, value in enumerate(set_coord):
    coord_index_dict[value] = index

indices = [str(coord_index_dict[i]) for i in coordinates]


print(*indices)
