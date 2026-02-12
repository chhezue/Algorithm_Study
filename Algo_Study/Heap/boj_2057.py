import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    arr = list(map(int, input().split())) # arr = [12, 7, 9, 15, 5]

    for item in arr:
        if len(heap) == n: # 힙이 꽉 찬 경우
            if item > heap[0]: # 힙의 최솟값보다 현재 item이 크다면
                heapq.heappop(heap)
                heapq.heappush(heap, item)
            else:
                continue
        else: # 힙이 아직 꽉 차지 않은 경우
            heapq.heappush(heap, item)

print(heap[0])