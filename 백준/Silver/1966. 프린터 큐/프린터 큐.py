from collections import deque
n = int(input().strip())
docs = []
priority = []
for _ in range(n):
    docs.append(list(map(int, (input().split()))))
    priority.append(list(map(int, (input().split()))))
    
def solution(target,m, p):
    queue = deque(p)  # 중요도 리스트를 큐로 만듬 [1,1,9,1,1,1]
      # 인쇄 기준이 될 최대 중요도 선정
    idx = deque(range(target)) # 각 문서의 인덱스

    # queue의 값을 순회하면서 가장 중요도가 높은 것부터 인쇄함. 만약 낮다면 맨 뒤로 보냄
    # 같은 중요도일때는 어떻게 해야할까?
    # 같은 중요도를 체크하기 위해 idx를 이용해야 한다.  -> 이해가 잘 안됨..
    count = 0
    while queue:
        if queue[0] == max(queue):
            count += 1
            queue.popleft()
            if idx.popleft() == m:
                return count
        else:
            queue.append(queue.popleft())
            idx.append(idx.popleft())

for i in range(n):
    print(solution(docs[i][0], docs[i][1], priority[i]))