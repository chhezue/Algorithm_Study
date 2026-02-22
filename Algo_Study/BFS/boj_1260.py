import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, start):
    queue = deque([start]) # 시작 정점 삽입 (start가 정수기 때문에 []로 감싸야 함.)
    visited = [False] * (n+1) # 1~n 인덱스를 사용함.
    visited[start] = True # 시작 정점은 방문 처리
    result = []

    while queue:
        # 큐에서 정점을 뽑고 result 배열에 넣는다. (뽑혔다는 건 방문했다는 의미)
        cur = queue.popleft() # 시작 정점: 1
        result.append(cur)
        print(f"{cur} 방문 완료 -> 현재까지 방문한 노드: {result}")
        print(f"아래에서 {cur}의 연결 노드를 검사한다.")

        # cur의 연결 노드를 모두 검사한다.
        print(f"{cur}의 인접 노드들: {graph[cur]}")
        for item in sorted(graph[cur]): # 방문할 수 있는 정점이 여러 개인 경우, 오름차순 정렬
            # 연결 노드 중 방문하지 않은 노드가 있다면 큐에 append
            if visited[item] == False:
                print(f"{cur}의 인접 노드들 중 {item}을 검사하지 않았으므로 큐에 넣음.")
                queue.append(item)
                visited[item] = True
                print(f"현재 큐: {queue}")

    return result

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)] # graph = [[], [], [], [], [], []]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print("생성된 그래프:", graph)

result = bfs(graph, v)
print(*result)
