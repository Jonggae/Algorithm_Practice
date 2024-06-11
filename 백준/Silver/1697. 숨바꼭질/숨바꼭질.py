from collections import deque

n, k = map(int, (input().split()))


# 그래프를 어떻게 만들 것인가?

def bfs( start, goal):
    queue = deque([start])
    visited = {start: 0}  # 시작은 거리 0

    while queue:
        current = queue.popleft() # 시작 지점을 방문 처리함

        if current == goal:
            return visited[current] # 목표에 도착했다면 거리를 출력

        # 현재 위치에서 갈 수 있는 위치 계산
        next_position = [current-1, current+1, current*2]

        for position in next_position:
            # 위치가 유효한 범위 내에 있어야하고 방문 하지 않았어야 함
            if 0<= position <= 100000 and position not in visited:
                visited[position] = visited[current]+1
                queue.append(position)
    return -1

print(bfs(n,k))