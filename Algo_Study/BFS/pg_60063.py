from collections import deque

def solution(board):
    n = len(board)

    start = ((0, 0), (0, 1)) # 두 좌표의 튜플 덩어리
    queue = deque([(start, 0)])  # (위치, 시간)
    visited = set([start])

    # 좌, 우, 상, 하
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]

    while queue:
        pos, second = queue.popleft()
        r1, c1 = pos[0]
        r2, c2 = pos[1]

        # 두 좌표 중 하나라도 마지막 좌표에 도달한 경우
        if (r1 == n - 1 and c1 == n - 1) or (r2 == n - 1 and c2 == n - 1):
            return second

        # 1. 상하좌우로 이동할 수 있는 경우 검사
        for k in range(4):
            nr1 = r1 + dr[k]
            nc1 = c1 + dc[k]
            nr2 = r2 + dr[k]
            nc2 = c2 + dc[k]

            if (0 <= nr1 < n and 0 <= nc1 < n and 0 <= nr2 < n and 0 <= nc2 < n
                    and board[nr1][nc1] == 0 and board[nr2][nc2] == 0):
                next = (nr1, nc1), (nr2, nc2)  # 리스트로 변환 후 정렬, 다시 튜플로 변환
                if not next in visited:
                    queue.append((next, second + 1))
                    visited.add(next)

        # 2. 가로로 놓인 경우 회전
        if r1 == r2:
            for d in [-1, 1]:  # 위(-1), 아래(1)
                if 0 <= r1 + d < n:
                    # 위쪽 두 칸 혹은 아래쪽 두 칸이 모두 비어 있다면, 4개의 경로(좌하단, 우하단, 좌상단, 우상단) 모두 회전 가능
                    if board[r1 + d][c1] == 0 and board[r2 + d][c2] == 0:
                        for r, c in [(r1, c1), (r2, c2)]:
                            next = (r, c), (r + d, c)
                            if next not in visited:
                                queue.append((next, second + 1))
                                visited.add(next)

        # 3. 세로로 놓인 경우 회전
        if c1 == c2:
            for d in [-1, 1]:  # 가로(-1), 세로(1)
                if 0 <= c1 + d < n:
                    if board[r1][c1 + d] == 0 and board[r2][c2 + d] == 0:
                        for r, c in [(r1, c1), (r2, c2)]:
                            next = (r, c), (r, c + d)
                            if next not in visited:
                                queue.append((next, second + 1))
                                visited.add(next)

    return -1

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])) # 7