input = 20

# 방법 1
# def find_prime_list_under_number(number):
#     # 2~20의 수 중 소수라면 prime_list 배열에 넣기
#     prime_list = []
#
#     for n in range(2, number + 1):
#         for i in range(2, n):
#             if n % i == 0:
#                 break
#         else:
#             prime_list.append(n)
#
#     return prime_list

# 방법 2
def find_prime_list_under_number(number):
    # 2~20의 수 중 소수라면 prime_list 배열에 넣기
    prime_list = []

    for n in range(2, number + 1):
        # n보다 작은 모든 소수들에 대해서만 나눠서 검증하면 됨.
        for i in prime_list:
            if n % i == 0:
                break
        else:
            prime_list.append(n)

    return prime_list

result = find_prime_list_under_number(input)
print(result)