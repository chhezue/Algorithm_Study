import sys
input = sys.stdin.readline

k, n = map(int, input().split()) # n개가 필요하다.
lines = [] # 가지고 있는 랜선의 길이
for _ in range(k):
    lines.append(int(input()))
max_len = 0

left = 1
right = max(lines) # 랜선 중 최대 길이를 right로 설정

while left <= right:
    mid = (left + right) // 2
    sum = 0

    for line in lines:
        sum += line // mid

    if sum >= n: # 나무를 더 많이 잘랐을 경우
        max_len = mid
        left = mid + 1
    else:
        right = mid - 1

print(max_len)