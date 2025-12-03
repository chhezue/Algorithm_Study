def solution(nums):
    stack = []
    result = [-1] * len(nums)

    for i, num in enumerate(nums):
        while stack and stack[-1][1] < num: # 5가 선택되었고 3 < 5
            idx, value = stack.pop() # (0, 3)
            result[idx] = num # result[0] = 5가 되어야 한다.

        stack.append((i, num))

    return result

n = int(input())
nums = list(map(int, input().split()))
print(*solution(nums))
