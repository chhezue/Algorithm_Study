finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# 배열을 이진 탐색하며 찾기: 시간복잡도 O(long(N))
def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2 # 반으로 잘라서 내가 부른 숫자

    while current_min <= current_max:
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target: # up인 경우 (8 < 14)
            current_min = current_guess + 1 # 최솟값은 9가 됨.
        else: # down인 경우
            current_max = current_guess - 1
        current_guess = (current_min + current_max) // 2 # 내가 부를 숫자 다시 계산 (반으로 쪼갬)

    return False

result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)  # True