import sys
input = sys.stdin.readline

candidates = []
n = int(input())
start = max(0, n - 63)

for i in range(start, n):
    # print("시작: i = ", i)
    current = 0
    current += i

    nums = list(map(int, str(i)))
    current += sum(nums)

    if current == n:
        # print("조건을 만족하는 i = ", i)
        candidates.append(i)

if len(candidates) == 0:
    print(0)
else:
    print(min(candidates))