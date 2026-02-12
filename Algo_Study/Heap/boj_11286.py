import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())

    if x == 0:
        if len(heap) == 0:
            print(0)
            continue

        item = heapq.heappop(heap)

        if item[1]: # 양수라면 그대로 출력
            item = item[0]
        else: # 음수라면 음수로 되돌려서 출력
            item = item[0] * -1
        print(item)
    elif x > 0:
        heapq.heappush(heap, (x, True))
    else:
        heapq.heappush(heap, (x * -1, False))