from collections import deque
from typing import List

# color = visited 배열처럼 동작
class Solution:
    def bfs(self, graph, color, start):
        # 탐색하고자 하는 그래프의 시작점의 color가 0일 경우, 즉 방문하지 않은 경우에는 아무 색으로나 칠해 줘야 한다.
        # 그래야 아래 while 문에서 반대 색으로 바꿔 가며 탐색할 수 있다.
        if color[start] == 0:
            color[start] = 1

        queue = deque([start]) # 큐에 시작점을 넣음.

        # 정점들을 -1, 1 두 색으로 칠하면서 BFS로 퍼뜨리기
        while queue:
            cur = queue.popleft()

            for item in graph[cur]:
                # 인접 노드 중 색이 칠해지지 않은 경우, cur의 색과 반대로 칠한다.
                if color[item] == 0:
                    color[item] = color[cur] * -1
                    queue.append(item)
                elif color[item] == color[cur]:
                    return False

        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0] * len(graph)

        for i in range(len(graph)):
            if color[i] == 0: # 아직 색칠되지 않았다면 bfs 실행
                result = self.bfs(graph, color, i)
                if result == False:
                    return False

        return True

s = Solution()
print(s.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))
print(s.isBipartite([[1,3],[0,2],[1,3],[0,2]]))