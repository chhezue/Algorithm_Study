def find_max_num(num_list):
    max = num_list[0]
    for i in range(len(num_list)):
        if max < num_list[i]:
            max = num_list[i]

    return max

print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))
