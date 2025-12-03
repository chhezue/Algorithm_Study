from collections import deque
from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = {} # 무방향 그래프
        for i in range(len(rooms)):
            graph[i] = rooms[i]

        # 방문하지 않은 방의 번호가 있으면 False
        result = self.bfs(graph, 0)
        for i in range(len(rooms)):
            if i not in result:
                return False
        return True

    def bfs(self, graph, start):
        queue = deque([start]) # 1. 시작 노드(rooms[0])을 큐에 넣는다.
        visited = []

        while queue:
            # 2. 현재 큐의 노드를 빼서 visited에 추가
            current = queue.popleft()
            visited.append(current)

            # 3. 현재 노드의 인접 노드 중, 방문하지 않은 노드들을 큐에 추가
            adj_rooms = graph[current]
            for r in adj_rooms:
                if r not in visited:
                    queue.append(r)

        return visited

s = Solution()
print(s.canVisitAllRooms([[1],[2],[3],[]]))
print(s.canVisitAllRooms([[1, 3],[3, 0, 1],[2],[0]]))