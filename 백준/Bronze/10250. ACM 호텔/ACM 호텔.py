n = int(input())


def find_room(h, w, man):
    floor = man % h  # 층 번호 계산
    room_number = (man // h) + 1  # 호실 번호 계산
    if floor == 0:  # 손님이 층의 끝에 배정될 때
        floor = h
        room_number -= 1
    return (floor * 100) + room_number


for _ in range(n):
    h, w, man = list(map(int, input().split()))
    print(find_room(h, w, man))
