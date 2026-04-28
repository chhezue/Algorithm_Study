def solution(cost, hint):
    k = len(hint[0][1:]) # 힌트권 개수
    my_hint = []

    def min_cost(index, my_hint):
        # Base Case: 마지막 스테이지까지 마친 후
        if index == len(cost):
            return 0

        # 구매한 힌트권 사용
        count = my_hint.count(index + 1)
        if count >= len(cost) - 1:
            count = len(cost) - 1
        cur_cost = cost[index][count] # 힌트권을 사용한 스테이지 해결 비용

        # 1. 힌트 번들을 구매하지 않는 경우
        cost_a = cur_cost + min_cost(index + 1, my_hint)

        # 2. 힌트 번들을 구매하는 경우
        # 마지막 스테이지가 아닌 경우
        if index != len(hint):
            buy_cost = hint[index][0]
            new_buy_hint = my_hint.copy()

            for j in range(1, k + 1):
                new_buy_hint.append(hint[index][j]) # 힌트권 각각 추가
            cost_b = cur_cost + buy_cost + min_cost(index + 1, new_buy_hint)
        # 마지막 스테이지에서는 번들을 살 수 없다.
        else:
            cost_b = cost_a

        return min(cost_a, cost_b)

    return min_cost(0, my_hint)