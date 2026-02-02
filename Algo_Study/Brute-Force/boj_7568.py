import sys
input = sys.stdin.readline

n = int(input())
candidates = []

for _ in range(n):
    a, b = map(int, input().split())
    candidates.append([a, b, 0])

# print("후보: ", candidates)

for i in range(n):
    for j in range(n):
        if candidates[i][0] < candidates[j][0] and candidates[i][1] < candidates[j][1]:
            candidates[i][2] += 1

# print("등수 추가된 후보: ", candidates)

for i in range(n):
    print(candidates[i][2] + 1, end=" ")