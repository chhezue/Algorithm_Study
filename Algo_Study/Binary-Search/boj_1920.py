import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
wanted = list(map(int, input().split())) # 찾고자 하는 수
arr.sort()

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return 1 # 찾은 경우
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return 0  # 못 찾은 경우

for i in wanted:
    print(binary_search(arr, i))

# n = int(input())
# arr = set(map(int, input().split()))
# m = int(input())
# wanted = list(map(int, input().split())) # 찾고자 하는 수
#
# def find_number(arr, target):
#     if target in arr:
#         return 1
#     else:
#         return 0
#
# for i in wanted:
#     print(find_number(arr, i))