n = int(input())  # 방의 크기 N (1~100)

room = [list(input().strip()) for _ in range(n)]

# 가로, 세로의 누울 자리를 구하기 위해서 2차원으로 저장함
# 어느 위치든 2칸 이상만 있으면 누울 수 있음. * 짐이 중앙에 있는 경우는 1자리가 아닐 수 있다.
# 모든 방을 일렬로 정렬한 뒤, X와 n칸 마다 나누면서 체크해보자

# 가로
room_width = [''.join(room[i]) for i in range(n)]
# 세로 - zip을 이용하여 병렬로 읽은 값을 다시 배열로 만듦
room_height = [''.join(row) for row in zip(*room)]  # 이 방법을 잘 알아두자


# 점 들을 묶어서 다시 배열로 만드는 함수
def group_dots(row):
    grouped = []
    current_char = ''

    for char in row:
        if (char == '.'):
            current_char += char
        else:
            if current_char:
                grouped.append(current_char)
                current_char = ''
    if current_char:
        grouped.append(current_char)
    return grouped

room_width_2 = [group_dots(row) for row in room_width]
room_height_2 = [group_dots(row) for row in room_height]
width = [item for sublist in room_width_2 for item in sublist]
height = [item for sublist in room_height_2 for item in sublist]

a = 0
b = 0
for i in range(len(width)):
    if ".." in width[i]:
        a += 1
for i in range(len(height)):
    if ".." in height[i]:
        b += 1

print(a, b)

