from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        distance = 1

        visited = [[False] * cols for _ in range(rows)]
        directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]

        # 만약 출발 칸 또는 도착 칸이 1이면 -1 return
        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1

        # [[0]]인 경우
        if rows == 1 and cols == 1 and grid[0][0] == 0:
            return 1

        return self.bfs(grid, visited, directions, 0, 0, distance)

    def bfs(self, grid, visited, directions, r, c, distance):
        queue = deque([(r, c, distance)])
        visited[r][c] = True

        while queue:
            r, c, distance = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    if grid[nr][nc] == 0 and not visited[nr][nc]:
                        if nr == len(grid) - 1 and nc == len(grid[0]) - 1:
                            return distance + 1
                        else:
                            visited[nr][nc] = True
                            queue.append((nr, nc, distance + 1))

        return -1

s = Solution()
print(s.shortestPathBinaryMatrix([[0,1],[1,0]]))
print(s.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))
print(s.shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]))