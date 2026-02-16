import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split())) # [3, 5, 2, 7]
stack = [] # 아직 오큰수를 찾지 못한 요소가 들어가야 한다.
result = [-1] * n # 오큰수 결과를 저장할 배열

for i in range(n):
    # 스택이 비어 있지 않고, 현재 값이 top의 오큰수가 되는 경우
    # 현재 스택에 있는 요소들을 peek 하며, arr[i]가 top의 오큰수가 될 수 있는지 검사해야 한다.
    # 종료 조건: top이 오큰수가 될 수 없으면 바로 종료
    # 현재 top이 오큰수가 될 수 없으면, 자연스럽게 아래에 쌓인 요소들은 볼 필요가 없음.
    while stack and arr[stack[-1]] < arr[i]:
        result[stack[-1]] = arr[i]
        stack.pop()

    # 1. 스택이 비어 있는 경우
    # 2. top 하나를 검사했는데 그것의 오큰수가 될 수 없는 경우
    # 3. 스택에 쌓인 요소의 오큰수를 전부 정한 후
    stack.append(i) # 자기 자신도 오큰수를 찾아야 하므로 스택에 append

print(*result)