import sys
def input(): return sys.stdin.readline().rstrip()

# 1. 누적합 이용한 풀이
# n, k = map(int, input().split())
# arr = list(map(int, input().split()))
# prefix_sum = [0] * (n + 1)
# max_temper = float('-inf')
#
# for i in range(1, n + 1):
#     prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
#
# for i in range(k, n + 1):
#     day_temper = prefix_sum[i] - prefix_sum[i - k]
#     max_temper = max(max_temper, day_temper)
#
# print(max_temper)

# 2. 슬라이딩 윈도우 이용한 풀이
n, k = map(int, input().split())
arr = list(map(int, input().split()))

left = 0 # left는 0번째 인덱스부터 시작
right = k - 1 # right는 (left + k - 1) 인덱스부터 시작

temper_sum = sum(arr[left:right + 1]) # left~right 초기 합 구함.
temper_max = sum(arr[left:right + 1])

# 구간 합이므로 슬라이딩 윈도우 이용
while True:
    temper_max = max(temper_max, temper_sum)
    if right + 1 == n:
        break
    temper_sum -= arr[left]
    temper_sum += arr[right + 1]
    left += 1
    right += 1

print(temper_max)