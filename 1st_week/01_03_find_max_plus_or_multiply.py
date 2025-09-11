# def find_max_plus_or_multiply(array):
#     result = 0
#
#     for i in range(len(array)):
#         plus = result + array[i]
#         multiply = result * array[i]
#
#         if plus > multiply:
#             result = plus
#         else:
#             result = multiply
#
#     return result

def find_max_plus_or_multiply(array):
    result = 0
    for number in array:
        # 현재 숫자가 <= 1 이라면, 현재까지의 결과가 <= 1 이라면 무조건 더하는 것이 낫다.
        if number <= 1 or result <= 1:
            result += number
        else:
            result *= number

    return result

result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))