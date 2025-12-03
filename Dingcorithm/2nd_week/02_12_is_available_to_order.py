shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

def is_available_to_order(menus, orders):
    # 이진 탐색의 전제 조건: 정렬되어 있어야 함.
    menus.sort()
    orders.sort()

    for order in orders:
        result = is_existing_target_number_binary(order, menus)
        if result == False:
            return False

    return True

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

result = is_available_to_order(shop_menus, shop_orders)
print(result)