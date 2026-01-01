def solution(places):
    result = []

    for i in range(len(places)):
        # 2차원 배열의 하나의 행을 다시 격자 형태로 만듦.
        grid = [list(row) for row in places[i]]
        result.append(validate(grid))

    return result

def validate(grid):
    # 사람을 모아서 전부 큐에 넣기
    p_list = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 'P':
                p_list.append((i, j))

    # 엣지 케이스: 사람이 아무도 없는 경우
    if not p_list:
        return 1 # 모두가 거리두기를 지키고 있다고 판단

    one_distance = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 맨해튼 거리 1
    two_distance_row = [(2, 0), (-2, 0)] # 맨해튼 거리 2
    two_distance_col = [(0, 2), (0, -2)] # 맨해튼 거리 2
    diagonal = [(1, 1), (-1, -1), (1, -1), (-1, 1)] # 대각선

    for i in range(len(p_list)):
        r, c = p_list[i]

        # 맨해튼 거리가 1인 경우, 무조건 0 return
        for dr, dc in one_distance:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                if grid[nr][nc] == 'P':
                    return 0

        for dr, dc in two_distance_row:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                if grid[nr][nc] == 'P':
                    # 두 좌표 사이에 파티션이 있는지 검사
                    if grid[(r + nr) // 2][nc] != 'X':
                        return 0

        for dr, dc in two_distance_col:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                if grid[nr][nc] == 'P':
                    # 두 좌표 사이에 파티션이 있는지 검사
                    if grid[nr][(c + nc) // 2] != 'X':
                        return 0

        for dr, dc in diagonal:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                # 대각선에 사람이 있는 경우, 두 칸에 모두 파티션이 있어야 한다.
                if grid[nr][nc] == 'P':
                    if grid[nr][c] != 'X' or grid[r][nc] != 'X':
                        return 0

    return 1

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))