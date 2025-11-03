numbers = [1, 1, 1, 1, 1]
target_number = 3

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    result = []
    count = 0
    get_all_ways_by_recursive(array, 0, 0, result)

    for item in result:
        if item == target:
            count += 1

    return count

def get_all_ways_by_recursive(array, current_index, current_sum, result):
    if current_index == len(array):
        result.append(current_sum)
        return

    get_all_ways_by_recursive(array, current_index + 1, current_sum + array[current_index], result)
    get_all_ways_by_recursive(array, current_index + 1, current_sum - array[current_index], result)

print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!