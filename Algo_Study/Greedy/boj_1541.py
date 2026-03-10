import sys
input = sys.stdin.readline

str = input().rstrip().split('-') # '-'를 기준으로 분리
result = 0
arr = []

for item in str:
    x = sum(map(int, item.split('+')))
    arr.append(x)

result = arr[0]
for i in range(1, len(arr)):
    result -= arr[i]

print(result)