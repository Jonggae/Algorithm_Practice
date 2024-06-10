import sys
vertex, edge, start = map(int, input().split())

edges = [list(map(int, sys.stdin.readline().split())) for _ in range(edge)]
vertexes = [0] * vertex


def make_graph(vertex, edges):
    graph = {i: [] for i in range(1, vertex + 1)}

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    return graph


graph = make_graph(vertex, edges)


def dfs(graph, start):

    stack = [start]
    visited_order = 1 # 방문 순서 기록

    while stack:
        vertex = stack.pop()
        if vertexes[vertex - 1] == 0:  # 해당 정점이 방문되지 않았다면
            vertexes[vertex - 1] = visited_order
            visited_order += 1
            # 방문 가능한 정점 중 작은 숫자부터 방문하려면, 오름차순으로 정렬
            stack.extend(sorted(graph[vertex], reverse=True))

dfs(graph, start)  # 1 대신 start 사용

for i in vertexes:
    print(i)