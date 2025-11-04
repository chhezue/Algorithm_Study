input = [4, 6, 2, 9, 1]

# 시간복잡도: O(N^2)
def selection_sort(array):
    n = len(array)
    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j # 최솟값의 위치만 저장 (j 루프가 끝날 때까지 계속 갱신됨)

        array[i], array[min_index] = array[min_index], array[i] # 마지막에 한 번만 교환

    return array

selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 =", selection_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 =", selection_sort([3, -1, 17, 9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 =", selection_sort([100, 56, -3, 32, 44]))