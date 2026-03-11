# 양쪽에서 좁혀오는 투 포인터
import sys
def input(): return sys.stdin.readline().rstrip()

n = int(input()) # 재료의 개수
m = int(input()) # target number
arr = list(map(int, input().split())) # 재료 목록
arr.sort()

count = 0
left = 0
right = n - 1
sum = arr[left] + arr[right] # arr[0] + arr[5]에서 시작

while left < right:
    sum = arr[left] + arr[right]
    if sum == m:
        count += 1
        left += 1
        right -= 1
    elif sum > m:
        right -= 1
    else:
        left += 1

print(count)