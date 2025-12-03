import sys
input = sys.stdin.readline

def solution(nums, n, m):
    nums.sort()
    left = 0
    right = 0
    min_diff = float('inf')

    while left < n and right < n: # 조건 제약: 무조건 두 수를 골라야 함.
        diff = nums[right] - nums[left]

        if diff >= m:
            min_diff = min(min_diff, diff)
            left += 1
        else:
            right += 1

    return min_diff

n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]
print(solution(nums, n, m))