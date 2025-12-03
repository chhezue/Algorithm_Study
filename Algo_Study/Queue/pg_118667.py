from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    q1_sum = sum(q1)
    q2_sum = sum(q2)

    # 두 큐의 합이 홀수라면 /2 시 절반이 될 수 없으므로 -1
    if (q1_sum + q2_sum) % 2 == 1:
        return -1
    if q1_sum == q2_sum: # 이미 같으면 0
        return 0

    max_count = len(queue1) * 10
    target_sum = (q1_sum + q2_sum) // 2

    while q1_sum != target_sum and answer < max_count:
        if q1_sum > q2_sum and q1:
            item = q1.popleft()
            q2.append(item)
        elif q2_sum > q1_sum and q2:
            item = q2.popleft()
            q1.append(item)

        answer += 1
        q1_sum = sum(q1)
        q2_sum = sum(q2)

    if q1_sum != q2_sum:
        return -1
    else:
        return answer

print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))