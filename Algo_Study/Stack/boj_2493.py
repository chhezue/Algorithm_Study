def top(nums):
    stack = []
    result = [0] * len(nums)

    for i in range(len(nums) - 1, -1, -1): # 역순으로
        # print("i:", i, "nums[i]:", nums[i])
        while stack and stack[-1][0] < nums[i]:
            value, idx = stack.pop()
            result[idx] = i + 1

        stack.append((nums[i], i))

    return result

n = int(input())
nums = list(map(int, input().split()))
print(*top(nums))

# input: 6 9 5 7 4
# output: 0 0 2 2 4