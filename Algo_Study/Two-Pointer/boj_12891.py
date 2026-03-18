import sys
def input(): return sys.stdin.readline().rstrip()

s, p = map(int, input().split())
str = input()
arr = list(map(int, input().split()))
count_arr = [0] * 4
count = 0

# 초기 윈도우의 문자열 count 저장 (0~p)
for i in range(p):
    if str[i] == 'A':
        count_arr[0] += 1
    elif str[i] == 'C':
        count_arr[1] += 1
    elif str[i] == 'G':
        count_arr[2] += 1
    elif str[i] == 'T':
        count_arr[3] += 1

if count_arr[0] >= arr[0] and count_arr[1] >= arr[1] and count_arr[2] >= arr[2] and count_arr[3] >= arr[3]:
    count += 1

# 구간 합이므로 슬라이딩 윈도우 이용
for i in range(p, s):
    # 왼쪽 문자 제거
    if str[i - p] == 'A':
        count_arr[0] -= 1
    elif str[i - p] == 'C':
        count_arr[1] -= 1
    elif str[i - p] == 'G':
        count_arr[2] -= 1
    elif str[i - p] == 'T':
        count_arr[3] -= 1

    # 오른쪽 문자 추가
    if str[i] == 'A':
        count_arr[0] += 1
    elif str[i] == 'C':
        count_arr[1] += 1
    elif str[i] == 'G':
        count_arr[2] += 1
    elif str[i] == 'T':
        count_arr[3] += 1

    if count_arr[0] >= arr[0] and count_arr[1] >= arr[1] and count_arr[2] >= arr[2] and count_arr[3] >= arr[3]:
        count += 1

print(count)