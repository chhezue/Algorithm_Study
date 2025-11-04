input = [4, 6, 2, 9, 1]

# 시간복잡도: O(N^2)
def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i): # 0 ~ i-1 까지의 범위에서 모든 원소와 비교
            if array[i - j] < array[i - j - 1]: # 거꾸로 비교
                array[i - j], array[i - j - 1] = array[i - j - 1], array[i - j]
            else:
                # 거꾸로 비교하는 도중, 현재 삽입하려는 원소가 더 크다면 앞의 원소를 비교할 필요가 없다.
                # 앞의 배열은 이미 다 정렬되어 있다고 가정하기 때문
                break

    return array

insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 =", insertion_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 =", insertion_sort([3, -1, 17, 9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 =", insertion_sort([100, 56, -3, 32, 44]))