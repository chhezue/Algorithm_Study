# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}

# 재귀 함수의 무한 호출 문제 때문에 스택으로 구현하는 것이 낫다.
# dfs: 깊이 끝까지 찾았다가 돌아오는 것
def dfs_stack(adjacent_graph, start_node):
    stack = [start_node] # 1. 시작 노드를 스택에 넣는다.
    visited = []

    while stack:
        # 2. 현재 스택의 노드를 빼서 visited에 추가
        cur_node = stack.pop()
        visited.append(cur_node)

        # 3. 현재 노드의 인접 노드 중, 방문하지 않은 노드들을 스택에 추가
        adjacent_nodes = adjacent_graph[cur_node]
        for node in adjacent_nodes:
            if node not in visited:
                stack.append(node)

    return visited

print(dfs_stack(graph, 1))  # 1이 시작 노드
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!