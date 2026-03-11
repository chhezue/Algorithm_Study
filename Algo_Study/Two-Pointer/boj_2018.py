import sys
def input(): return sys.stdin.readline().rstrip()

n = int(input())
count = 1
left = 1
right = 1
sum = 1

while right < n:
    if sum == n:
        count += 1
        right += 1
        sum += right
    elif sum > n: # 합계가 n보다 큰 경우
        sum -= left # 이전의 left를 제외
        left += 1 # 현재 left를 구간의 시작점으로 변경
    else: # 합계가 n보다 작은 경우
        right += 1  # 현재 right를 구간의 끝점으로 변경
        sum += right # sum에 새로운 right 더함.

print(count)