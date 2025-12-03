def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 연속된 0, 1 덩어리의 개수 구하기
    zero_count = 0
    one_count = 0
    prev = ""

    for i in range(len(string)):
        if string[i] == "0":
            if prev != "0":
                zero_count += 1
                prev = string[i]
        else:
            if prev != "1":
                one_count += 1
                prev = string[i]

    return min(zero_count, one_count)

print(find_count_to_turn_out_to_all_zero_or_all_one("0001100")) # 1
print(find_count_to_turn_out_to_all_zero_or_all_one("11111")) # 0
print(find_count_to_turn_out_to_all_zero_or_all_one("00000001")) # 1
print(find_count_to_turn_out_to_all_zero_or_all_one("11001100110011000001")) # 4
print(find_count_to_turn_out_to_all_zero_or_all_one("11101101")) # 2
