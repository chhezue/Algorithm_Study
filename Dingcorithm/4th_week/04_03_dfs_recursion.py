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
visited = []

# 1. 시작 노드인 1부터 탐색
# 2. 현재 방문한 노드를 visited 배열에 추가
# 3. 현재 방문한 노드와 인접한 노드 중, 방문하지 않은 노드를 방문
def dfs_recursion(adjacent_graph, cur_node, visited_array):
    visited_array.append(cur_node) # 현재 노드 visited에 추가
    adjacent_nodes = adjacent_graph[cur_node] # [2, 5, 9]

    print("cur_node:", cur_node, "adjacent_nodes:", adjacent_nodes)

    for node in adjacent_nodes:
        if node not in visited_array: # 인접 노드가 방문 리스트에 없다면 (아직 방문하지 않았다면)
            dfs_recursion(adjacent_graph, node, visited_array) # 시작 노드를 인접 노드로 해서 재귀 함수 호출

dfs_recursion(graph, 1, visited)  # 1이 시작 노드
print(visited)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!