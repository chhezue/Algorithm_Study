import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def solution(grid, c, r):
    result = 0
    empties = []

    # 1. 빈칸 목록 저장
    for i in range(c):
        for j in range(r):
            if grid[i][j] == 0:
                empties.append((i, j))

    # 2. 빈칸 목록 중 3개 뽑는 조합 반복
    for walls in combinations(empties, 3):
        new_grid = [row[:] for row in grid] # 격자 복사
        for r, c in walls: # 벽 세우기
            new_grid[r][c] = 1

        count = bfs(new_grid) # 바이러스 BFS + 안전 영역(0) 개수 세기
        result = max(result, count) # 최댓값 갱신

    return result

# 바이러스 BFS
def bfs(grid):
    # 바이러스 모두 찾아 큐에 넣기
    queue = deque()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                queue.append((i, j))

    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    count = 0

    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                # 바이러스 퍼뜨리기
                if grid[nr][nc] == 0:
                    grid[nr][nc] = 2
                    queue.append((nr, nc))

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                count += 1

    return count

c, r = map(int, input().split())
grid = []
for _ in range(c):
    grid.append(list(map(int, input().split())))
print(solution(grid, c, r))