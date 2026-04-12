import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # target = m
trees = list(map(int, input().split())) # 나무는 정렬할 필요 없음.
max_height = 0

left = 1
right = max(trees) # 나무를 하나도 가져가지 못하는 경우까지

while left <= right:
    mid = (left + right) // 2
    sum = 0

    for tree in trees:
        if tree > mid:
            sum += (tree - mid)

    if sum >= m: # 나무를 더 많이 잘랐을 경우
        # print(f"현재 절단기의 높이: {mid}, 현재 나무의 합: {sum}")
        max_height = mid
        left = mid + 1
    else:
        right = mid - 1

print(max_height)