from collections import deque
from typing import List

class Solution:
    def bfs(self, grid, i, j, v):
        queue = deque([(i, j)]) # 큐에 시작점을 넣음.
        v[i][j] = True

        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        while queue:
            r, c = queue.popleft()

            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]

                if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])
                        and grid[nr][nc] == "1" and not v[nr][nc]):
                        queue.append((nr, nc))
                        v[nr][nc] = True

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        # 1. 전체 격자를 (0,0) 부터 끝까지 스캔
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 2. 아직 방문하지 않은 1을 만나면 BFS 시작, count += 1
                if grid[i][j] == "1" and not visited[i][j]:
                    self.bfs(grid, i, j, visited)
                    count += 1

        return count

s = Solution()
print(s.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
print(s.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))