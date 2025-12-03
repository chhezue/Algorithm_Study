seat_count = 9 # 극장 자리의 개수
vip_seat_array = [4, 7] # vip 고정석
memo = {
    1: 1,
    2: 2,
}

# [1, 2, 3, 4, 5, 6, 7, 8, 9]
def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    result = 0

    if total_count in memo:
        return memo[total_count]

    # 1. 1~3번끼리 바꾸는 경우
    # result += 4 - 1
    first_count = get_all_ways_of_theater_seat(fixed_seat_array[0] - 1, fixed_seat_array)
    memo[fixed_seat_array[0] - 1] = first_count
    # 2. 5~6번끼리 바꾸는 경우
    # result += 6 - 5 + 1
    second_count = get_all_ways_of_theater_seat(fixed_seat_array[1] - fixed_seat_array[0] + 1, fixed_seat_array)
    memo[fixed_seat_array[1] - fixed_seat_array[0] + 1] = second_count
    # 3. 8~9번끼리 바꾸는 경우
    # result += 9 - 8 + 1
    third_count = get_all_ways_of_theater_seat(seat_count - fixed_seat_array[1] + 1, fixed_seat_array)
    memo[seat_count - fixed_seat_array[1] + 1] = third_count

    return result


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))

print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9,[2,4,7]))
print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11,[2,5]))
print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10,[2,6,9]))