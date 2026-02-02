import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
board = []

# 지도 입력
for _ in range(n):
    board.append(list(map(int, input().split())))

command = list(map(int, input().split()))
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]  # [top, bottom, north, south, west, east]

for i in range(k):
    item = command[i] # 4

    # 이동할 위치
    x_pos = x + dx[item]
    y_pos = y + dy[item]

    # 범위가 벗어나지 않는지 검사
    if x_pos < 0 or x_pos >= n or y_pos < 0 or y_pos >= m:
        continue
    else:
        temp = dice[0]
        if item == 1:  # 동쪽으로 굴릴 경우
            dice[0] = dice[4]
            dice[4] = dice[1]
            dice[1] = dice[5]
            dice[5] = temp
        elif item == 2:  # 서쪽으로 굴릴 경우
            dice[0] = dice[5]
            dice[5] = dice[1]
            dice[1] = dice[4]
            dice[4] = temp
        elif item == 3:  # 북쪽으로 굴릴 경우
            dice[0] = dice[3]
            dice[3] = dice[1]
            dice[1] = dice[2]
            dice[2] = temp
        else:  # 남쪽으로 굴릴 경우
            dice[0] = dice[2]
            dice[2] = dice[1]
            dice[1] = dice[3]
            dice[3] = temp

        if board[x_pos][y_pos] == 0: # 이동한 칸에 쓰여 있는 수가 0이면
            board[x_pos][y_pos] = dice[1]  # bottom 값을 board에 복사
        else: # 0이 아닌 경우
            dice[1] = board[x_pos][y_pos]  # board 값을 bottom에 복사
            board[x_pos][y_pos] = 0 # 칸에 쓰여 있는 수는 0이 됨.

        print(dice[0])
        x, y = x_pos, y_pos