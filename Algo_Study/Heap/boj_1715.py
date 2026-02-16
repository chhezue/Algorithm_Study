import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
result = 0

# 최소 힙으로 정렬
for _ in range(n):
    x = int(input())
    heapq.heappush(heap, x)
# print("초기 힙:", heap)

while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    # print("카드 최소 비교 횟수:", a + b)
    result += a + b
    heapq.heappush(heap, a + b)
    # print("변경된 힙:", heap)

print(result)