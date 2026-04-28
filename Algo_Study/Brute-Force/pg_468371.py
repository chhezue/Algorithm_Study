import math

def solution(signals):
    n = len(signals)
    cycle_times = [] # 각 신호등의 전체 주기 (green + yellow + red)

    for s in signals:
        cycle_times.append(sum(s))

    lcm = math.lcm(*cycle_times) # while문은 최소공배수까지 진행된다.
    time = 0 # 현재 시간

    while time <= lcm:
        flag = True

        for i in range(n):
            cur_pos = time % cycle_times[i] # i 기준으로 현재 위치 계산
            green = signals[i][0]
            yellow = signals[i][1]

            # 노란불이 켜지는 구간 = 초록불이 끝난 직후부터 빨간불이 시작되기 전까지
            if green <= cur_pos < green + yellow:
                continue
            else:
                flag = False
                break

        # 동시에 n개의 노란불이 모두 켜진 경우
        if flag:
            return time + 1
        else:
            time += 1

    return -1

print(solution([[2, 1, 2], [5, 1, 1]])) # 13
print(solution([[2, 3, 2], [3, 1, 3], [2, 1, 1]])) # 11
print(solution([[3, 3, 3], [5, 4, 2], [2, 1, 2]])) # 193