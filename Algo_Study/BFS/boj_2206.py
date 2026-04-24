import sys
from collections import deque
from typing import List
input = sys.stdin.readline

class Solution:
    def bfs(self, grid, i, j, v):
        # 큐는 (x, y, 거리, 벽을 부쉈는지 여부)로 정의한다.
        queue = deque([(i, j, 0, 0)]) # 큐에 시작점을 넣음. (거리 레벨 0으로 시작)
        v[i][j][0] = True # 시작점 방문 체크 (벽 부수지 않음.)

        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        while queue:
            r, c, l, broken = queue.popleft()
            if r == len(grid) - 1 and c == len(grid[0]) - 1: # 마지막 좌표를 찾은 경우
                return l + 1

            # 다음 레벨로 퍼져나가는 과정
            # 꺼낸 노드 (r, c, l)를 기준으로, 인접한 4개의 노드의 거리 레벨은 모두 l + 1
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]

                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                        # 1. 현재 위치가 벽이고 부서지지 않은 경우
                        if grid[nr][nc] == 1 and broken == 0 and not v[nr][nc][1]:
                            v[nr][nc][1] = True # 벽을 부순다.
                            queue.append((nr, nc, l + 1, 1)) # 다음 레벨 노드를 append
                        # 2. 현재 위치가 벽이고 이미 이전에 벽을 부순 경우
                        elif grid[nr][nc] == 1 and broken == 1 and not v[nr][nc][1]:
                            continue
                        # 3. 현재 위치가 길인 경우
                        elif grid[nr][nc] == 0 and not v[nr][nc][broken]:
                            v[nr][nc][broken] = True
                            queue.append((nr, nc, l + 1, broken)) # 현재 벽 부서진 정보를 그대로 append

        return -1

    def solution(self, grid: List[List[int]]) -> int:
        visited = [[[False]*2 for _ in range(m)] for _ in range(n)] # 3차원 배열
        return self.bfs(grid, 0, 0, visited)

n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().strip())))

print(Solution().solution(grid))