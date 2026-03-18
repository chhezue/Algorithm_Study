import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 0
min_len = float('inf')
sum = 0

# while right < n:
#     if sum >= s:
#         min_len = min(min_len, right - left)
#         sum -= arr[left]
#         left += 1
#     else:
#         sum += arr[right]
#         right += 1

while True:
    if sum >= s:
        min_len = min(min_len, right - left)
        sum -= arr[left]
        left += 1
    else:
        if right == n:
            break
        sum += arr[right]
        right += 1

if min_len == float('inf'):
    print(0)
else:
    print(min_len)