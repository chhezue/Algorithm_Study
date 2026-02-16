import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split())) # [3, 5, 2, 7]
stack = []
result = [0] * n

# 배열을 역순으로 검사
for i in range(n-1, -1, -1):
    while stack and arr[stack[-1]] < arr[i]:
        result[stack[-1]] = i + 1
        stack.pop()

    stack.append(i)

print(*result)