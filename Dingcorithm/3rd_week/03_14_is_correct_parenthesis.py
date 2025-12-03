def is_correct_parenthesis(string):
    stack = []

    for char in string:
        if char == "(":
            stack.append(char)
        else:
            if not stack: # 스택이 비어 있으면
                return False
            if stack[-1] == "(": # 짝이 맞는 경우
                stack.pop()
            else: # 짝이 맞지 않는 경우
                return False

    if stack:
        return False

    return True

print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))