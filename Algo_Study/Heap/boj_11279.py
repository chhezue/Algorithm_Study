import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())

    if x > 0:
        heapq.heappush(heap, x * -1)
    else:
        if len(heap) == 0:
            print(0)
            continue
        item = heapq.heappop(heap)
        print(item * -1)