from collections import deque
from typing import List

# 1. BFS는 "하나의 시작점에서 연결된 덩어리"만 탐색한다.
# 2. 다른 섬을 탐색하고 싶다면 BFS를 새로 호출해야 한다.
# 3. BFS를 반복적으로 호출하는 흐름은 바깥 루프에서 한다.
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        result = 0

        visited = [[False] * cols for _ in range(rows)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # 전체 grid 순회
        for r in range(rows):
            for c in range(cols):
                # 방문하지 않았고 1이라면 -> 새로운 섬 발견
                # bfs를 호출해서 그 섬 전체를 visited = True로 만들어야 한다.
                if not visited[r][c] and grid[r][c] == '1':
                    self.bfs(grid, visited, directions, r, c)
                    result += 1

        return result

    # 같은 섬의 땅을 모두 visited = True로 만드는 작업
    def bfs(self, grid, visited, directions, r, c):
        queue = deque([(r, c)])
        visited[r][c] = True

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc # 상하좌우 모두 탐색

                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    if grid[nr][nc] == '1' and not visited[nr][nc]:
                        queue.append((nr, nc))
                        visited[nr][nc] = True

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