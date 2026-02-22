import sys
from collections import deque
from itertools import combinations
from typing import List
from copy import deepcopy
input = sys.stdin.readline

class Solution:
    def bfs(self, grid, i, j):
        queue = deque([(i, j)]) # 큐에 시작점을 넣음.

        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        while queue:
            r, c = queue.popleft()

            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]

                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 0:
                    grid[nr][nc] = 2
                    queue.append((nr, nc))

    def findSafetyFromVirus(self, grid: List[List[str]]) -> int:
        max_safety = 0 # 안전 구역 개수
        empty = []

        # 0인 좌표를 empty 배열에 넣기
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    empty.append((i, j))

        # 1. 벽을 세울 3개 조합을 뽑는다.
        for walls in combinations(empty, 3):
            new_grid = deepcopy(grid)
            safety = 0

            # print("뽑힌 조합:", walls)
            for r, c in walls:
                new_grid[r][c] = 1

            # 전체 격자를 (0, 0) 부터 끝까지 스캔
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if new_grid[i][j] == 2: # 바이러스를 만나면 bfs 시작
                        self.bfs(new_grid, i, j)

            # 남은 안전 구역의 개수 세기
            for i in range(len(new_grid)):
                for j in range(len(new_grid[0])):
                    if new_grid[i][j] == 0:
                        safety += 1

            max_safety = max(max_safety, safety)

        return max_safety

n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

print(Solution().findSafetyFromVirus(grid))