import sys
def input(): return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
prefix_sum = [0] * (n + 1)

for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

for _ in range(m):
    i, j = map(int, input().split()) # i부터 j까지 합 구하기
    print(prefix_sum[j] - prefix_sum[i - 1])