finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2  # 중간값

    while current_min <= current_max:
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:  # up인 경우
            current_min = current_guess + 1
        else:  # down인 경우
            current_max = current_guess - 1
        current_guess = (current_min + current_max) // 2  # 중간값 다시 계산

    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)