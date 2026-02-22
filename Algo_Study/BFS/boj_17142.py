import sys
from collections import deque
from itertools import combinations
from typing import List
from copy import deepcopy
input = sys.stdin.readline

class Solution:
    def bfs(self, grid, v, visited):
        queue = deque(v) # 큐에 시작점을 넣음.
        last = 0 # 마지막 0이 감염된 시간
        # print("초기 큐:", queue)

        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        while queue:
            r, c, l = queue.popleft()

            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]

                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and visited[nr][nc] == False and grid[nr][nc] != 1:
                    # 좌표가 0인 경우, 마지막 감염 좌표일 수 있으므로 second를 갱신한다.
                    if grid[nr][nc] == 0:
                        last = max(last, l + 1)
                        grid[nr][nc] = 2
                    visited[nr][nc] = True
                    queue.append((nr, nc, l + 1))

        # BFS 끝났는데도 0이 남아 있으면 실패
        for row in grid:
            if 0 in row:
                return -1

        return last

    def findSafetyFromVirus(self, grid: List[List[str]], m: int) -> int:
        candidates = []
        min_second = float('inf')

        # 초기에 활성화할 바이러스 후보 좌표 넣기
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 2:
                    candidates.append((i, j, 0))

        for v in combinations(candidates, m):
            new_grid = deepcopy(grid)
            visited = [[False] * len(grid[0]) for _ in range(len(grid))]

            # 시작 바이러스 좌표 방문 처리
            for r, c, l in v:
                visited[r][c] = True

            # print("뽑힌 조합:", v)
            # 뽑힌 바이러스를 전부 큐에 넣어서 bfs 시작
            second = self.bfs(new_grid, v, visited)

            if second == -1:
                continue
            else:
                min_second = min(second, min_second)

        if min_second == float('inf'):
            return -1
        else:
            return min_second

n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

print(Solution().findSafetyFromVirus(grid, m))