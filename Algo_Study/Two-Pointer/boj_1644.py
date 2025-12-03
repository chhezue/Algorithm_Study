import sys
def input(): return sys.stdin.readline().rstrip()

def primes_under(n):
    if n <= 2:
        return []

    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    i = 2
    while i * i < n:
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
        i += 1

    return [i for i in range(n) if is_prime[i]]

def solution(n):
    if n == 1:
        return 0

    # n 이하의 자연수 중 소수가 들어간 배열(정렬되어 있음)
    arr = primes_under(n + 1)
    result = 0

    for i in range(len(arr)):
        prefix_sum = 0
        for j in range(i, len(arr)):
            prefix_sum += arr[j]
            if prefix_sum > n:
                break
            if prefix_sum == n:
                result += 1
                break

    return result

n = int(input())
print(solution(n))