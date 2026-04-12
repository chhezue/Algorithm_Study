# stones = 디딤돌에 적힌 숫자가 순서대로 담긴 배열 (디딤돌을 밟을 때마다 숫자 -1)
# k = 한 번에 건너뛸 수 있는 디딤돌의 최대 개수
def solution(stones, k):
    answer = 0
    left = 1
    right = max(stones) # stones의 최대 길이 = 건너갈 수 있는 사람의 최대 명수

    while left <= right:
        mid = (left + right) // 2
        can_cross = True
        zero_count = 0

        for stone in stones:
            if stone - mid < 0:
                zero_count += 1
            else:
                zero_count = 0

            # 돌이 연속 k개 이상 < 0 일 경우
            if zero_count >= k:
                can_cross = False
                break

        if can_cross == True:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)) # 3