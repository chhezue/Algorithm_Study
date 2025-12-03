def solution(nums, n, m):
    if n == 1:
        if nums[0] == m:
            return 1
        return 0

    result = 0

    for i in range(n):
        prefix_sum = 0
        for j in range(i, n):
            prefix_sum += nums[j]
            if prefix_sum == m:
                result += 1
                break

    return result

n, m = map(int, input().split())
nums = list(map(int, input().split()))
print(solution(nums, n, m))