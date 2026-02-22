from collections import deque
from typing import List

class Solution:
    def bfs(self, grid, i, j, v):
        queue = deque([(i, j, 0)]) # 큐에 시작점을 넣음. (거리 레벨 0으로 시작)
        v[i][j] = True

        dr = [-1, 0, 1, 0, 1, 1, -1, -1]
        dc = [0, 1, 0, -1, 1, -1, 1, -1]

        while queue:
            r, c, l = queue.popleft()
            if r == len(grid) - 1 and c == len(grid[0]) - 1: # 마지막 좌표를 찾은 경우
                return l + 1

            # 다음 레벨로 퍼져나가는 과정
            # 꺼낸 노드 (r, c, l)를 기준으로, 인접한 8개의 노드의 거리 레벨은 모두 l + 1
            for k in range(8):
                nr = r + dr[k]
                nc = c + dc[k]

                if (0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 0 and not v[nr][nc]):
                        queue.append((nr, nc, l + 1)) # 다음 레벨 노드를 append
                        v[nr][nc] = True

        return -1

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # 시작점이나 도착점이 1이라면 애초에 -1 return
        if grid[len(grid) - 1][len(grid) - 1] == 1 or grid[0][0] == 1:
            return -1

        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        return self.bfs(grid, 0, 0, visited)

s = Solution()
print(s.shortestPathBinaryMatrix([[0,1],[1,0]]))
print(s.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))
print(s.shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]))