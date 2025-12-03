def stack_sequence(n, sequence):
    # sequence = [4, 3, 6, 8, 7, 5, 2, 1]
    # n = 8
    stack = []
    ops = [] # 결과 배열
    j = 0 # sequence 배열의 인덱스

    for i in range(1, n + 1):
        stack.append(i)
        ops.append("+")
        while stack and j < n and stack[-1] == sequence[j]:
            stack.pop()
            ops.append("-")
            j += 1

    if j != n:
        print("NO")
    else:
        print("\n".join(ops))

sequence = list()
n = int(input())
for _ in range(n):
    sequence.append(int(input()))
stack_sequence(n, sequence)