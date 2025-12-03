import sys
input = sys.stdin.readline

# 5 1 3 5 10 7 4 9 2 8 -> 2
# 1 2 3 4 5 6 7 8 9 10 -> 1
def solution(nums, n, m):
    left = 0
    right = 0
    min_len = len(nums) # 10
    cur_sum = 0

    while True: # 조건 제약: 수를 하나만 골라도 됨.
        cur_sum_len = right - left # 현재 누적합의 길이
        # print("현재 left:", left, "right:", right, "cur_sum:", cur_sum, "cur_sum_len:", cur_sum_len)

        if cur_sum >= m: # 누적합이 m보다 큼: 합 작게 변경
            min_len = min(min_len, cur_sum_len)
            cur_sum -= nums[left]
            left += 1
            # print("[left 늘림] min_len:", min_len, "cur_sum:", cur_sum)
        # left, right 인덱스는 n - 1 인덱스까지 갈 수 있다.
        # right 인덱스가 n이 되면 모든 경우의 수를 검사한 것이니 종료.
        # left는 증가만 하므로 right의 경우만 고려하면 됨.
        elif right == n:
            break
        else:
            cur_sum += nums[right]
            right += 1
            # print("[right 늘림] min_len:", min_len, "cur_sum:", cur_sum)

    if min_len != len(nums):
        return min_len
    else:
        return 0

n, m = map(int, input().split())
nums = list(map(int, input().split()))
print(solution(nums, n, m))