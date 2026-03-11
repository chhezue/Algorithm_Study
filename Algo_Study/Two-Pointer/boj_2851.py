import sys
def input(): return sys.stdin.readline().rstrip()

prefix_sum = []
prefix = 0
a, b = 0, 0

for _ in range(10):
    prefix += int(input())
    prefix_sum.append(prefix)

# print(prefix_sum)

if prefix_sum[-1] < 100:
    print(prefix_sum[-1])
else:
    for i in range(10):
        if prefix_sum[i] > 100:
            a = prefix_sum[i]
            b = prefix_sum[i - 1]
            break

    # 차이가 더 작은 것이 100에 더 가까운 값
    if a - 100 > 100 - b:
        print(b)
    elif a - 100 < 100 - b:
        print(a)
    else: # 차이가 같은 경우, 더 큰 값 출력
        print(a)
