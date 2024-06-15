t = int(input())  # 테스트 케이스 수

room_address = []  # [0]층, [1]호
for i in range(t):
    floor = int(input())
    room = int(input())
    room_address.append([floor, room])


# 아래층의 n호 까지 사람 수의 합
# 0층은 1, 2, 3 명
# 누적 합을 여러번 구함
def find_total_man(k, n, floor=0, man_list=None):  # k층 n호의 인간

    if man_list is None:
        man_list = list(range(1, n + 1))
    if floor == k:
        return man_list

    total_man = []
    for i in range(1, n + 1):
        total_man.append(sum(man_list[:i]))

    return find_total_man(k, n, floor + 1, total_man)


for i in range(t):
    answer = find_total_man(room_address[i][0], room_address[i][1])
    print(answer[room_address[i][1]-1])
