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

    while True:
        # 정답을 찾은 경우
        if q1_sum == q2_sum:
            break
        # 정답을 찾지 못했고, 무한 루프가 발생하는 경우
        if answer >= max_count:
            return -1

        # q1의 합이 더 큰 경우, 하나를 빼서 q2에 넣는다.
        if q1_sum > q2_sum:
            item = q1.popleft()
            q2.append(item)
            q2_sum += item
            q1_sum -= item
        elif q1_sum < q2_sum:
            item = q2.popleft()
            q1.append(item)
            q1_sum += item
            q2_sum -= item

        answer += 1

    return answer

print(solution([3, 2, 7, 2], [4, 6, 5, 1])) # 2
print(solution([1, 2, 1, 2], [1, 10, 1, 2])) # 7
print(solution([1, 1], [1, 5])) # -1