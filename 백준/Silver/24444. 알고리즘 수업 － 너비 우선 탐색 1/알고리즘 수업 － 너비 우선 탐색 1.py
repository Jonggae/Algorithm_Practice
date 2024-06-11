import sys

from collections import deque

input = sys.stdin.read
data = input().split()
index = 0

vertex, edge, start = int(data[index]), int(data[index+1]), int(data[index+2])
index += 3

graph = {i: [] for i in range(1, vertex + 1)}
for _ in range(edge):
    u, v = int(data[index]), int(data[index+1])
    graph[u].append(v)
    graph[v].append(u)
    index += 2

for adj in graph.values():
    adj.sort()


# 인접 그래프 생성


# 일반적인 bfs방법 - 문제의 해결을 위해서는 좀 수정해야함

# 각 노드의 방문 순서를 저장함
order = [0] * (vertex + 1)


def bfs(graph, start):
    visited = [False] * (vertex + 1)
    order = [0] * (vertex + 1)
    queue = deque([start])
    visited[start] = True
    order[start] = 1
    order_count = 2

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                order[neighbor] = order_count
                order_count += 1
                queue.append(neighbor)

    return order


order = bfs(graph, start)
for i in range(1, vertex + 1):
    print(order[i])