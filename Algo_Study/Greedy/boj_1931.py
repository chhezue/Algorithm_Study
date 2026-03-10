import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    start, end = map(int, input().split())
    arr.append((start, end))

sorted_arr = sorted(arr, key=lambda x: (x[1], x[0]))
result = [sorted_arr[0]]
# print(f"정렬된 arr: {sorted_arr}")

for i in range(1, len(sorted_arr)):
    if sorted_arr[i][0] >= result[-1][1]:
        result.append(sorted_arr[i])
        # print(result)

print(len(result))