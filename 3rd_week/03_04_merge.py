array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]

def merge(array1, array2):
    result = []
    a_idx = 0
    b_idx = 0

    while a_idx < len(array1) and b_idx < len(array2):
        if array1[a_idx] < array2[b_idx]:
            result.append(array1[a_idx])
            a_idx += 1
        else:
            result.append(array2[b_idx])
            b_idx += 1

    if a_idx < len(array1):
        result += array1[a_idx:]
    if b_idx < len(array2):
        result += array2[b_idx:]

    return result

print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1, 2, 3, 5, 40], [10, 78, 100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1, -1, 0], [1, 6, 9, 10]))