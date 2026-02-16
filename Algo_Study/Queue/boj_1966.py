import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

count = int(input())

for _ in range(count):
    n, m = map(int, input().split())
    importance = list(map(int, input().split()))
    queue = deque()

    for idx, i in enumerate(importance):
        queue.append((i, idx))  # 중요도, 원래 위치

    wanted = queue[m]  # (2, 3)
    result = 0

    while True:
        max_importance = max(queue, key=lambda x: x[0])
        item = queue.popleft()

        if item == max_importance:
            if item == wanted:
                result += 1
                break
            result += 1
        else:
            queue.append(item)

    print(result)