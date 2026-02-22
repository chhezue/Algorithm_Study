import sys
input = sys.stdin.readline

def dfs(graph, start, visited, result):
    result.append(start)

    # start와 연결된 이웃 노드 검사
    for item in sorted(graph[start]): # 방문할 수 있는 정점이 여러 개인 경우, 오름차순 정렬
        # 연결 노드 중 방문하지 않은 노드가 있다면 재귀 호출
        if visited[item] == False:
            visited[item] = True
            dfs(graph, item, visited, result) # 콜 스택에 넣음.

    return result

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)] # graph = [[], [], [], [], [], []]
visited = [False] * (n+1)
visited[v] = True
result = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print("생성된 그래프:", graph)

result = dfs(graph, v, visited, result)
print(*result)
