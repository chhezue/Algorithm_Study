input = 50

# memo 라는 변수에 Fibo(1), Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}

def fibo_dynamic_programming(n, fibo_memo):
    # 1. 메모에 이미 해당 값이 있으면 반환
    if n in fibo_memo:
        return fibo_memo[n]

    # 2. 만약 없다면, 피보나치를 통해 그 값을 구하고 메모에 저장
    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo

    return nth_fibo

print(fibo_dynamic_programming(input, memo))