from collections import deque

# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}

def bfs_queue(adj_graph, start_node):
    queue = deque([start_node]) # 1. 시작 노드를 큐에 넣는다.
    visited = []

    while queue:
        # 2. 현재 큐의 노드를 빼서 visited에 추가
        cur_node = queue.popleft()
        visited.append(cur_node)

        # 3. 현재 노드의 인접 노드 중, 방문하지 않은 노드들을 큐에 추가
        adjacent_nodes = adj_graph[cur_node]
        for node in adjacent_nodes:
            if node not in visited:
                queue.append(node)

    return visited

print(bfs_queue(graph, 1))  # 1이 시작 노드
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!