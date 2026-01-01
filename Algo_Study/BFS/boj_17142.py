import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def solution(grid, n, m):
    result = float('inf')
    sleep = []
    safe_count = 0

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                safe_count += 1
            if grid[i][j] == 2: # 비활성 바이러스 목록 저장
                sleep.append((i, j))
    
    # 엣지 케이스: 0이 하나도 없는 경우
    if safe_count == 0:
        return 0

    # 비활성 바이러스 목록 중 m개의 활성 바이러스를 뽑는 조합 반복
    for virus in combinations(sleep, m):
        new_grid = [row[:] for row in grid] # 격자 복사
        for r, c in virus: # 활성 바이러스는 -2
            new_grid[r][c] = -2

        second = bfs(new_grid, safe_count)
        if second == -1:
            pass
        else:
            result = min(result, second)

    if result == float('inf'):
        return -1
    else:
        return result

# 바이러스 BFS
def bfs(grid, safe_count):
    # 활성 바이러스 모두 찾아 큐에 넣기
    queue = deque()
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == -2:
                queue.append((i, j, 0))

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while queue:
        r, c, s = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # 비활성 바이러스거나, 그냥 공간이라면 바이러스를 퍼뜨린다.
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                if grid[nr][nc] == 0:
                    grid[nr][nc] = -2
                    safe_count -= 1
                    if safe_count == 0:
                        return s + 1
                    queue.append((nr, nc, s + 1))
                elif grid[nr][nc] == 2:
                    grid[nr][nc] = -2
                    queue.append((nr, nc, s + 1))

    return -1

n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))
print(solution(grid, n, m))