import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

result = 0
idx = len(arr) - 1

while k != 0:
    if arr[idx] > k:
        idx -= 1
    else:
        count = k // arr[idx]
        result += count
        k -= (arr[idx] * count)

print(result)